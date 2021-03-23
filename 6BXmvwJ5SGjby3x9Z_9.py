"""


Create a function that takes `time1` and `time2` and return how many hours
have passed between the two times.

### Examples

    hours_passed("3:00 AM", "9:00 AM") ➞ "6 hours"
    
    hours_passed("2:00 PM", "4:00 PM") ➞ "2 hours"
    
    hours_passed("1:00 AM", "3:00 PM") ➞ "14 hours"

### Notes

  * `time1` will always be the starting time and `time2` the ending time.
  * Return `"no time passed"` if `time1` is equal to `time2`.

"""

def hours_passed(time1, time2):
  def convert(time):
    lt = time.split()
    lt[0] = lt[0].replace(lt[0][-3:], '')
    for i in range(len(lt)):
      if lt[i].isdigit():
        if lt[i] == '12' and lt[i+1] == 'AM':
          lt[i] = 0
        else:
          lt[i] = int(lt[i])
      else:
        if lt[i] == 'AM':
          lt[i] = 0
        else:
          lt[i] = 12
    return lt
  tpassed = sum(convert(time2))-sum(convert(time1))
  return '{} hours'.format(tpassed) if not time1 == time2 else 'no time passed'

