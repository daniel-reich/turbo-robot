"""


You are given a list of `dates` in the format `Dec 11` and a `month` in the
format `Dec` as arguments. Each **date** represent a **video** that was
uploaded on that day. Return the number of uploads for a given month.

### Examples

    upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept") ➞ 2
    
    upload_count(["Sept 22", "Sept 21", "Oct 15"], "Oct") ➞ 1

### Notes

If you only pay attention to the month and ignore the day, the challenge will
become easier.

"""

def upload_count(dates, month):
  count = 0
  for x in dates:
    y = x.split(' ')
    if y[0] == month:
      count += 1
  return count

