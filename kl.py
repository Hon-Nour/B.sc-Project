import random
from datetime import datetime, timedelta
import calendar
# from dateutil.relativedelta import relativedelta


# Example usage:
global_variable = []
# def generate_timeslots():
#     days = list_weekdays_between_dates(start_date_str, end_date_str)
#     timeslots = []

#     for day in days:
#         for duration in range (1,9):
#             max_hour = 18 - (duration - 1)
#             for hour in range(8, max_hour):  # From 8:00 to 17:00 (inclusive)
#                 timeslot_start = f"{hour:02d}:00"
#                 timeslot_end = f"{hour+duration:02d}:00"
#                 timeslots.append((day, timeslot_start, timeslot_end, duration))


            
#     return timeslots

# # # Generate timeslots
# # all_timeslots = generate_timeslots()
# # for timeslot in all_timeslots:
# #     print(timeslot)

# activity_info = [
#     {'name': 'Class A', 'duration': 2},
#     {'name': 'Class B', 'duration': 3},
#     # Add more activities with durations as needed
# ]



# from datetime import datetime, timedelta

# def list_weekdays_between_dates(start_date_str, end_date_str):
#     # Convert start and end dates from string to datetime objects
#     start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
#     end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
#     # Initialize a list to store weekdays and their corresponding dates
#     weekdays = []
    
#     # Iterate through the dates from start_date to end_date
#     current_date = start_date
#     while current_date <= end_date:
#         # Get the day of the week for the current date
#         day_of_week = current_date.strftime("%A")
        
#         # Check if it's a weekday (Monday to Saturday)
#         if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
#             # Append the day of the week and the current date to the list
#             weekdays.append(f"{day_of_week} {current_date.strftime('%Y-%m-%d')}")
        
#         # Move to the next day
#         current_date += timedelta(days=1)
    
#     return weekdays

# # Example usage:
# start_date_str = "2024-02-01"
# end_date_str = "2024-02-29"
# # weekdays_between_dates = list_weekdays_between_dates(start_date_str, end_date_str)

# # # Print the weekdays and their corresponding dates
# # for weekday in weekdays_between_dates:
# #     print(weekday)

# # # Generate timeslots
# all_timeslots = generate_timeslots()
# for timeslot in all_timeslots:
#     print(timeslot)


# from datetime import datetime, timedelta
# import random

# def randomly_assign_activity(activity_info, timeslots):
#     assigned_activities = []
#     for activity in activity_info:
#         if activity['occurrence_type'] == 'weekly':
#             # Randomly choose one timeslot for weekly activities
#             timeslot = random.choice(timeslots)
#         else:
#             timeslot = random.choice(timeslots)
#         assigned_activities.append((activity, timeslot))
#     return assigned_activities

# def schedule_weekly(assigned_activities, start_date, end_date):
#     weekly_activities = []
#     for activity, timeslot in assigned_activities:
#         if activity['occurrence_type'] == 'weekly':
#             current_date = start_date
#             while current_date <= end_date:
#                 weekly_activities.append((activity, timeslot, current_date))
#                 current_date += timedelta(days=7)  # Move to the same weekday of the next week
#         else:
#             weekly_activities.append((activity, timeslot, start_date))  # Non-weekly activities scheduled once
#     return weekly_activities

# # Example usage:
# start_date = datetime(2024, 2, 1)
# end_date = datetime(2024, 2, 29)
# activity_info = [
#     {'name': 'Class A', 'occurrence_type': 'weekly'},
#     {'name': 'Class B', 'occurrence_type': 'monthly'},
#     # Add more activities with occurrence types as needed
# ]

# # Generate timeslots for each weekday (Monday to Saturday)
# timeslots = [
#     ('Monday', '08:00', '10:00'),
#     ('Monday', '10:00', '12:00'),
#     ('Tuesday', '08:00', '10:00'),
#     ('Tuesday', '10:00', '12:00'),
#     ('Wednesday', '08:00', '10:00'),
#     ('Wednesday', '10:00', '12:00'),
#     ('Thursday', '08:00', '10:00'),
#     ('Thursday', '10:00', '12:00'),
#     ('Friday', '08:00', '10:00'),
#     ('Friday', '10:00', '12:00'),
#     ('Saturday', '08:00', '10:00'),
#     ('Saturday', '10:00', '12:00')
# ]

# # Randomly assign activities to timeslots
# assigned_activities = randomly_assign_activity(activity_info, timeslots)

# # Schedule weekly activities
# weekly_activities = schedule_weekly(assigned_activities, start_date, end_date)
# print(weekly_activities)


# [
#     ({'name': 'Class A', 'duration': 2, 'occurrence_type': 'weekly'}, ('Thursday 2024-02-01', '08:00', '10:00', 2)),
#     ({'name': 'Class B', 'duration': 2, 'occurrence_type': 'weekly'}, ('Thursday 2024-02-08', '08:00', '10:00', 2))
#     # Add more activities with durations as needed
# ]

# def check_and_append(value_list, timeslot):
#     global global_variable
    
#     # Check if any item in the value list corresponds to any existing item in the global variable
#     for value in value_list:
#         for item in global_variable:
#             if item[0] == value or item[1] == timeslot:
#                 break  # Exit the loop if the item already exists
#         else:
#             # If the item doesn't exist, append it to the global variable
#             global_variable.append((value, timeslot))
    
#     return global_variable



# def check_and_append(value, timeslot, global_variable):
#     timeslot_start = timeslot[1]
#     timeslot_end = timeslot[2]
        
#     # Convert timeslot start and end times to datetime objects
#     start_datetime = datetime.strptime(timeslot_start, '%H:%M')
#     end_datetime = datetime.strptime(timeslot_end, '%H:%M')
        
#     # Check if the value corresponds to any existing item in the global variable
#     for item in global_variable:
#         global_start = item[1][1]
#         global_end = item[1][2]
        
#         # Convert timeslot start and end times to datetime objects
#         global_start_datetime = datetime.strptime(global_start, '%H:%M')
#         global_end_datetime = datetime.strptime(global_end, '%H:%M')
#         if item[0] == value or item[1] == timeslot:
#             break  # Exit the loop if the item already exists
#         if global_end_datetime > start_datetime:
#             break
    
#     else:
#         # If the item doesn't exist, append it to the global variable
#         global_variable.append((value, timeslot))
    
#     return global_variable



def check_and_append(value, timeslot, global_variable):       
    # Check if the value corresponds to any existing item in the global variable
    for item in global_variable:
        if item[0] == value:
            break  
    else:
        # If the item doesn't exist, append it to the global variables
        global_variable.append((value, timeslot))
    
    return global_variable

def schedule_weekly(value, timeslot, global_variable, end_date_str):
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
            date_datetime += timedelta(days=7)  # Move to the same weekday of the next week
            timeslot = (f"{timeslot[0].split()[0]} {date_datetime.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
    return global_variable



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


# Example usage:
start_date_str = "2024-02-01"
end_date_str = "2024-03-29"



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

            # # If the duration is 2 hours, add the next consecutive timeslot
            # if hour != 17:  # Check if it's not the last hour of the day
            #     timeslot_start_next = f"{hour:02d}:00"
            #     timeslot_end_next = f"{hour+2:02d}:00"
            #     timeslots.append((day, timeslot_start_next, timeslot_end_next))

    return timeslots

# Generate timeslots
timeslots = generate_timeslots()
# start_end_times = [(timeslot[1], timeslot[2]) for timeslot in timeslots]




value_list = [{'name': 'Class C', 'duration': 2, 'occurrence_type': 'weekly'},
              {'name': 'Class A', 'duration': 1, 'occurrence_type': 'once'}, 
              {'name': 'Class B', 'duration': 4, 'occurrence_type': 'twice weekly'},   
              {'name': 'Class D', 'duration': 3, 'occurrence_type': 'monthly'}]
# timeslot = ('Thursday 2024-02-01', '08:00', '10:00', 2)
# global_variable = []

def filter_activities_by_duration(activity_info, timeslot, global_variable, end_date_str):
    for activity in activity_info:
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
                global_variable = check_and_append(activity, timeslot, global_variable)
            if activity_occurence == 'weekly':
                global_variable = schedule_weekly(activity, timeslot, global_variable, end_date_str)
            if activity_occurence == 'twice weekly':
                global_variable = schedule_twice_weekly(activity, timeslot, global_variable, end_date_str)
            if activity_occurence == 'monthly':
                global_variable = schedule_monthly(activity, timeslot, global_variable, end_date_str)
    return global_variable

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
    
    
#     # Parse the date string from the timeslot tuple
#     date_str = timeslot[0].split()[1]
    
#     # Convert the date string to a datetime object
#     date_datetime = datetime.strptime(date_str, '%Y-%m-%d')
    
#     # Add 7 days to the date
#     new_date = date_datetime + timedelta(days=7)
    
#     # Construct a new timeslot tuple with the updated date
#     new_timeslot = (f"{timeslot[0].split()[0]} {new_date.strftime('%Y-%m-%d')}", timeslot[1], timeslot[2], timeslot[3])
    
#     return new_timeslot


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




def find_available_timeslots(timeslots, global_variable):
    available_timeslots = []
    for timeslot in timeslots:
        # Check if the timeslot is not in global_variable
        if all(item[1] != timeslot for item in global_variable):
            available_timeslots.append(timeslot)
    return available_timeslots

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
            
    # for item in global_variable:
    #     # Check if the timeslot is not in global_variable
    #     if item[1] != timeslot:
    #         available_timeslots = timeslot
    #         return available_timeslots
    #     else:
    #         break

# Assuming timeslots is a list of timeslots
available_timeslots = find_available_timeslots(timeslots, global_variable)

# print(available_timeslots)
# timmy = []
# for timeslot in timeslots:
#     love = alternative_scheduletwice_timeslot(timeslot, global_variable)
#     timmy.append(love)
# print(timmy)

# for timeslot in timeslots:
#     global_variable = filter_activities_by_duration(value_list, timeslot, global_variable, end_date_str)
# #     available_timeslots = find_available_timeslots(timeslot, global_variable)
# # print(available_timeslots)
# print(global_variable)

# for timeslot in timeslots:
#     print(timeslot)
#     for value in value_list:
#         yumm = schedule_monthly(value, timeslot, global_variable, end_date_str)

# print(yumm)

timeslot = ('Thursday 2024-02-01', '08:00', '09:00', 1)
activity = [{'name': 'Class B', 'duration': 4, 'occurrence_type': 'twice weekly'}]
global_variable = schedule_bi_weekly(activity, timeslot, global_variable, end_date_str)
print(global_variable)
# for value in value_list:
#     yumm = schedule_monthly(value, timeslot, global_variable, end_date_str)

# print(yumm)
            
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# # Assuming current_date is a string in the format '%Y-%m-%d'
# current_date = '2024-03-31'

# # Convert the string to a datetime object
# date_datetime = datetime.strptime(current_date, '%Y-%m-%d')

# # Increase the datetime object by exactly one month
# date_datetime += relativedelta(months=1)

# # Convert it back to a string if needed
# new_date = date_datetime.strftime('%Y-%m-%d')

# print(new_date)  # Output will be the date increased by one month


# for timeslot in timeslots:

#     # Extract the date string from the timeslot tuple
#     date_string = timeslot[0].split()[1]

#     # Convert the date string to a datetime object
#     date_datetime = datetime.strptime(date_string, '%Y-%m-%d')

#     current_date = date_datetime + timedelta(days=7)

#     print(date_datetime, current_date)  # Output: 2024-02-01 00:00:00

# from datetime import datetime

# def check_timeslot_validity(timeslots):
#     for timeslot in timeslots:
#         timeslot_start = timeslot[1]
#         timeslot_end = timeslot[2]
        
#         # Convert timeslot start and end times to datetime objects
#         start_datetime = datetime.strptime(timeslot_start, '%H:%M')
#         end_datetime = datetime.strptime(timeslot_end, '%H:%M')
        
#         # Check if timeslot_start is less than timeslot_end
#         if start_datetime >= end_datetime:
#             print(f"Invalid timeslot: {timeslot}")
#         else:
#             print(f"Valid timeslot: {timeslot}")


# check_timeslot_validity(timeslots)
