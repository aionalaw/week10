from flask import Flask, url_for, redirect, render_template, request


import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_employee():
   return render_template('employee.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         gender = request.form['gender']
         phone = request.form['phone']
         bdate = request.form['bdate']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cmd = "INSERT INTO employee (EmpName,EmpGender,EmpPhone,EmpBdate) VALUES ('{0}','{1}','{2}','{3}')".format(name,gender,phone,bdate)
            cur.execute(cmd)
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
         
      finally:
         return render_template("output.html",msg = msg)
         con.close()

@app.route('/info')
def info():
   con = sql.connect("employee.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from employee")
   
   rows = cur.fetchall(); 
   return render_template("info.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)

