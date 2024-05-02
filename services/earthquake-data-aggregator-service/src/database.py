# database.py

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
URL_DATABASE = os.getenv("DATABASE_URL")

# Create the database if it doesn't exist
if not database_exists(URL_DATABASE):
    create_database(URL_DATABASE)

engine = create_engine(URL_DATABASE)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This creates the 'messages' table if it doesn't exist
Base.metadata.create_all(bind=engine)