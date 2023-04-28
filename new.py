from flask import Flask, render_template, request
import sqlite3 as sql

conn = sql.connect('database.db')
print("opened database successfully")

conn.execute('CREATE TABLE stud (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(home.html)


@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST','GET'])
def addres():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,addre,city,pin) VALUES [?,?,?,?]", (nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg = msg)
            con.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row 

    cur = con.cursor()
    cur.exceute("Select * from students")

    rows = cur.fetchall();
    return render_template("list.html", rowa = rows)

if __name__ == '__main__':
    app.run(debug = True)
