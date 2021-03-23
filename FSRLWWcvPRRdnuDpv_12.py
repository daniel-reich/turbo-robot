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

def time_to_eat(current_time):
​
    time = ''
    am_pm = ''
​
    if 'a.m.' in current_time:
        am_pm = 'am'
        time = current_time.replace(':', '').replace(' a.m.', '')
    else:
        am_pm = 'pm'
        time = current_time.replace(':', '').replace(' p.m.', '')
​
    h_c = int(time[:-2])
    m_c = int(time[-2:])
    if am_pm == 'am' and len(str(h_c)) == 2:
        h_c -= 12
​
    if am_pm == 'pm':
        h_c += 12
​
    times = [7, 12, 19]
    times += [h_c]
    times.sort()
    if h_c == 23:
        diff_h = times[0] + 1
    else:
        idx = times.index(h_c)
        diff_h = times[idx+1] - times[idx]
​
    diff_m = 0
    if m_c > 0:
        diff_m = 60 - m_c
        diff_h -= 1
​
    return [diff_h, diff_m]

