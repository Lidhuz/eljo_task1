from flask import *
from database import *
master=Blueprint('master',__name__)

@master.route('/masterhome',methods=['get','post'])
def masterhome():
	return render_template('master_home.html')


@master.route('/masteradddep',methods=['get','post'])
def masteradddep():
	if 'submit' in request.form:
		depname=request.form['dname']
		q="select * from department where dep_name='%s'"%(depname)
		res=select(q)
		if len(res)>0:
			flash("The Fuel Category Is Already Exists")
		else:
			q="insert into department values(null,'%s')"%(depname)
			insert(q)
			flash("Department Added")
			return redirect(url_for('master.masteradddep'))
	return render_template('master_add_department.html')


@master.route('/masterviewdep',methods=['get','post'])
def masterviewdep():
	data = {}
	if 'action' in request.args:
		action = request.args['action']
		id = request.args['id']
	else:
		action = None

	if action == 'delete':
		q = "delete from department where dep_id='%s'" % (id)
		delete(q)
		return redirect(url_for('master.masterviewdep'))

	if action == 'update':
		q = "select * from department where dep_id='%s'" % (id)
		res = select(q)
		data['updatecat'] = res

	if 'update' in request.form:
		categoryname = request.form['cname']
		q = "update department set dep_name='%s' where dep_id='%s'" % (categoryname, id)
		update(q)
		return redirect(url_for('master.masterviewdep'))

	q = "select * from department"
	res = select(q)
	data['Cat'] = res
	return render_template('master_view_department.html',data=data)



@master.route('/masteraddempl',methods=['get','post'])
def masteraddempl():
	data={}
	ids = session['login_id']
	if 'submit' in request.form:
		categ = request.form['Category']
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		mob=request.form['mobile']
		psw=request.form['password']
		q = "select * from login where email='%s'" % (email)
		res = select(q)
		if len(res) > 0:
			flash("Your Email ID Already Exists ")
		else:
			q = "insert into login values(null,'%s','%s','employee')" % (email, psw)
			result = insert(q)
			q = "insert into employee values(null,'%s',(select dep_id from department where dep_id='%s'),'%s','%s','%s','null')" % (result,categ,fname,lname,mob)
			insert(q)
			flash("Employee Registration Successfully Completed")
	q="select * from department"
	res = select(q)
	data['cat'] = res
	return render_template('master_add_employee.html',data=data)


@master.route('/masterviewempl',methods=['get','post'])
def masterviewempl():
	data={}
	ids = session['login_id']
	q="SELECT * FROM department "
	res = select(q)
	data['dep'] = res

	if 'submit' in request.form:
		name = request.form['place']
		q="SELECT * FROM employee inner join login using(login_id) inner join department using(dep_id) where dep_name='%s'"%(name)
		res = select(q)
		data['emp'] = res

	return render_template('master_view_employee.html',data=data)

