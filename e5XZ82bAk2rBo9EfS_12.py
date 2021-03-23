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
    lst = []
    for i in range(len(times)) :
        hrs = (24+int(times[i][0].split(':')[0])-int(times[i][1].split(':')[0])+(-1 if int(times[i][0].split(':')[1])<int(times[i][1].split(':')[1]) else 0))%24
        hrs = '0'*(2-len(str(hrs))) + str(hrs)
        min = (60+int(times[i][0].split(':')[1])-int(times[i][1].split(':')[1]))%60
        min = '0'*(2-len(str(min))) + str(min)
        lst.append(hrs+':'+min)
    return lst

