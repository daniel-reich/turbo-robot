"""


Given a series of lists, with each individual list containing the **time of
the alarm set** and the **sleep duration** , return **what time to sleep**.

### Examples

    bed_time(["07:50", "07:50"]) ➞ ["00:00"]
    # The second argument means 7 hours, 50 minutes sleep duration.
    
    bed_time(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]) ➞ ["20:15", "22:00", "23:30"]
    # The second argument of each sub list means 10 hours sleep duration.
    
    bed_time(["05:45", "04:00"], ["07:10", "04:30"]) ➞ ["01:45", "02:40"]
    # Sleep duration can be different among the lists.

### Notes

  * Times should be given in 24-hrs (i.e. "23:25" as opposed to "11:25PM").
  * Return a list of strings.

"""

def bed_time(*times):
  time = []
  for i in range(len(times)):
    first_hour = get_HourMinutes(times,i , 0)[0]
    first_minutes = get_HourMinutes(times,i , 0)[1]
    second_hour = get_HourMinutes(times,i , 1)[0]
    second_minutes = get_HourMinutes(times,i , 1)[1]
    sleep_hour = (first_hour-second_hour)%24
    sleep_minutes = (first_minutes-second_minutes)%60
    if (first_minutes-second_minutes) < 0:
      sleep_hour += -1
    time_string = ""
    if sleep_hour >= 10:
      time_string = str(sleep_hour) + ":"
    else:
      time_string = "0" + str(sleep_hour) + ":"
    if sleep_minutes >= 10:
      time_string += str(sleep_minutes)
    else:
      time_string += "0" + str(sleep_minutes)
    time.append(time_string)
  return time
​
def get_HourMinutes(times, i, index_time):
  hourMinutes = []
  time = times[i]
  index = time[index_time].find(":")
  hourMinutes.append(int(time[index_time][:index]))
  hourMinutes.append(int(time[index_time][index+1:]))
  return hourMinutes

