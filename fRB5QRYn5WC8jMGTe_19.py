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

def time_difference(a, t, b):
  t = t.replace(",","").split(" ")
  t[3] = t[3].split(":")
  mon_di = {"February": "2", "June": "6", "November": "11", "September": "9", "March": "3", "April": "4", "July": "7", "August": "8", "December": "12", "January": "1"}
  mon2_di = {"July": "August", "December": "January"}
  city_di = {"Los Angeles": ["-08","-00"], "New York":  ["-05","-00"], "Caracas": ["-04","-30"], "Buenos Aires": ["-03","-00"], "London": ["00","00"], "Rome": ["01","00"], "Moscow": ["03","00"], "Tehran": ["03","30"], "New Delhi": ["05","30"], "Beijing": ["08","00"], "Canberra": ["10", "00"]}
  t[3][0] = int(t[3][0]) - int(city_di[a][0]) + int(city_di[b][0]) 
  t[3][1] = int(t[3][1]) - int(city_di[a][1]) + int(city_di[b][1])
  if t[3][1] >= 60 : 
    t[3][0] += 1
    t[3][1] -= 60
  elif t[3][1] < 0: 
    t[3][0] -= 1
    t[3][1] += 60
  if t[3][0] >= 24 : 
    t[1] = int(t[1])+1
    t[3][0] -= 24
  elif t[3][0] < 0:
    t[1] = int(t[1])-1
    t[3][0] += 24
  if t[3][0] < 10:
    t[3][0] = "0"+str(t[3][0])
  if t[3][1] < 10:
    t[3][1] = "0"+str(t[3][1])
  if t[0] in ["July", "December"] and int(t[1]) > 31:
    if t[0] == "December":
      t[2] = int(t[2]) + 1
    t[0] = mon2_di[t[0]]
    t[1] -= 31
  return str(t[2])+"-"+mon_di[t[0]]+"-"+str(t[1])+" "+str(t[3][0])+":"+str(t[3][1])

