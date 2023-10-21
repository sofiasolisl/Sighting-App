from sighting_app import app
from sighting_app.models.user import User
from sighting_app.models.sighting import Sighting
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt
from flask import flash
import datetime
bcrypt = Bcrypt(app) 

@app.route("/", methods = ['GET','POST'])
@app.route("/signup", methods = ['GET','POST'])
def signup():
    if request.method == "POST":
        if request.form['pswrd'] == request.form['pswrd_confirm']:
            data=dict(request.form)
            print("password", request.form['pswrd'])
            if request.form['pswrd'] == "" :
                flash("Input a Password")
                return redirect ('/')
            data['pswrd'] = bcrypt.generate_password_hash(request.form['pswrd'])
            if User.getAll() == None:
                data ['id']=1
            else:
                data ['id']=len(User.getAll()) + 1
            print (data)
            if User.user_validations(request.form):
                print("Super con las validaciones")
                user=User.save(data)
                session['id']=user.id
                return redirect ('/dashboard')
        else:
            flash("Password must be the same")
    return render_template('index.html')

@app.route("/signin", methods = ['GET','POST'])
def signin():
    if request.method == "POST":
        data=dict(request.form)
        db_user=User.getEmail(data.get('email'))
        print(db_user)
        if  db_user is None or not bcrypt.check_password_hash(db_user.password , data.get('pswrd')) :
            flash ("Invalid Email/Password")
            return redirect ('/')
        session["id"]=db_user.id
        return redirect ("/dashboard")
    else:
        return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    if session.get('id') == None:
        return redirect ('/')
    else:
        user = User.getId(session.get('id'))
        all_sighting=Sighting.getAll()
        all_counts_skeptics=Sighting.getAllSkepticsCount()
        sighting_id=[]
        for skeptics in all_counts_skeptics:
                sighting_id.append(skeptics.get('sighting_id'))
        print(sighting_id)
        reporters_info=Sighting.getAllReportersInfo()
        return render_template('dashboard.html', user=user, all_sighting=all_sighting, all_counts_skeptics=all_counts_skeptics, reporters_info=reporters_info, sighting_id=sighting_id)

@app.route ('/show/<int:sighting_id>')
def show(sighting_id):
    if session.get('id') == None:
        return redirect ('/')
    else:
        user = User.getId(session.get('id'))
        sighting=Sighting.getId(sighting_id)
        sighting_reporter_info=sighting.getSightingReporterInfo(sighting_id)[0]
        print(sighting_reporter_info)
        skeptics_of_sighting=Sighting.get_users_skeptical_to_sighting(sighting_id)
        print(type(skeptics_of_sighting))
        if skeptics_of_sighting == 'No users skeptical':
            skeptics_of_sighting = 0
            skeptics_id=[0]
        else:
            skeptics_of_sighting=skeptics_of_sighting.users_who_are_skeptical
            skeptics_id=[]
            for skeptics in skeptics_of_sighting:
                skeptics_id.append(skeptics.id)
        
        print("ID",skeptics_id)
        return render_template('show.html',sighting=sighting, sighting_reporter_info=sighting_reporter_info, user=user,all_skeptics=skeptics_of_sighting, skeptics_id=skeptics_id)

@app.route('/delete/<int:sighting_id>')
def delete(sighting_id):
    if session.get('id') == None:
        return redirect ('/')
    sighting=Sighting.getId(sighting_id)
    data={}
    if session.get('id') == sighting.user_reporter_id:
        data['id']=sighting.id
        data['user_reporter_id']=sighting.user_reporter_id
        Sighting.delete(data)
        return redirect ('/dashboard')
    else:
        return redirect ('/dashboard')

@app.route ('/new' , methods=['GET','POST'])
def new():
    if session.get('id') == None:
        return redirect ('/')
    if request.method == "POST":
        data=dict(request.form)
        if Sighting.validations(data):
            print('Super con sightging validations')
            if Sighting.getAll() == []:
                data ['id']=1
            else:
                data ['id']=len(Sighting.getAll())+1
            data ['user_reporter_id'] = session.get('id')
            print(data)
            Sighting.save(data)
            return redirect ('/dashboard')
        else:
            return redirect ('/dashboard')
    else:
        user = User.getId(session.get('id'))
        return render_template('new.html',user=user)

@app.route ('/edit/<int:sighting_id>' , methods=['GET','POST'])
def edit(sighting_id):
    if session.get('id') == None:
        return redirect ('/')
    if request.method == "POST":
        data=dict(request.form)
        if Sighting.validations(data):
            print('Super con sighting validations')
            data ['id']=session.get('id')
            Sighting.edit(data)
            return redirect ('/dashboard')
        else:
            return redirect ('/dashboard')
    else:
        user = User.getId(session.get('id'))
        sighting=Sighting.getId(sighting_id)
        return render_template('edit.html', sighting=sighting, user=user)

@app.route('/skeptical/<int:sighting_id>/<skeptical>')
def skeptical(sighting_id, skeptical):
    if session.get('id') == None:
        return redirect ('/')
    else:
        user_id=session.get('id')
        data={
                'user_id':user_id,
                'sighting_id':sighting_id
        }
        if skeptical == "add":
            User.skeptical_add(data)
            return redirect (f'/show/{sighting_id}')
        else:
            User.skeptical_remove(data)
            return redirect (f'/show/{sighting_id}')


@app.route("/logout")
def logout():
    if session.get('id') == None:
        return redirect ('/')
    session.clear()
    return redirect ('/')