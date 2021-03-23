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
  List = []
  List.append(str(seconds%60))
  seconds -= seconds%60
  List.append(str(int((seconds%3600)/60)))
  seconds -= seconds%3600
  List.append(str(int((seconds/3600)%24)))
  for i in List:
    if len(i) != 2:
      List[List.index(i)] = '0'+i
  return List[2]+':'+List[1]+':'+List[0]

