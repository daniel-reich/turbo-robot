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

def solve(item):
    wake, duration = item
    h, m = [int(_) for _ in wake.split(':')]
    duration_h, duration_m = [int(_) for _ in duration.split(':')]
    h = (h - duration_h) % 24
    for _ in range(duration_m):
        m -= 1
        if m == -1:
            m = 59
            h -= 1
    h %= 24
    return str(h).zfill(2) + ':' + str(m).zfill(2)
        
    
def bed_time(*args):
    return [solve(item) for item in args]

