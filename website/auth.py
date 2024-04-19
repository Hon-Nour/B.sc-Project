from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Users, Biodata
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user # type: ignore

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
               flash('Logged in successful!', category='success')
               return redirect('/dashboard')
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    logout_user
    return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():   
    if request.method == 'POST':
        # Retrieve data from the form
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2') 
        role_id = 2

        user = Users.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be atleast 7 characters.', category='error') 
        else:
            new_user = Users(email=email, firstname=firstname, lastname=lastname, password=generate_password_hash(password1, method='pbkdf2:sha256'), role_id=role_id)
            db.session.add(new_user)
            db.session.commit()

            # Get the ID of the newly added user
            user_id = new_user.id

            flash('Account created!', category='success')
            return redirect(url_for("auth.biodata", user_id=user_id, role_id=role_id, email=email, firstname=firstname, lastname=lastname))
    return render_template("sign_up.html")


@auth.route('/biodata', methods=['GET', 'POST'])
def biodata():
    if request.method == 'POST':
        # Retrieve data from the form
        regno = request.form.get('regno')
        mobilenumber = request.form.get('mobilenumber')
        address = request.form.get('address')
        department = request.form.get('department')
        
        # Retrieve user ID from URL parameters
        user_id = request.args.get('user_id')
        role_id = request.args.get('role_id')
        email = request.args.get('email')
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')

        # Check if any required field is empty
        if not all([regno, mobilenumber, address, department, user_id, email, firstname, lastname]):
            flash('All fields are required.', category='error')
            return redirect(url_for("auth.biodata", user_id=user_id, role_id=role_id, email=email, firstname=firstname, lastname=lastname))
        
        if len(regno) < 11:
            flash('Incomplete Reg Number.', category='error')
        elif len(mobilenumber) < 11:
            flash('Incomplete mobile number.', category='error')
        elif len(address) < 7:
            flash('Address is required.', category='error') 
        else:
            # Create a new biodata object and add it to the database
            new_biodata = Biodata(user_id=user_id, role_id=role_id, regno=regno, firstname=firstname, lastname=lastname, email=email,
                                  mobilenumber=mobilenumber, address=address, department=department)
            db.session.add(new_biodata)
            db.session.commit()

            flash('Biodata added successfully!', category='success')
            return redirect('/dashboard')  # Redirect to the dashboard

    # If it's a GET request, render the biodata form
    user_id = request.args.get('user_id')
    role_id = request.args.get('role_id')
    email = request.args.get('email')
    firstname = request.args.get('firstname')
    lastname = request.args.get('lastname')

    return render_template('biodata.html', user_id=user_id, role_id=role_id, email=email, firstname=firstname, lastname=lastname)


@auth.route('/dashboard')
def dashboard():
    return "<p>dashboard</p>"