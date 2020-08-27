from flask import Flask, render_template, request, session, make_response, redirect
from appointments import Appointments
from user import User,Details
from data import *
import uuid

app = Flask(__name__)
app.debug = True
app.env = 'development'

@app.route('/')
def home_template():
    return render_template('template/home.html')

@app.route('/logout')
def logout():
    User.logout()
    return redirect("/")

@app.route('/login_user', methods=['POST', 'GET'])
def login_user():
	return render_template('template/new.html',message="To be implemented")

@app.route('/login_admin', methods=['POST','GET'])
def login_page():
    return render_template('template/login.html')

@app.route('/login_admin_valid', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email=="admin":
            if password=="admin":
                return render_template("template/dashboard.html")         
    return "error detected"

@app.route('/addmember',methods=['POST','GET'])
def memberregistration():
    if request.method == 'POST':
        name = request.form['fullname']
        email = request.form['email']
    uid = adduser(name=name,email=email)
    if uid==-1:
        return render_template('template/new.html',message="User already exists")
    else:
        return render_template('template/new.html',message="Registered with id : "+uid)

@app.route('/editmember',methods=['POST','GET'])
def editmember():
    if request.method == 'POST':
        uid = request.form['uid']
        name = request.form['fullname']
        email = request.form['email']
        password = request.form['password']
    if userexists(uid):
        editdetails(uid,name,email,password)
        return render_template('template/new.html',message='Details edited successfully')
    else:
        return render_template('template/new.html',message='User does not exist in system')        

@app.route('/listmembers',methods=['POST','GET'])
def listmembers():
    df = showmembers()
    users_list = [User(df['id'][index], df['name'][index]) for index in range(len(df))]
    return render_template('template/listmember.html',message=users_list)

@app.route('/viewmembers',methods=['POST','GET'])
def viewmembers():
    df = showdetails()
    detailed_list = [Details(df['id'][index],df['name'][index],df['email'][index]) for index in range(len(df))]
    return render_template('template/listdetails.html',message=detailed_list)

@app.route('/addtiming',methods=['POST','GET'])
def inserttime():
    if request.method=='POST':
        uid = request.form['uid']
        day = request.form.get('day')
        time = request.form.get('time')
    result = addtime(uid,day,time)
    if result:
        return render_template('template/new.html',message="Added successfully")
    else:
        return render_template('template/new.html',message='Uid does not exist')

@app.route('/listtiming',methods=['GET','POST'])
def listtiming():
    result = showtimes()
    print(result)
    mod_result = [Appointments(result['id'][index],result['day'][index],result['slot'][index]) for index in range(len(result))]
    return render_template('template/allappointments.html',message=mod_result)

@app.route('/viewsingletiming',methods=['GET','POST'])
def showtime():
    if request.method=='POST':
        uid = request.form['uid']
    result = showmtime(uid)
    if len(result)==0:
        return render_template('template/new.html',message='Uid does not exist')
    else:
        mod_result=[Appointments(result['id'][index],result['day'][index],result['slot'][index]) for index in range(len(result))]
        return render_template('template/allappointments.html',message=mod_result)

@app.route('/removetiming',methods=['GET','POST'])
def deletetime():
    if request.method=='POST':
        uid = request.form['uid']
        day = request.form.get('day')
        time = request.form.get('time')
    result = removetime(uid,day,time)
    return render_template('template/new.html',message='Processed')

@app.route('/removeuser',methods=['GET','POST'])
def deletuser():
    if request.method=='POST':
        uid = request.form['uid']
        email = request.form['email']
    result = removeuser(uid,email)
    if result:
        return render_template('template/new.html',message="Success")
    else:
        return render_template('template/new.html',message="User not found") 




if __name__=='__main__':
    app.run()