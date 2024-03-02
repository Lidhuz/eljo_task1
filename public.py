from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def index():
	return render_template('index.html')



@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['email']
		password=request.form['password']
		q="select * from login where email='%s' and password='%s'"%(username,password)
		res=select(q)

		if res:
			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('master.masterhome'))
	
			if res[0]['usertype']=="employee":
				return redirect(url_for('employee.employeehome'))

		else:
			flash("Incorrect email or password.")
	return render_template('login.html')