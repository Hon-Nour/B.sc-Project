from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="./template")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "hall_allocation"
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)

@app.route("/", methods=["POST", "GET"])
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