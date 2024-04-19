import random
from datetime import datetime, timedelta
import calendar

def filter_activities_by_duration(activity_info, timeslot, global_variable, end_date_str):
    for activity in activity_info:
        if activity_duration_fits_timeslot(activity, timeslot):
            activity_occurence = activity['occurrence_type']
            for item in global_variable:
                if item[1] == timeslot:
                    break  # Exit the loop if the item already exists
                if item[1][0] == timeslot[0] and item[1][2] > timeslot[1]:
                    break
                if item[0] == activity and item[1]== timeslot:
                    break
            else:
                if activity_occurence == 'once':
                    global_variable = schedule_once(activity, timeslot, global_variable)
                if activity_occurence == 'weekly':
                    global_variable = schedule_weekly(activity, timeslot, global_variable, end_date_str)
                if activity_occurence == 'twice weekly':
                    global_variable = schedule_twice_weekly(activity, timeslot, global_variable, end_date_str)
                if activity_occurence == 'Bi-weekly':
                    global_variable = schedule_bi_weekly(activity, timeslot, global_variable, end_date_str)
                if activity_occurence == 'monthly':
                    global_variable = schedule_monthly(activity, timeslot, global_variable, end_date_str)
    return global_variable



def activity_duration_fits_timeslot(activity, timeslot):
    # Check if the duration of the activity fits within the timeslot
    timeslot_start = timeslot[1]
    timeslot_end = timeslot[2]
    activity_duration = activity['duration']
    # timeslot_start, timeslot_end = start_end_times
    timeslot_duration = calculate_timeslot_duration(timeslot_start, timeslot_end)
    return activity_duration == timeslot_duration



def calculate_timeslot_duration(start_time, end_time):
     # Convert start and end times to datetime objects
    start_datetime = datetime.strptime(start_time, '%H:%M')
    end_datetime = datetime.strptime(end_time, '%H:%M')

    # Calculate the duration by subtracting start time from end time
    duration = end_datetime - start_datetime

    # Return the duration in hours
    return duration.total_seconds() / 3600  # Convert seconds to hours



def schedule_once(activity, timeslot, global_variable):       
    # Check if the value corresponds to any existing item in the global variable
    for item in global_variable:
        if item[0] == activity:
            break  
    else:
        # If the item doesn't exist, append it to the global variables
        global_variable.append((activity, timeslot))
    
    return global_variable



def schedule_weekly(activity, timeslot, global_variable, end_date_str):      
    # Check if the value corresponds to any existing item in the global variable
    for item in global_variable:
        if item[0] == activity:
            break  
    else:
        # Convert end dates from string to datetime objects
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        # Extract the date string from the timeslot tuple
        current_date = timeslot[0].split()[1]
    
        # Convert the date string to a datetime object
        date_datetime = datetime.strptime(current_date, '%Y-%m-%d')
        # Append the (value, timeslot) tuple to global_variable for each week until end_date is reached
        while date_datetime <= end_date:
            global_variable.append((activity, timeslot))
            date_datetime += timedelta(days=7)  # Move to the same weekday of the next week
            # Construct a new timeslot tuple with the updated date  
            timeslot = (f"{timeslot[0].split()[0]} {date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
    return global_variable




def schedule_twice_weekly(activity, timeslot, global_variable, end_date_str):
    # Check if the value corresponds to any existing item in the global variable
    for item in global_variable:
        if item[0] == activity:
            break
    else:
        # Convert end dates from string to datetime objects
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        # Extract the date string from the timeslot tuple
        current_date = timeslot[0].split()[1]
        
        # Convert the date string to a datetime object
        date_datetime = datetime.strptime(current_date, '%Y-%m-%d')\
        # Get the start and end of the week containing the given date
        start_of_week = date_datetime - timedelta(days=date_datetime.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        while date_datetime <= end_of_week:
             # Skip Sunday timeslots
            if date_datetime.weekday() == 6:
                # Move to Friday
                date_datetime -= timedelta(days=2)  
                timeslot = (f"{date_datetime.strftime('%A')} {date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
            # Check if the value and timeslot already exist in global_variable
            for item in global_variable:
                if item[1] == timeslot:
                     # Find a close alternative timeslot with the same duration that is not in global_variable
                    timeslot = alternative_scheduletwice_timeslot(timeslot, global_variable)
                    date_datetime = datetime.strptime(timeslot[0].split()[1], '%Y-%m-%d')
            new_date_datetime = date_datetime
            while new_date_datetime <= end_date:
                global_variable.append((activity, timeslot))
                new_date_datetime += timedelta(days=7)  # Move to the same weekday of the next week
                timeslot = (f"{timeslot[0].split()[0]} {new_date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
            date_datetime += timedelta(days=3)
            timeslot = (f"{date_datetime.strftime('%A')} {date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
            if date_datetime.weekday() == 6:
                # Move to Friday
                date_datetime -= timedelta(days=2)  
                timeslot = (f"{date_datetime.strftime('%A')} {date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])

    return global_variable



def schedule_bi_weekly(value, timeslot, global_variable, end_date_str):
    for item in global_variable:
        if item[0] == value:
            break  
    else:
        # Convert end dates from string to datetime objects
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        # Extract the date string from the timeslot tuple
        current_date = timeslot[0].split()[1]
    
        # Convert the date string to a datetime object
        date_datetime = datetime.strptime(current_date, '%Y-%m-%d')
        while date_datetime <= end_date:
            global_variable.append((value, timeslot))
            date_datetime += timedelta(days=14)  # Move to the same weekday of the next week
            timeslot = (f"{timeslot[0].split()[0]} {date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
    return global_variable



def alternative_scheduletwice_timeslot(timeslot, global_variable):
    global timeslots
        
    # Convert the date string to a datetime object
    week_datetime = datetime.strptime(timeslot[0], '%A %Y-%m-%d')
    # Get the start and end of the week containing the given date
    start_of_week = week_datetime - timedelta(days=week_datetime.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    available_timeslots = find_available_timeslots(timeslots, global_variable)
    for available_timeslot in available_timeslots:
        if available_timeslot[3] == timeslot[3]:
            if start_of_week <= datetime.strptime(available_timeslot[0], '%A %Y-%m-%d') <= end_of_week:
                return available_timeslot
            


def find_available_timeslots(timeslots, global_variable):
    available_timeslots = []
    for timeslot in timeslots:
        # Check if the timeslot is not in global_variable
        if all(item[1] != timeslot for item in global_variable):
            available_timeslots.append(timeslot)
    return available_timeslots



def schedule_monthly(value, timeslot, global_variable, end_date_str):
    for item in global_variable:
        if item[0] == value:
            break
    else:
        # Convert end dates from string to datetime objects
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
        # Extract the date string from the timeslot tuple
        current_date = timeslot[0].split()[1]

        # Convert the date string to a datetime object
        date_datetime = datetime.strptime(current_date, '%Y-%m-%d')
    
        # Append the (value, timeslot) tuple to global_variable for each month until end_date is reached
        while date_datetime <= end_date:
            # Skip Sunday timeslots
            if date_datetime.weekday() == 6:
                # Check if it's the end of the month
                if (date_datetime + timedelta(days=1)).month != date_datetime.month:
                    new_datetime = date_datetime - timedelta(days=2)  # Move to Friday
                    timeslot = (f"{new_datetime.strftime('%A')} {new_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
                else:
                    # Move to Monday if it's a regular Sunday
                    new_datetime = date_datetime + timedelta(days=1)
                    timeslot = (f"{new_datetime.strftime('%A')} {new_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
            # Check if the value and timeslot already exist in global_variable
            for item in global_variable:
                if item[1] == timeslot:
                     # Find a close alternative timeslot with the same duration that is not in global_variable
                    alternative_timeslot = alternative_month_timeslot(timeslot, global_variable)
                    # Append the alternative timeslot to global_variable
                    global_variable.append((value, alternative_timeslot))
            else:
                global_variable.append((value, timeslot))

        #    # Increase the datetime object by exactly one month
        #     date_datetime += relativedelta(months=1)
            
            # Move to the same day of the next month
            date_datetime = date_datetime.replace(month=date_datetime.month + 1)
            # Handle the case where the next month has fewer days
            if date_datetime.day != int(current_date.split('-')[2]):
                # Adjust the day to the last day of the next month
                date_datetime = date_datetime.replace(day=1) - timedelta(days=1)
            # Construct a new timeslot tuple with the updated date  
            timeslot = (f"{timeslot[0].split()[0]} {date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])

    return global_variable




def alternative_month_timeslot(timeslot, global_variable):
    # Get the date of the timeslot
    date = timeslot[0].split()[1]
    date_datetime = datetime.strptime(date, '%Y-%m-%d')
    # Get the year and month from the date
    year = date_datetime.year
    month = date_datetime.month
    
    # Get the total number of days in the month
    num_days_in_month = calendar.monthrange(year, month)[1]
    
    # Loop through all the days in the month
    for day in range(1, num_days_in_month + 1):
        # Construct the date string in 'YYYY-MM-DD' format
        date_str = f"{year}-{month:02d}-{day:02d}"
        
        # Convert the date string to a datetime object
        date = datetime.strptime(date_str, '%Y-%m-%d')
        timeslot = (f"{date.strftime('%A')} {date.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])

        for item in global_variable:
            if item[1] == timeslot:
                break
        else:
            # Check if the day is not Sunday
            if date.weekday() != 6:  # Sunday is represented by 6
                alternative_timeslot = timeslot
                return alternative_timeslot
            else:
                break



def list_weekdays_between_dates(start_date_str, end_date_str):
    # Convert start and end dates from string to datetime objects
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    # Initialize a list to store weekdays and their corresponding dates
    weekdays = []
    
    # Iterate through the dates from start_date to end_date
    current_date = start_date
    while current_date <= end_date:
        # Get the day of the week for the current date
        day_of_week = current_date.strftime("%A")
        
        # Check if it's a weekday (Monday to Saturday)
        if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            # Append the day of the week and the current date to the list
            weekdays.append(f"{day_of_week} {current_date.strftime('%Y-%m-%d')}")
        
        # Move to the next day
        current_date += timedelta(days=1)
    
    return weekdays

# Example usage:
start_date_str = "2024-02-01"
end_date_str = "2024-02-29"



def generate_timeslots():
    days = list_weekdays_between_dates(start_date_str, end_date_str)
    timeslots = []

    for day in days:
        for duration in range (1,9):
            max_hour = 18 - (duration - 1)
            for hour in range(8, max_hour):  # From 8:00 to 17:00 (inclusive)
                timeslot_start = f"{hour:02d}:00"
                timeslot_end = f"{hour+duration:02d}:00"
                timeslots.append((day, timeslot_start, timeslot_end, duration))

    return timeslots

# Generate timeslots
timeslots = generate_timeslots()
# start_end_times = [(timeslot[1], timeslot[2]) for timeslot in timeslots]

# Example usage:
global_variable = []


activity_info = [{'name': 'Class C', 'duration': 2, 'occurrence_type': 'weekly'},
                 {'name': 'Class A', 'duration': 1, 'occurrence_type': 'once'}, 
                 {'name': 'Class B', 'duration': 4, 'occurrence_type': 'twice weekly'},
                 {'name': 'Church', 'duration': 4, 'occurrence_type': 'Bi-weekly'},
                 {'name': 'Class D', 'duration': 3, 'occurrence_type': 'monthly'}]
# timeslot = ('Thursday 2024-02-01', '08:00', '10:00', 2)
# global_variable = []

for timeslot in timeslots:
    global_variable = filter_activities_by_duration(activity_info, timeslot, global_variable, end_date_str)

print(global_variable)
