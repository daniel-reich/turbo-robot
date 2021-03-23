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

def clean_time(s):
  if s == 0:
    return '00'
  elif s < 10:
    return '0' + str(s)
  else:
    return str(s)
​
def bed_time(*times):
  ans = []
  for time in times:
    start = time[0]
    end = time[1]
    s_hour = start.split(":")[0]
    e_hour = end.split(":")[0]
    s_min = start.split(":")[1]
    e_min = end.split(":")[1]
    hour_diff = int(s_hour) - int(e_hour)
    min_diff = int(s_min) - int(e_min)
    if hour_diff < 0:
      hour_diff += 24
    if min_diff < 0:
      min_diff += 60
      hour_diff -= 1
    ans.append(clean_time(hour_diff) + ':' + clean_time(min_diff))
  return ans

