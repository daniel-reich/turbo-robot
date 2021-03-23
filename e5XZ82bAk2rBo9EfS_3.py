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
  wakeuplist = []
  for truetimes in times:
    alarmstring = truetimes[0]
    durationstring  = truetimes[1]
    alarmlist = alarmstring.split(":")
    durationlist = durationstring.split(":")
​
    alarmhour = int(alarmlist[0])
    alarmminute = int(alarmlist[1])
    durationhour = int(durationlist[0])
    durationminute = int(durationlist[1])
​
    wakeupminute = alarmminute - durationminute
    wakeuphour = alarmhour - durationhour
​
    if wakeupminute < 0:
        wakeupminute = 60 + wakeupminute
        wakeuphour -= 1
​
    if wakeuphour < 0:
      wakeuphour = 24 + wakeuphour
​
    if wakeupminute < 10:
        wakeupminutestring = "0" + str(wakeupminute)
    else:
      wakeupminutestring = str(wakeupminute)
      
    if wakeuphour < 10:
      wakeuphourstring = "0" + str(wakeuphour)
    else:
      wakeuphourstring = str(wakeuphour)
    
    wakeuphourstring = wakeuphourstring + ":" + wakeupminutestring
    wakeuplist.append(wakeuphourstring)
​
  return wakeuplist

