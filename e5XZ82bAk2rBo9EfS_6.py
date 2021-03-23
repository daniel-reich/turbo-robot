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

from datetime import timedelta, time, datetime, date
​
def bed_time(*times):
  return [go_to_sleep(*time) for time in times]
  
def go_to_sleep(alarm_time, sleep_time):
  hours, minutes = sleep_time.split(":")
  hours, minutes = int(hours), int(minutes)
  delta_time = timedelta(hours=hours, minutes=minutes)
  
  hours, minutes = alarm_time.split(":")
  hours, minutes = int(hours), int(minutes)
  alarm_time = time(hour=hours, minute=minutes)
  
  sleep_time = (datetime.combine(date(3,3,3), alarm_time) - delta_time).time()
  
  return "{:02d}:{:02d}".format(sleep_time.hour, sleep_time.minute)

