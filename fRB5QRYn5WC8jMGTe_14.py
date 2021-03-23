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

import re
from datetime import datetime, timedelta
​
rx = re.compile(r'([a-z]+|\b\d{1,2}\b|\b\d{4}\b)', re.IGNORECASE)
dtformat = '%m %d %Y %H %M %z'
odtf = '{}-{}-{} {:02d}:{:02d}'
timezones = {
    'Los Angeles': '-0800', 
    'New York': '-0500',  
    'Caracas': '-0430', 
    'Buenos Aires': '-0300',  
    'London': '+0000',  
    'Rome': '+0100',  
    'Moscow': '+0300',  
    'Tehran': '+0330',  
    'New Delhi': '+0530', 
    'Beijing': '+0800', 
    'Canberra': '+1000' 
}
month = lambda s: str(('JanFebMarAprMayJunJulAugSepOctNovDec'.index(s[:3])) // 3 + 1).zfill(2)
​
def zonetime(city):
    tz = timezones[city]
    sign = -1 if tz[0] == '-' else 1
    return (sign * int(tz[1:3]), sign * int(tz[3:]))
​
def time_difference(city_a, timestamp, city_b):
    ca, cb = zonetime(city_a), zonetime(city_b)
    timediff = timedelta(hours=(cb[0] - ca[0]), minutes=(cb[1] - ca[1]))
    e = rx.findall(timestamp) + [timezones[city_a]]
    citya_datetime = datetime.strptime(month(e[0]) + ' ' + ' '.join(map(lambda s: s.zfill(2), e[1:])), dtformat)
    cityb_datetime = citya_datetime + timediff
    return odtf.format(cityb_datetime.year, cityb_datetime.month, cityb_datetime.day, cityb_datetime.hour, cityb_datetime.minute)

