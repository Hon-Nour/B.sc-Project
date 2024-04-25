from datetime import time
from website.models import Time
from website import db,  create_app# type: ignore

def generate_timeslots():
    timeslots = []

    for duration in range(1, 9):
        max_hour = 18 - (duration - 1)
        for hour in range(8, max_hour):  # From 8:00 to 17:00 (inclusive)
            timeslot_start = time(hour, 0)
            timeslot_end = time(hour + duration, 0)
            timeslots.append((timeslot_start, timeslot_end, duration))

    return timeslots


def upload_timeslots():
    timeslots = generate_timeslots()
    with create_app().app_context():
        for timeslot in timeslots:
            new_time = Time(start_time=timeslot[0], end_time=timeslot[1], duration=timeslot[2])
            db.session.add(new_time)   
        db.session.commit()
    print('Timeslots uploaded successfully.')

if __name__ == '__main__':
    upload_timeslots()
