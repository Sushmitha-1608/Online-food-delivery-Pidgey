from flask import *
from sqlalchemy import and_
from sqlalchemy import or_
from app.models import Customer, Restadmin, Items, Orders, Diginadmin
from app import app, db


@app.route('/')
@app.route('/index')
def index():

	return render_template('index.html',restadmin = Restadmin.query.all())

@app.route('/indexmenu', methods = ['GET','POST'])
def indexmenu():


	if request.method == "GET":
		restid = request.args.get("restid")
	
	elif request.method == "POST":
		restid = request.form['restid']

	items = Items.query.filter(Items.rid == restid).all()
	restad = Restadmin.query.filter(Restadmin.rid == restid).first()
	return render_template('indexmenu.html',restad=restad, restadmin=items)


@app.route('/register')
def register():
	return render_template('userregister.html')


@app.route('/registerNext', methods = ['GET','POST'])
def registerNext():

	if request.method == "GET":
		cmail = request.args.get("cmail")
		cpassword = request.args.get("cpassword")

	elif request.method == "POST":
		cmail = request.form['cmail']
		cpassword = request.form['cpassword']


		customercheck = Customer.query.filter(and_(Customer.cmail == cmail, Customer.cpassword == cpassword)).first()


		if customercheck :

			return render_template('userregister.html',cmsg="Registration Failed, \n User Already Registered..!")

		else:
		
			customer = Customer(cname=request.form["cname"], cmail=request.form["cmail"], cmobile=request.form["cmobile"], caddress=request.form["caddress"], cpassword=request.form['cpassword'])
					
			db.session.add(customer)
			db.session.commit()


			return render_template('userlogin.html',cusmsg="Registered Succcessfully...! \n Please Login To Continue")


@app.route('/login')
def login():
	return render_template('userlogin.html')


@app.route('/loginNext',methods=['GET','POST'])
def loginNext():

	if request.method == "GET":
		cmail = request.args.get("cmail")
		cpassword = request.args.get("cpassword")
	
	elif request.method == "POST":
		cmail = request.form['cmail']
		cpassword = request.form['cpassword']

		
		customer  = Customer.query.filter(and_(Customer.cmail == cmail, Customer.cpassword == cpassword)).first()


		if customer :
			session['cmail'] = request.form['cmail']
			return redirect(url_for('userhome1'))
			
		return render_template('userlogin.html',cusname="Login failed...\n Please enter valid username and password!")


@app.route('/userhome1',methods=['GET','POST'])
def userhome1():
	if not session.get('cmail'):
		return redirect(request.url_root)
	cmail=session['cmail']
	customer  = Customer.query.filter(Customer.cmail == cmail).first()

	return render_template('userhome.html',cusname=customer.cname,restadmin = Restadmin.query.all())


@app.route('/userorders',methods=['GET','POST'])
def userorders():
	if not session.get('cmail'):
		return redirect(request.url_root)
	cmail=session['cmail']
	customer  = Customer.query.filter(Customer.cmail == cmail).first()
	cid=customer.cid
	myorders = Orders.query.filter(Orders.cid == cid)

		
	return render_template('userorders.html',cusname=customer.cname,restadmin = customer.query.all(), myorders=myorders)



@app.route('/showuserprofile', methods = ['GET','POST'])
def showuserprofile():
	if not session.get('cmail'):
		return redirect(request.url_root)
	cmail=session['cmail']

	customer=Customer.query.filter(Customer.cmail==cmail).first()

	return render_template('showuserprofile.html',cusname=customer.cname,cusinfo = customer)



@app.route('/updateuserprofile',methods = ['GET','POST'])
def updateuserprofile():
	if not session.get('cmail'):
		return redirect(request.url_root)
	return render_template('updateuserprofile.html')


@app.route('/updateuserprofileNext', methods = ['GET','POST'])
def updateuserprofileNext():
	if not session.get('cmail'):
		return redirect(request.url_root)
	cmail=session['cmail']

	cpassword = request.form['cpassword']
	
	customer=Customer.query.filter(Customer.cmail==cmail).first()
	customer.cpassword=cpassword
	db.session.commit()
	return render_template('updateuserprofile.html', cmsg="Passsword Updated Succcessfully...!")


# customerlogout.html
@app.route('/logout')
def logout():
	session.pop('cmail',None)
	return redirect(url_for('index'))



@app.route('/restmenu', methods = ['GET','POST'])
def restmenu():
	if not session.get('cmail'):
		return redirect(request.url_root)

	if request.method == "GET":
		restid = request.args.get("restid")
	
	elif request.method == "POST":
		restid = request.form['restid']

	items = Items.query.filter(Items.rid == restid).all()
	restad = Restadmin.query.filter(Restadmin.rid == restid).first()
	return render_template('restmenu.html',restad=restad, restadmin=items)

@app.route('/restlogin')
def restlogin():
	return render_template('restlogin.html')

@app.route('/restlogin1')
def restlogin1():
	return render_template('restlogin1.html')
	
# restadminloginNext.html
@app.route('/restloginNext',methods=['GET','POST'])
def restloginNext():

	if request.method == "GET":
		rmail = request.args.get("rmail")
		rpassword = request.args.get("rpassword")
	
	elif request.method == "POST":
		rmail = request.form['rmail']
		rpassword = request.form['rpassword']

		
		restadmin1  = Restadmin.query.filter(and_(Restadmin.rmail == rmail, Restadmin.rpassword == rpassword)).first()


		if restadmin1 :
			session['rmail'] = request.form['rmail']
			return redirect(url_for('resthome1'))
			
		return render_template('restlogin.html',rusname="Login failed...\n Please enter valid username and password!")


@app.route('/restloginNext1', methods=['GET', 'POST'])
def restloginNext1():
	if request.method == "GET":
		rmail = request.args.get("rmail")
		rpassword = request.args.get("rpassword")

	elif request.method == "POST":
		rmail = request.form['rmail']
		rpassword = request.form['rpassword']

		restadmin2 = Restadmin.query.filter(and_(Restadmin.rmail == rmail, Restadmin.rpassword == rpassword)).first()

		if restadmin2:
			session['rmail'] = request.form['rmail']
			return redirect(url_for('resthome2'))

		return render_template('restlogin12.html', rusname="Login failed...\n Please enter valid username and password!")

@app.route('/resthome1',methods=['GET','POST'])
def resthome1():
	if not session.get('rmail'):
		return redirect(request.url_root)
	rmail=session['rmail']
	restadmin  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	rid=restadmin.rid

	myorders = Orders.query.filter(and_(Orders.rid == rid, Orders.ostatus=='pending'))
	return render_template('resthome.html',rusname=restadmin.rname,restadmin = Restadmin.query.all(), myorders=myorders)

@app.route('/resthome2',methods=['GET','POST'])
def resthome2():
	if not session.get('rmail'):
		return redirect(request.url_root)
	rmail=session['rmail']
	restadmin  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	rid=restadmin.rid

	myorders = Orders.query.filter(and_(Orders.rid == rid, Orders.ostatus=='pending'))
	return render_template('resthome12.html',rusname=restadmin.rname,restadmin = Restadmin.query.all(), myorders=myorders)

@app.route('/acceptorreject',methods=['GET','POST'])
def acceptorreject():
	if not session.get('rmail'):
		return redirect(request.url_root)
	rmail=session['rmail']

	ohash = request.form['ohash']
	acceptreject=	request.form['acceptreject']

	if acceptreject=="accept":
		orders=Orders.query.filter(Orders.ohash==ohash).first()
		orders.ostatus="accepted"
		db.session.commit()
		
	
	if acceptreject=="reject":
		Orders.query.filter(Orders.ohash == ohash).delete()
		db.session.commit()
		

	restadmin  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	rid=restadmin.rid

	myorders = Orders.query.filter(Orders.rid == rid)

	return redirect(url_for('resthome2'))


@app.route('/restacceptedorders',methods=['GET','POST'])
def restacceptedorders():
	if not session.get('rmail'):
		return redirect(request.url_root)
	rmail=session['rmail']
	restadmin  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	rid=restadmin.rid
	myorders = Orders.query.filter(and_(Orders.rid == rid, Orders.ostatus=='accepted'))
	restadmin  = Restadmin.query.filter(Restadmin.rmail == rmail).first()

	
	return render_template('restacceptedorders.html',rusname=restadmin.rname,restadmin = Restadmin.query.all(), myorders=myorders)

@app.route('/showmyrestmenu',methods=['GET','POST'])
def showmyrestmenu():
	if not session.get('rmail'):
		return redirect(request.url_root)
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid
	items = Items.query.filter(Items.rid == restid).all()


	return render_template('showmymenu.html',restad=restad, restadmin=items)

@app.route('/additem')
def additem():
	if not session.get('rmail'):
		return redirect(request.url_root)
	return render_template('additem.html')


@app.route('/additemNext',methods = ['GET','POST'])
def additemNext():
	if not session.get('rmail'):
		return redirect(request.url_root)
	if request.method == "GET":
		iname = request.args.get("iname")
		iprice = request.args.get("iprice")

	elif request.method == "POST":
		iname = request.form['iname']
		iprice = request.form['iprice']

	
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid

	items = Items(iname=request.form["iname"], iprice=request.form["iprice"], rid=restid)
	db.session.add(items)
	db.session.commit()
	
	return redirect(url_for('showmyrestmenu'))



@app.route('/updateitem',methods = ['GET','POST'])
def updateitem():
	if not session.get('rmail'):
		return redirect(request.url_root)
	return render_template('updateitem.html')


@app.route('/updateitemNext',methods = ['GET','POST'])
def updateitemNext():
	if not session.get('rmail'):
		return redirect(request.url_root)
	if request.method == "GET":
		iid = request.args.get("iid")
		iname = request.args.get("iname")
		iprice = request.args.get("iprice")
	
	elif request.method == "POST":
		iid = request.form['iid']
		iname = request.form['iname']
		iprice = request.form['iprice']

	
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid

	item = Items.query.filter(and_(Items.iid ==iid,Items.rid==restid)).first()
	if item :
		item.iname=iname
		item.iprice=iprice

		db.session.commit()
		return redirect(url_for('showmyrestmenu'))
	else :
		# return redirect(url_for('updateitem'))		
		return render_template('updateitem.html',imsg="Error! Item id does not belong to you..! ")



@app.route('/deleteitem',methods = ['GET','POST'])
def deleteitem():
	if not session.get('rmail'):
		return redirect(request.url_root)
	return render_template('removeitem.html')	


@app.route('/deleteitemNext',methods = ['GET','POST'])
def deleteitemNext():
	if not session.get('rmail'):
		return redirect(request.url_root)
	if request.method == "GET":
		iid = request.args.get("iid")
	
	elif request.method == "POST":
		iid = request.form['iid']
	
	rmail=session['rmail']
	restad  = Restadmin.query.filter(Restadmin.rmail == rmail).first()
	restid=restad.rid

	item = Items.query.filter(and_(Items.iid ==iid,Items.rid==restid)).first()
	if item :
		
		db.session.delete(item)
		db.session.commit()
		return redirect(url_for('showmyrestmenu'))
	else :
		return render_template('removeitem.html',imsg="Error! Item id does not belong to you..! ")


@app.route('/showrestprofile', methods = ['GET','POST'])
def showrestprofile():
	if not session.get('rmail'):
		return redirect(request.url_root)
	
	rmail=session['rmail']

	restadmin=Restadmin.query.filter(Restadmin.rmail==rmail).first()
	return render_template('showrestprofile.html',resinfo = restadmin)		


@app.route('/updaterestprofile',methods = ['GET','POST'])
def updaterestprofile():
	if not session.get('rmail'):
		return redirect(request.url_root)
	return render_template('updaterestprofile.html')


@app.route('/updaterestprofileNext', methods = ['GET','POST'])
def updaterestprofileNext():
	if not session.get('rmail'):
		return redirect(request.url_root)
	
	rmail=session['rmail']

	rpassword = request.form['rpassword']
	
	restadmin=Restadmin.query.filter(Restadmin.rmail==rmail).first()
	restadmin.rpassword=rpassword
	db.session.commit()
	return render_template('updaterestprofile.html', rmsg="Passsword Updated Succcessfully...!")



@app.route('/restlogout')
def restlogout():
	session.pop('rmail',None)
	return redirect(url_for('index'))


@app.route('/payment', methods = ['GET','POST'])
def payment():
	if not session.get('cmail'):
		return redirect(request.url_root)
	if request.method == "GET":
		tprice = request.args.get("total")
		items = request.args.get("items")
		rid=request.args.get("restid")
		
	
	elif request.method == "POST":
		tprice=request.form['total']
		items=request.form["items"]
		rid=request.form['restid']

	if(tprice=="0"):
	# return (str(tprice=="0"))
		return render_template('errorzero.html')	


	cmail=session['cmail']
	customer  = Customer.query.filter(Customer.cmail == cmail).first()


	restadmin  = Restadmin.query.filter(Restadmin.rid == rid).first()
	rname=restadmin.rname
	ostatus="pending"
	x={temp:items.count(temp) for temp in items}
	c=","
	x.pop(c)
	return render_template('payment.html', x=x , tprice=tprice, rname=rname ,items=items, rid=rid)



@app.route('/submitorder', methods = ['GET','POST'])
def submitorder():
	if not session.get('cmail'):
		return redirect(request.url_root)
	if request.method == "GET":
		tprice = request.args.get("tprice")
		items = request.args.get("items")
		rid=request.args.get("rid")

	elif request.method == "POST":
		tprice=request.form['tprice']
		items=request.form["items"]
		rid=request.form['rid']

	cmail=session['cmail']
	customer  = Customer.query.filter(Customer.cmail == cmail).first()

	restadmin  = Restadmin.query.filter(Restadmin.rid == rid).first()
	rid=restadmin.rid

	ostatus="pending"
	
	orders = Orders(cid=customer.cid, rid=rid, items=items,tprice=tprice,ostatus=ostatus)
	if orders :

		db.session.add(orders)
		db.session.commit()

		return render_template('lastpage.html')


	return render_template('payment.html')

@app.route('/adminlogin')
def adminlogin():

	return render_template('adminlogin.html')

@app.route('/adminloginNext',methods=['GET','POST'])
def adminloginNext():
	
	if request.method == "GET":
		amail = request.args.get("amail")
		apassword = request.args.get("apassword")

	elif request.method == "POST":
		amail = request.form['amail']
		apassword = request.form['apassword']


		diginadmin  = Diginadmin.query.filter(and_(Diginadmin.amail == amail, Diginadmin.apassword == apassword)).first()


		if diginadmin :
			session['amail'] = request.form['amail']
			return redirect(url_for('adminHome1'))

		return render_template('adminlogin.html',admmsg="Login failed...\n Please enter valid username and password!")



@app.route('/adminHome1',methods=['GET','POST'])
def adminHome1():
	if not session.get('amail'):
		return redirect(request.url_root)
	amail=session['amail']
	diginadmin  = Diginadmin.query.filter(Diginadmin.amail == amail).first()

	return render_template('adminhome.html')

@app.route('/restregisterbyadmin', methods = ['GET','POST'])
def restregisterbyadmin():
	if not session.get('amail'):
		return redirect(request.url_root)	
	if request.method == "GET":
		rmail = request.args.get("rmail")
		rmobile = request.args.get("rmobile")

	elif request.method == "POST":
		rmail = request.form['rmail']
		rmobile = request.form['rmobile']

	restadmin = Restadmin.query.filter(or_(Restadmin.rmail == rmail, Restadmin.rmobile == rmobile)).first()

	if restadmin:
		return render_template('adminhome.html', admsg="Restaurant Already Registered...!")

	else:
		newrest = Restadmin(rname=request.form["rname"], rmail=request.form["rmail"], rmobile=request.form["rmobile"], raddress=request.form["raddress"], rpassword=request.form['rpassword'])
	
		db.session.add(newrest)
		db.session.commit()
		return render_template('adminhome.html', ssmsg="Restaurant Registered Succcessfully...!")


@app.route('/adminshowrest')
def adminshowrest():
	if not session.get('amail'):
		return redirect(request.url_root)

	return render_template('adminshowrest.html',restadmin = Restadmin.query.all())


@app.route('/adminrestmenu', methods = ['GET','POST'])
def adminrestmenu():
	if not session.get('amail'):
		return redirect(request.url_root)

	if request.method == "GET":
		restid = request.args.get("restid")
	
	elif request.method == "POST":
		restid = request.form['restid']

	items = Items.query.filter(Items.rid == restid).all()
	restad = Restadmin.query.filter(Restadmin.rid == restid).first()
	return render_template('adminrestmenu.html',restad=restad, restadmin=items)	


@app.route('/adminlogout')
def adminlogout():

	session.pop('amail',None)
	return redirect(url_for('index'))	

@app.route('/about')
def about():
	return render_template('aboutus.html')


