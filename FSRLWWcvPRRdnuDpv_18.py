"""


Jake is a very habitual person. He eats breakfast at 7:00 a.m. each morning,
lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

Create a function that takes in the current time as a string and determines
the duration of time before Jake's next meal. Represent this as a list with
the first and second elements representing hours and minutes, respectively.

### Examples

    time_to_eat("2:00 p.m.") ➞ [5, 0]
    // 5 hours until the next meal, dinner
    
    time_to_eat("5:50 a.m.") ➞ [1, 10]
    // 1 hour and 10 minutes until the next meal, breakfast

### Notes

N/A

"""

def convert(ct):
  timeList = str.split(ct,' ')
  h = str.split(timeList[0],':')[0]
  m = str.split(timeList[0],':')[1]
  if h == '12':
    h = '0'
  if timeList[1] == 'p.m.':
    h = int(h) + 12
  return [int(h),int(m)]
  
def time_to_eat(current_time):
  time = convert(current_time)
  ans = []
  if time[0] < 7:
    ans.append(7-time[0])
    if time[1] > 0:
      ans[0] -= 1
      ans.append(60-time[1])
    else:
      ans.append(0)
  elif 12 > time[0] >= 7:
    ans.append(12-time[0])
    if time[1] > 0:
      ans[0] -= 1
      ans.append(60-time[1])
    else:
      ans.append(0)
  elif 19 > time[0] >= 12:
    ans.append(19-time[0])
    if time[1] > 0:
      ans[0] -= 1
      ans.append(60-time[1])
    else:
      ans.append(0)
  elif time[0] >= 19:
    ans.append(24-time[0]+7)
    if time[1] > 0:
      ans[0] -= 1
      ans.append(60-time[1])
    else:
      ans.append(0)
  return ans

