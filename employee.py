from flask import *
from database import *
import uuid
employee=Blueprint('employee',__name__)

@employee.route('/employeehome',methods=['get','post'])
def employeehome():
	return render_template('employee_home.html')



@employee.route('/viewprofile',methods=['get','post'])
def viewprofile():
	data={}
	ids = session['login_id']
	q = "SELECT * FROM `employee` inner join department using(dep_id) inner join login using(login_id) WHERE login_id='%s'" % (ids)
	res = select(q)
	data['my'] = res
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None
	if action == 'update':
		q = "select * from employee where login_id='%s'" % (ids)
		res = select(q)
		data['updatecat'] = res

	if 'update' in request.form:
		fname = request.form['fname']
		lname = request.form['lname']
		mobile = request.form['mobile']
		photo = request.files['image']
		path='static/uploads/'+str(uuid.uuid4())+photo.filename
		photo.save(path)
		q = "update employee set firstname='%s',lastname='%s',contact='%s',photo='%s' where login_id='%s'" % (fname,lname,mobile,path,ids)
		update(q)
		return redirect(url_for('employee.viewprofile'))
	return render_template('employee_view_profile.html',data=data)



# @employee.route('/employeehome',methods=['get','post'])
# def employeehome():
# 	return render_template('employee_home.html')