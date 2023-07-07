import sqlite3
from flask import *
import json
from snake import snake


app = Flask(__name__)

def connect_db():
    db = sqlite3.connect('snake.db').cursor()
    db.execute("CREATE TABLE IF NOT EXISTS SNAKES("
               "family TEXT, genus TEXT, species TEXT, subspecies TEXT, averagelength INTEGER, area TEXT, optimaltemp INTEGER)"  
              )
    db.connection.close