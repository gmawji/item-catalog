#===================
# Imports
#===================
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database_setup import *
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import os, random, string, datetime, json, httplib2, requests

#===================
# Flask instance
#===================
app = Flask(__name__)

#===================
# GConnect CLIENT_ID
#===================
#CLIENT_ID = json.loads(
#    open('client_secrets.json', 'r').read())['web']['client_id']
#APPLICATION_NAME = "Item Catalog Application"

#===================
# DB
#===================
# Connect to database
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
# Create session
DBSession = sessionmaker(bind=engine)
session = DBSession()


#===================
# Flask Routing
#===================
# Homepage
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Items).order_by(desc(Items.date)).limit(5)
    return render_template('public_catalog.html',
                            categories = categories,
                            items = items)

# Category Items
@app.route('/<category_name>/items/')
@app.route('/catalog/<category_name>/items/')
def showCategory(category_name):
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Items).filter_by(name=category_name)\
                                .order_by(asc(Items.name))
    print items
    count = session.query(Items).filter_by(category=category).count()
    return render_template('public_items.html',
                            category = category.name,
                            categories = categories,
                            items = items,
                            count = count)


# url_for static path processor
# remove when deployed
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

# Always at end of file !Important!
if __name__ == '__main__':
    app.secret_key = 'DEV_SECRET_KEY'
    app.debug = False
    app.run(host = '0.0.0.0', port = 5000)