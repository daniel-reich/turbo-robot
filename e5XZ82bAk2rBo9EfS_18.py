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
​
    return_strs=[]
    for alarm,duration in times:
​
        alarm_hr= int(alarm[:2]) if alarm[0]!='0' else int(alarm[1:2])
        alarm_min=(60*alarm_hr)+ (int(alarm[3:]) if alarm[3]!='0' else int(alarm[4:]))
​
        duration_hr = int(duration[:2]) if duration[0] != '0' else int(duration[1:2])
        duration_min =(60*duration_hr)+ (int(duration[3:]) if duration[3] != '0' else int(duration[4:]))
        sleep_min=(alarm_min-duration_min)%(24*60)
​
        return_strs.append(str(sleep_min//60).zfill(2)+':'+str(sleep_min%60).zfill(2))
​
    return return_strs

