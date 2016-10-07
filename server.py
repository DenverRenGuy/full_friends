from flask import Flask, redirect, render_template, session, flash, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'ShhhSneaky'
mysql = MySQLConnector(app, 'fullFriends')

#CRUD Operations
allQuery = 'SELECT u.id, u.last_name, u.first_name, u.created_at FROM users u ORDER BY u.last_name ASC'


@app.route('/')
def index():
    allFriends = mysql.query_db(allQuery)
    return render_template('index.html', allFriends = allFriends)

@app.route('/friends', methods=['POST'])
def create():
    d = request.form
    createQuery = 'INSERT INTO users(first_name, last_name, created_at) VALUES (:first_name, :last_name, NOW());'
    data = {
            'first_name': d['first_name'],
            'last_name': d['last_name']
    }
    mysql.query_db(createQuery, data)
    flash('Friend Record Added Successfully!', 'success')
    return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET'])
def edit(id):
    singleQuery = 'SELECT u.id, u.last_name, u.first_name FROM users u WHERE u.id = :id'
    data = {
            'id': id
    }
    friends = mysql.query_db(singleQuery, data)
    return render_template('edit.html', friends = friends)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    d = request.form
    updateQuery = 'UPDATE users SET first_name = :first_name, last_name = :last_name, last_update = NOW() WHERE id = :id'
    data = {
            'first_name': d['first_name'],
            'last_name': d['last_name'],
            'id': id
    }
    mysql.query_db(updateQuery, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    deleteQuery = 'DELETE FROM users WHERE id = :id'
    data = {'id': id}
    mysql.query_db(deleteQuery, data)
    return redirect('/')

app.run(debug=True)
