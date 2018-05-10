import sqlite3
import getpass
conn = sqlite3.connect("test.db")
c= conn.cursor()
c.execute('
acc_type =rawinput("Type login to log in,and signup to sign up:")
while (acc_type != "login" and acc_type != "login" and acc_type != "login" and acc_type != "login"):
	acc_type =rawinput("Type login to log in,and signup to sign up:")
	if (acc_type == "signup" or acc_type == "sign up")
		first_name = input("first name:")
		last_name = input("Last name:")
		username = input("Username:")
		password = getpass.getpass("Password:")
		password2 = getpass.getpass("Confirm password:")
		while (password != password2):
			print ("Not identical!")
			password = getpass.getpass("Password:")
			password2 = getpass.getpass("Confirm password:")
			print ("Not identical!")
		email = input("email:")
		c.execute
	elif (acc_type == "login" or acc_type == "log in") :
		username = input("username:")
		password = getpass.getpass("Password:")
		c.execute('select * from test where username== %r and password== %r',usernamme,password)
		print (c.fetchall(),"\n")
