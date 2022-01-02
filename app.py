from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)


app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='regform'

mydb = mysql.connector.connect(
  host="",
  user="",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE regform")


mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database="regform"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE userdata(name VARCHAR(150), age INT(3), email VARCHAR(150), mobile VARCHAR(10), location VARCHAR(100));")


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        age = details['age']
        email = details['email']
        mobile = details['mobile']
        location = details['location']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdata(name, age, email, mobile, location) VALUES (%s, %s, %s, %s, %s)", (name, age, email, mobile, location))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


@app.route('/users')
def users():
    cur =mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM userdata")
    if resultValue > 0:
        usersDetails = cur.fetchall()

        return render_template('users.html',usersDetails=usersDetails)

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=80)
