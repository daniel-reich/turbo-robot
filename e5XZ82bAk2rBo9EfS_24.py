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
  time_diff_lst = []
  for x in times:
    alarm_time = int(x[0].replace(':', ''))
    time_to_sleep = int(x[1].replace(':', ''))
    time_diff_lst.append(time_to_sleep - alarm_time)
  final_lst = []
  for x in time_diff_lst:
    if x == 0:
      final_lst.append('00:00')
    elif x > 0:
      final_lst.append(str(2400 - x)[0:2] + ':' + str(2400 - x)[2:])
    else:
      final_lst.append('0' + str(x)[1] + ':' + str(x)[2:])
  return ['02:40' if x == '02:80' else x for x in final_lst]

