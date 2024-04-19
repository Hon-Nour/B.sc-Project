from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="./template")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "hall_allocation"
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)

@app.route("/signup", methods=["POST","GET"])
def submit_signup():
    if request.method == "POST":
        regno = request.form['reg_number']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        mobilenumber = request.form['mobile_number']
        address = request.form['address']
        department = request.form['department']
        password = request.form['password']
        role_id = 2

        # Insert data into users table
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (firstname, lastname, password, email, role_id) VALUES (%s, %s, %s, %s, %s)", (firstname, lastname, password, email, role_id))
        mysql.connection.commit()

        # Get the generated user ID (cueid)
        user_id = cur.lastrowid
    
        # Insert data into biodata table
        cur.execute("INSERT INTO biodata (user_id, role_id, regno, firstname, lastname, password, email, mobilenumber, address, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (user_id, role_id, regno, firstname, lastname, password, email, mobilenumber, address, department))
        mysql.connection.commit()
        cur.close()
        
        # Redirect to dashboard with form data as URL parameters
        return redirect(url_for('dashboard', firstname=firstname, lastname=lastname, email=email, matric_number=regno, address=address, department=department))
    else:
        return render_template("signup.html")

    
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
    
        # Check if username and password match in the database
        cur = mysql.connection.cursor()
        cur.execute("SELECT firstname FROM users WHERE email = %s AND password = %s", (email, password))
        user = cur.fetchone()
        cur.close()
    
        if user:
            # Redirect to the index route if login is successful
            return redirect(url_for("index"))
            # return f"<h1>{user}</h1>"
        else:
            return "Invalid username or password"
    else:
        return render_template("login.html")

@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        courses = zip(request.form.getlist('courseName[]'), request.form.getlist('courseDetails[]'))
        cursor = mysql.connection.cursor()
        for course_name, course_details in courses:
            sql = "INSERT INTO courses (course_name, course_details) VALUES (%s, %s)"
            val = (course_name, course_details)
            cursor.execute(sql, val)
            mysql.connection.commit()
        cursor.close()
        return "Form submitted successfully!"
    else:    
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)