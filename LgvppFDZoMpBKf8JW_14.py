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
  hours = seconds//3600
  min = seconds //60 - (hours*60)
  sec = seconds - ((hours * 60) + min)*60
  if hours >23:
    hours = '00'
  elif hours < 10:
    hours = '0'+str(hours)
  if min < 10:
    min = '0'+str(min)
  if sec < 10:
    print(sec)
    sec = '0'+str(sec)
    print(sec)
  return str(hours)+':'+str(min)+':'+str(sec)

