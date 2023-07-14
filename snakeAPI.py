import sqlite3
from flask import *
import json
from snake import Snake


app = Flask(__name__)


def connect_db():
    db = sqlite3.connect("snake.db").cursor()
    db.execute(
        "CREATE TABLE IF NOT EXISTS SNAKES("
        "family TEXT, genus TEXT, species TEXT, subspecies TEXT, averagelength INTEGER, area TEXT, optimaltemp INTEGER)"
    )
    db.connection.close


@app.route('/', methods=['GET'])
def index():
    connect_db()
    return "Welcome to the snake API !"

@app.route('/snakes/', methods=['GET'])
def get_snakes():
    db = sqlite3.connect("snake.db").cursor()
    db.execute(
        "SELECT * FROM SNAKES"
    )
    data = db.fetchall()
    return jsonify(data)


@app.route('/getSnakesBy')
def get_snakes_by_genus():
    db = sqlite3.connect("snake.db").cursor()
    db.execute(
        "SELECT * FROM SNAKES WHERE genus =?", (snake.genus)
    )
    data = db.fetchall()
    return jsonify(data)

@app.route('/addSnake', methods=['POST'])
def add_snake():
    db = sqlite3.connect("snake.db")
    c = db.cursor()
    snake = Snake(request.form['family'],
                  request.form['genus'],
                  request.form['species'],
                  request.form['subspecies'],
                  request.form['averagelength'],
                  request.form['area'], 
                  request.form['optimaltemp'])
    print(snake)
    c.execute(
        "INSERT INTO SNAKES(family, genus, species, subspecies, averagelength, area, optimaltemp) VALUES(?,?,?,?,?,?,?)",
        (snake.family, snake.genus, snake.species, snake.subspecies, snake.averagelength, snake.area, snake.optimaltemp)
    )
    db.commit()
    data = c.lastrowid
    return json.dumps(data)

if __name__ == '__main__':
    app.run(port=8800)