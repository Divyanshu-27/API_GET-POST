from sqlite3.dbapi2 import Cursor
import MySQLdb
from MySQLdb import cursors
import bcrypt
from flask import Flask,jsonify, render_template,request, redirect , url_for ,flash
from flask.helpers import flash
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL



app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config ["MYSQL_HOST"] = "localhost"
app.config ["MYSQL_USER"] = "root"
app.config ["MYSQL_PASSWORD"]= "root"
app.config ["MYSQL_DB"]= "d1"


mysql = MySQL(app)



@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM data")
    data = cur.fetchall()
    cur.close()




    return render_template('data.html' )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        Gmail = request.form['Gmail']
        name = request.form['name']
        password = request.form['password']= Bcrypt.generate_password_hash
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO data (Gmail, name ,password) VALUES (%s, %s, %s)", (Gmail,name, password))
        mysql.connection.commit()
    return redirect(url_for('index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM data WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
   