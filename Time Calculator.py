def add_time(start, duration, day=None):
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Split the start time into components
    start_parts = start.split(" ")
    time_value = start_parts[0]
    period = start_parts[1]
    hours, minutes = map(int, time_value.split(":"))
    
    # Split the duration into hours and minutes
    add_hours, add_minutes = map(int, duration.split(":"))
    
    # Add the minutes and handle overflow
    new_m = minutes + add_minutes
    if new_m >= 60:
        add_hours += new_m // 60
        new_m %= 60
    
    # Add the hours and handle AM/PM and days overflow
    new_h = hours + add_hours
    periods_to_add = (new_h // 12) % 2
    total_days = (new_h // 24) + (period == 'PM' and periods_to_add > 0)
    
    new_h %= 12
    if new_h == 0:
        new_h = 12
    
    # Switch AM/PM for each 12 hours passed
    if periods_to_add > 0:
        period = 'PM' if period == 'AM' else 'AM'
    
    if total_days == 1 and period == 'AM' and new_h == 12:
        period = 'PM'
    
    if total_days >= 1:
        if total_days == 1:
            out = " (next day)"
        else:
            out = f" ({total_days} days later)"
    else:
        out = ""
    
    # Handle the optional day parameter
    if day:
        day = day.capitalize()
        day_index = days_list.index(day)
        new_day_index = (day_index + total_days) % 7
        new_d = days_list[new_day_index]
        new_time = f"{new_h}:{str(new_m).zfill(2)} {period}, {new_d}{out}"
    else:
        new_time = f"{new_h}:{str(new_m).zfill(2)} {period}{out}"
    
    return new_time

# Example usage:
print(add_time('8:16 PM', '466:02', 'tuesday'))