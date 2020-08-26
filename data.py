import pandas as pd
import uuid
import csv

users = pd.read_csv('data/users.csv')
appointments = pd.read_csv('data/appointments.csv')

def uid_gen():
	uid=uuid.uuid4().hex
	return uid

def adduser(name,email,password='pass1234',id=uid_gen()):
	if users['email'].isin([email]).any():
		return -1
	with open('data/users.csv','a',newline="") as f:
		csvwriter = csv.writer(f)
		csvwriter.writerow([name,email,uid,password])
	return uid

def userexists(uid):
	if users['id'].isin([uid]).any():
		return 1
	else:
		return -1

def editdetails(uid,name,email,password):
	index = users.index[users['id']==uid].tolist()[0]
	users.set_value(index,'name',name)
	users.set_value(index,'email',email)
	users.set_value(index,'id',uid)
	users.set_value(index,'password',password)
	users.to_csv('data/users.csv',index=False)

def showmembers():
	colums = ['id','name']
	ans = users[colums]
	return ans

def showdetails():
	colums = ['id','name','email']
	return users[colums]
	
def addtime(uid,day,time):
	if users['id'].isin([uid]).any():
		with open('data/appointments.csv','a',newline="") as f:
			csvwriter = csv.writer(f)
			csvwriter.writerow([uid,day,time])
		return 1
	else:
		return -1

def showtimes():
	return appointments

def showmtime(uid):
	return appointments[appointments['id']==uid]
