from flask import Blueprint,render_template,url_for,request,flash,redirect
from . import db
from .models import User
from flask_login import login_user,logout_user,current_user,login_required
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth",__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    try:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            print(password)
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password,password):
                    flash('login in',category='success')
                    login_user(user,remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('password in incorrect', category='error')

        return render_template('login.html')
    except Exception as e:
        raise(e)


@auth.route('/signup', methods=['GET','POST'])
def signup():
    try:
        if request.method == 'POST':
            firstname = request.form.get("firstname")
            lastname = request.form.get('lastname')
            birthday = request.form.get('birth')
            email = request.form.get('email')
            password =request.form.get('password')
            password2 = request.form.get('password2')
            op1 = request.form.getlist('name')
            print(op1)

            # email_exists = User.query.filter_by(email=email).first()
            # if email_exists:
            #     flash('Email is already in use',category='error')
            # elif password != password2:
            #     flash('Password don\'t match!', category='error')
            # elif len(password) < 6:
            #     flash('Password is too short.', category='error')
            # elif len(email) < 4:
            #     flash("Email is invalid.", category='error')
            # else:
            #     new_user = User(firstname=firstname,lastname=lastname,email=email,birthday=birthday,password=generate_password_hash(
            #     password, method='sha256'))
            #     db.session.add(new_user)
            #     db.session.commit()
            #     login_user(new_user,remember=True)
            #     flash('User created',category='success')
            #     return redirect(url_for('auth.login'))
            


            
        return render_template('signup.html')
    except Exception as e:
        raise e


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))