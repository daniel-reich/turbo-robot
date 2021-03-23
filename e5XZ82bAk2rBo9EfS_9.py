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
    a=[]
    for t in range(len(times)):
        h=int(times[t][0][:2])-int(times[t][1][:2])
        h=h+24*(h<0)
        m=int(times[t][0][3:])-int(times[t][1][3:])
        if m<0:
            h-=1
            m+=60
        a.append('0'*(h<10)+str(h)+':'+'0'*(m<10)+str(m))
    return a

