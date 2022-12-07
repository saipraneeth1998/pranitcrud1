from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import mysql.connector
import logging

app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.INFO,format='%(levelname)s:%(message)s')

app.config['MYSQL_HOST'] = 'db1.caomyyms75ok.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'Praneeth'
app.config['MYSQL_PASSWORD'] = '123456789'
app.config['MYSQL_DB'] ='STUDENTS'

mydb = mysql.connector.connect(
  host="db1.caomyyms75ok.us-east-1.rds.amazonaws.com",
  user="Praneeth",
  password="123456789"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE STUDENTS")


mydb = mysql.connector.connect(
  host="db1.caomyyms75ok.us-east-1.rds.amazonaws.com",
  user="Praneeth",
  password="123456789",
  database="STUDENTS"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE userdata(name VARCHAR(150), age INT(3), email VARCHAR(150), mobile VARCHAR(10));")


mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        logging.info(name)
        age = details['age']
        email = details['email']
        mobile = details['mobile']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userdata(name, age, email, mobile) VALUES (%s, %s, %s, %s)", (name, age, email, mobile))
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
