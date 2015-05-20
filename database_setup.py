"""
Use ORM to build a new DB. This consists of the following steps:
1. Configuration:
	- Import the modules
	- Instantiate the base, declarative class (from which all other classes/objects will be derived)
	- At the end of the file, create the engine - Establish connectivity to the backend, creates the databse - \
          and create all the rows and tables that will be passed to it

2. Define the Class Code:
    Each table is class, inherited from Base
    
3. Define the table representation:
    Within each class, use the special variable __tablename__ = "some name", to define the table within he database.

4. Define the Mappers:
    Define the columnnames and derive it from the Column class. Each column has a set of attributes that \
    correspond to SQL attributes (string/integer, primary key/foreign key, nullable etc)

"""
#IMPORTS
import sys
from sqlalchemy import Column, ForeignKey, Integer, String #Note the lettering, indicating that these are all classes
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship #Used for ForeignKey mapping
from sqlalchemy import create_engine

#Instantiate the Base class
Base = declarative_base()

class Restaurant(Base): # 2. Class Code
    __tablename__ = "restaurant"  #3. Table Representation
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)





class MenuItem(Base): # 2. Class Code
    __tablename__ = "menu_item"
    id = Column(Integer, primary_key = True)
    name = Column(String(200), nullable = False)
    description = Column(String(200), nullable = False)
    course = Column(String(100), nullable = False)
    price = Column(String(100), nullable = False)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id')) # The tablename used in the prev Class followed by identifying column name is passed
    restaurant = relationship('Restaurant') # The previous Class itself is passed here 
    ## We will use the built-in function/decorator @property, in order to return RO attributes
    @property
    def serialize(self):
        return {
                'name' : self.name,
                'description' : self.description,
                'id' : self.id,
                'price' : self.price,
                'course' : self.course,
                }


#Create the Engine
engine = create_engine('sqlite:///restaurantmenu.db')
#Create all the tables and rows
Base.metadata.create_all(engine)

