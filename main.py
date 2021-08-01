from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'project_manager'
# intialize MySQL
mysql = MySQL(app)

# secret key
app.secret_key = "sk"


# routes
@app.route('/')
def Index():
    # check if user is loggedin
    if 'loggedin' in session:
        # user is loggedin show them the home page
        return render_template('home.html', username=session['username'], title="Home")
    # user is not loggedin redirect to login page
    return render_template('home.html')


@app.route('/registers', methods=['POST', 'GET'])
def registers():
    if request.method == 'POST':
        niu = request.form['niu']
        password = request.form['password']
        average_grade = request.form['average_grade']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (niu, password, average_grade) VALUES (%s,%s,%s)", (niu, password, average_grade))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return render_template('registers.html')
    return render_template('registers.html')

@app.route('/registerp', methods=['POST', 'GET'])
def registerp():
    if request.method == 'POST':
        niu = request.form['niu']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO professor (niu, password) VALUES (%s,%s)", (niu, password))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return render_template('registerp.html')
    return render_template('registerp.html')

@app.route('/shedulepn', methods=['POST', 'GET'])
def shedulepn():
    if request.method == 'POST':
        nshedules = request.form['nshedules']
        listshedules = list()
        for i in range(int(nshedules)):
            listshedules.append(i)
        return render_template('shedulep.html', nshedules = listshedules)
    return render_template('shedulepn.html')

@app.route('/shedulep/<nshedules>', methods=['POST', 'GET'])
def shedulep(nshedules):
    if request.method == 'POST':
        print(nshedules)
        print(nshedules)
        schedule_day = request.form['schedule_day']
        schedule_hour = request.form['schedule_hour']
        #print(schedule_day)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO schedule (date, time) VALUES (%s, %s)", (schedule_day, schedule_hour))
        mysql.connection.commit()
        return render_template('shedulep.html')
    #return render_template('shedulep.html')


# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
