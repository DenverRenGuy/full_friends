from flask import Flask, redirect, render_template, session, flash, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'ShhhSneaky'
mysql = MySQLConnector(app, 'fullFriends')

#CRUD Operations
allQuery = 'SELECT u.last_name, u.first_name, u.created_at FROM users u ORDER BY u.last_name DESC'


@app.route('/')
def index():
    allFriends = mysql.query_db(allQuery)
    return render_template('index.html', allFriends = allFriends)

@app.route('/create', methods=['POST'])
def create():
    d = request.form
    createQuery = 'INSERT INTO users(first_name, last_name, created_at) VALUES (:first_name, :last_name, NOW());'
    data = {
            'first_name': d['first_name'],
            'last_name': d['last_name']
    }
    mysql.query_db(createQuery, data)
    flash('Friend Record Added Successfully!')
    return redirect('/')



app.run(debug=True)
