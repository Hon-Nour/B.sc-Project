from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from datetime import datetime, timedelta

app = Flask(__name__, template_folder="./template")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "hall_allocation"
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)

def generate_timeslots():
    timeslots = []

    for duration in range (1,11):
        max_hour = 18 - (duration - 1)
        for hour in range(8, max_hour):  # From 8:00 to 17:00 (inclusive)
            timeslot_start = f"{hour:02d}:00"
            timeslot_end = f"{hour+duration:02d}:00"
            timeslots.append((timeslot_start, timeslot_end, duration))

    return timeslots

# Generate timeslots
timeslots = generate_timeslots()

for time in timeslots:
    start_time = datetime.strptime(time[0], '%H:%M').time()
    end_time = datetime.strptime(time[1], '%H:%M').time()
    duration = time[2]
    print(start_time, end_time, duration)
    

