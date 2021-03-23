"""


Write a function that takes the number of `seconds` and returns the digital
format clock time as a string. Time should be counted from `00:00:00`.

### Examples

    digital_clock(5025) ➞ "01:23:45"
    # 5025 seconds is 1 hour, 23 mins, 45 secs.
    
    digital_clock(61201) ➞ "17:00:01"
    # No AM/PM. 24h format.
    
    digital_clock(87000) ➞ "00:10:00"
    # It's 00:10 next day.

### Notes

`seconds` is always greater than or equal to 0.

"""

def digital_clock(seconds):
  hours, left = divmod(seconds, 3600)
  
  while hours >= 24:
    hours = hours - 24
  if left > 0:
    minutes, left = divmod(left, 60)
    if left > 0:
      return "{hh:02}:{mm:02}:{ss:02}".format(hh=hours, mm = minutes, ss = left)
    else:
      return "{hh:02}:{mm:02}:00".format(hh=hours, mm = minutes)
  else:
    return "{hh:02}:00:00".format(hh=hours)

