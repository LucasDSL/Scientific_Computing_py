def add_timer(start_time, duration, day_week=""):
    week_days = ["Sunday", "Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday"]
    start_time = start_time.split(" ")
    # Get the hours apart from the minutes and puts in the first position
    start_time.insert(0, start_time[0].split(":"))
    # Remove the format that has ":"
    start_time.remove(start_time[1])
    # The same as above on duration
    duration = duration.split(":")
    total_minutes = int(duration[1]) + int(start_time[0][1])
    final_hour = 0
    days_later = 0
    final_minutes = 0
    # Get the beggining hour and period of time: AM or PM
    old_hour = start_time[0][0]
    old_period = start_time[1]
    ''' Calculating the final minutes in two situations: 
    first if the sum of the starting and duration numbers are bigger than 60,
    whereas there will be one your more hour and where there are not more than
    60 minutes.'''
    if  total_minutes > 60:
        final_hour += int(start_time[0][0]) + 1
        minutes_left = total_minutes - 60
        final_minutes += minutes_left
    else: 
        final_minutes += int(start_time[0][1]) + int(duration[1])
    if old_hour == "11" and old_period == "PM" and final_hour == 12:
        days_later += 1
        old_period = "AM"
    print(final_hour, final_minutes, days_later)