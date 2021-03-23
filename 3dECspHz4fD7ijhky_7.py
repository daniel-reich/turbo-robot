"""


Create a function that takes a list of integers and returns the range of
consecutive numbers separated by dash a `-` between `starting` and `ending`
numbers.

  * Separate different ranges by `,` commas.
  * A range of numbers will be considered if **three or more consecutive numbers** are found in the list (see example #1).

### Examples

    numbers_range([-6, -3, -2, -1, 0, 1, 7, 8, 9, 10, 11, 14, 15]) ➞ "-6,-3-1,7-11,14,15"
    # -6 is an alone integer.
    # -3 to 1 is a range of consecutive numbers.
    # 7 to 11 is a range of consecutive numbers.
    # 14 and 15 are consecutive numbers but cannot be considered as a range.
    
    numbers_range([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) ➞ "-3--1,2,10,15,16,18-20"
    
    numbers_range([1, 2, 3, 9, 10, 15, 16, 18, 56, 57]) ➞ "1-3,9,10,15,16,18,56,57"

### Notes

N/A

"""

class Sequence:
​
  def __init__(self, start, end):
​
    self.start = start
    self.end = end
​
    self.seq = list(range(start, end + 1))
  
  def match(self, start, lst):
​
    sindex = lst.index(start)
​
    start_seq = self.seq[self.seq.index(start):]
​
    match = []
    n = 0
​
    try:
      while lst[sindex + n] == start_seq[n]:
        match.append(start_seq[n])
        n += 1
    except IndexError:
      pass
​
    if len(match) >= 3:
      return ['{}-{}'.format(min(match), max(match)), match]
    else:
      return str(start)
​
​
def numbers_range(numbers):
​
  if len(numbers) <= 0:
    return ''
    
  seq = Sequence(min(numbers), max(numbers))
​
  matches = []
  used = []
​
  for n in range(len(numbers)):
    number = numbers[n]
    if number in used:
      pass
    else:
      matched = seq.match(number, numbers)
      if isinstance(matched, list) == False:
        matches.append(matched)
      else:
        matches.append(matched[0])
        for item in matched[1]:
          used.append(item)
  
  return ', '.join(matches)

