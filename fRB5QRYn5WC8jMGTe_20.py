"""


In this challenge, the goal is to calculate what time it is in two different
cities. You're given a string `city_a` and the related string `timestamp`
(time in `city_a`) with the date formatted in full **U.S. notation** , as in
this example:

    "July 21, 1983 23:01"

You have to return a new timestamp with date and corresponding time in
`city_b`, formatted as in this example:

    "1983-7-22 23:01"

See the table below for a list of given cities and their **GMT** ( _Greenwich
Mean Time_ ) hours offsets.

GMT| City  
---|---  
\- 08:00| Los Angeles  
\- 05:00| New York  
\- 04:30| Caracas  
\- 03:00| Buenos Aires  
00:00| London  
\+ 01:00| Rome  
\+ 03:00| Moscow  
\+ 03:30| Tehran  
\+ 05:30| New Delhi  
\+ 08:00| Beijing  
\+ 10:00| Canberra  
  
### Examples

    time_difference("Los Angeles", "April 1, 2011 23:23", "Canberra") ➞ "2011-4-2 17:23"
    # Can be a new day.
    
    time_difference("London", "July 31, 1983 23:01", "Rome") ➞ "1983-8-1 00:01"
    # Can be a new month.
    
    time_difference("New York", "December 31, 1970 13:40", "Beijing") ➞ "1971-1-1 02:40"
    # Can be a new year.

### Notes

  * Pay attention to hours and minutes, a leading `0` is needed in the returned timestamp when they're a single digit.
  * Pay attention to cities with half hours offsets.

"""

import calendar
import math
​
def months_number(month, year):
    for month_index in range(1,13):
        if month_index == 1:
            month_index_before = 12
        else:
            month_index_before = month_index - 1
        if month_index == 12:
            month_index_after = 1
        else:
            month_index_after = month_index + 1
        if month == calendar.month_name[month_index]:
            month_number = month_index
            last_day = calendar.monthrange(int(year), month_index)[1]
            last_day_month_before = calendar.monthrange(int(year), (month_index_before))[1]
            last_day_month_after = calendar.monthrange(int(year), (month_index_after))[1]
    print('Index of the month is %d and it has %d days.' % (month_number, last_day))
    return (month_number, last_day, last_day_month_before, last_day_month_after)
​
def time_to_minutes(time_1):
    time_1_hours_and_minutes = time_1.split(':')
    if int(time_1_hours_and_minutes[0]) < 0:
        time_1_time = -(abs(int(time_1_hours_and_minutes[0]) * 60) + (int(time_1_hours_and_minutes[1])))
    elif (time_1_hours_and_minutes[0] == '-00'):
        time_1_time = -(abs(int(time_1_hours_and_minutes[0]) * 60) + (int(time_1_hours_and_minutes[1])))
    else:
        time_1_time = (int(time_1_hours_and_minutes[0]) * 60) + (int(time_1_hours_and_minutes[1]))
    return time_1_time
​
def minutes_to_time(minutes):
    if minutes > 0:
        time_hours = math.floor(minutes / 60)
        time_minutes = minutes % 60
    elif minutes < 0:
        minutes = abs(minutes)
        time_hours = -(math.floor(minutes / 60))
        time_minutes = minutes % 60
        if time_hours == 0:
            print('do?')
            time_hours = '-00'
    else:
        return ('Input error.')
    time_hours = str(time_hours)
    time_minutes = str(time_minutes)
    if len(time_hours) < 2:
        time_hours = '0' + time_hours
    if len(time_minutes) < 2:
        time_minutes = '0' + time_minutes
    result = '%s:%s' % (time_hours, time_minutes)
    return (result)
​
def sum_sub_time(time_1, time_2, operation):
    time_1_time = time_to_minutes(time_1)
    time_2_time = time_to_minutes(time_2)
    if operation == 'addition':
        time = time_2_time + time_1_time
    elif operation == 'subtraction':
        time = time_2_time - time_1_time
    else:
        return ('Input error.')
    print ('Time is %d' % time)
    result = minutes_to_time(time)
    if operation == 'addition':
        print ('The summation of time is %s.' % result)
    elif operation == 'subtraction':
        print ('The difference of time is %s.' % result)
    else:
        return ('Input error.')
​
    return (result)
​
def time_difference_between_cities(city_a, city_b):
    gmt_dict = {'Los Angeles' : '-08:00', 'New York' : '-05:00',
                'Caracas' : '-04:30', 'Buenos Aires' : '-03:00', 'London' : '00:00',
                'Rome' : '01:00', 'Moscow' : '03:00', 'Tehran' : '03:30', 'New Delhi' : '05:30',
                'Beijing' : '08:00', 'Canberra' : '10:00'}
    result = sum_sub_time(gmt_dict[city_a], gmt_dict[city_b], 'subtraction')
    return (result)
​
def time_difference(city_a, timestamp, city_b):
    timestamp_clean = timestamp.replace(',','')
    list_timestamp = timestamp_clean.split(' ')
    month_index = months_number(list_timestamp[0], list_timestamp[2])
    list_timestamp[0] = month_index[0]
    max_day = month_index[1]
    max_day_month_before = month_index[2]
    max_day_month_after = month_index[3]
    time_now = sum_sub_time(list_timestamp[3], time_difference_between_cities(city_a, city_b), 'addition')
    print ('The time now is %s' % (time_now))
    time_now = time_to_minutes(time_now)
    list_timestamp[3] = time_now
    print ('The time now is %s' % (time_now))
    for i in range(len(list_timestamp)):
        print (list_timestamp[i])
        list_timestamp[i] = int(list_timestamp[i])
    if time_now > (24 * 60):
        time_now = time_now - (24 * 60)
        list_timestamp[3] = time_now
        list_timestamp[1] = list_timestamp[1] + 1
    elif time_now < 0:
        time_now = time_now + (24 * 60)
        list_timestamp[3] = time_now
        list_timestamp[1] = list_timestamp[1] - 1
    print(list_timestamp)
    if (list_timestamp[1] == 0):
        list_timestamp[0] = list_timestamp[0] - 1
        if list_timestamp[0] == 0:
            list_timestamp[0] = 12
            list_timestamp[2] = list_timestamp[2] - 1
        list_timestamp[1] = max_day_month_before
    elif (list_timestamp[1])== max_day + 1:
        list_timestamp[0] = list_timestamp[0] + 1
        if list_timestamp[0] == 13:
            list_timestamp[0] = 1
            list_timestamp[2] = list_timestamp[2] + 1
        list_timestamp[1] = 1
    print(list_timestamp)
    list_timestamp[3] = minutes_to_time(list_timestamp[3])
    print(list_timestamp)
    for i in range(len(list_timestamp)):
        print (list_timestamp[i])
        list_timestamp[i] = str(list_timestamp[i])
    result = list_timestamp[2] + '-' + list_timestamp[0] + '-' + list_timestamp[1] + ' ' + list_timestamp[3]
    print (result)
    return (result)

