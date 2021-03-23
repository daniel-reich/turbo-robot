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
  hours = seconds // 3600
  minutes = (seconds - hours * 60 * 60) // 60
  seconds = int(seconds - (hours * 60 * 60 + minutes * 60))
  return '{:0>2}:{:0>2}:{:0>2}'.format(
    hours % 24,
    minutes % 60,
    seconds % 60
  )

