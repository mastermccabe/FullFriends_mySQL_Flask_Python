from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query

print("***************** FRIENDSHIPS *******************")
print mysql.query_db("SELECT * FROM friendships")
print("****************** USERS ******************")
print mysql.query_db("SELECT * FROM users")

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)

@app.route('/users', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'age': request.form['age']
           }
    mysql.query_db(query, data)
    return redirect('/')


# Say we wanted to update a specific record, we could create another page and add a form that would submit to the following route:
@app.route('/update_age', methods=['POST'])
def update():
    query = "UPDATE users SET age = :age WHERE id = :id"
    data = {
             'age': request.form['age2'],
             'id': request.form['user_id2']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/delete_users', methods=['POST'])
def delete():
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': request.form['user_id']}
    mysql.query_db(query, data)
    return redirect('/')




app.run(debug=True)
