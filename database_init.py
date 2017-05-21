from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(name="Nada Baynom",
              email="nbaynom0@skype.com",
              picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
session.add(User1)
session.commit()

## User2 = User(name="Renado Gress",
##               email="rgress1@t.co",
##               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
## session.add(User2)
## session.commit()

## User3 = User(name="Prinz Blakemore",
##               email="pblakemore2@bluehost.com",
##               picture='http://dummyimage.com/200x200.png/5fa2dd/ffffff')
## session.add(User3)
## session.commit()

## User4 = User(name="Ev Beetham",
##               email="ebeetham3@google.com.au",
##               picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
## session.add(User4)
## session.commit()

## User5 = User(name="Tamra Eyree",
##               email="teyree4@wix.com",
##               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
## session.add(User5)
## session.commit()

# Create fake categories
Category1 = Category(name="Football",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Cars",
                      user_id=2)
session.add(Category2)
session.commit

Category3 = Category(name="Snacks",
                      user_id=1)
session.add(Category3)
session.commit()

Category4 = Category(name="Gadgets",
                      user_id=1)
session.add(Category4)
session.commit()

Category5 = Category(name="Food",
                      user_id=1)
session.add(Category5)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="Football Boots",
               date=datetime.datetime.now(),
               description="Shoes to play football in.",
               picture="http://bit.ly/2qHbHxd",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="Football Shirt",
               date=datetime.datetime.now(),
               description="Shirt to play football in.",
               picture="http://bit.ly/2pb59qn",
               category_id=1,
               user_id=1)
session.add(Item2)
session.commit()

Item3 = Items(name="Football",
               date=datetime.datetime.now(),
               description="A Football.",
               picture="http://bit.ly/2pJSPR1",
               category_id=1,
               user_id=1)
session.add(Item3)
session.commit()

print "Your database has been populated with fake data!"