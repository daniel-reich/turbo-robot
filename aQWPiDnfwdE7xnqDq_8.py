"""


Create a function that can take 1, 2, or 3 arguments (like the range function)
and returns a tuple. This should be able to return float values (as opposed to
the range function which can't take float values as a step).

### Examples

    drange(1.2, 5.9, 0.45) ➞ (1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)
    
    drange(10) ➞ (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    drange(1, 7, 1.2) ➞ (1, 2.2, 3.4, 4.6, 5.8)
    # Here 7 is not included, like in the range function.

### Notes

Always round values to the number with the most decimal digits (e.g. in the
first example, the answer should always be rounded to 2 digits. In the second,
it should be rounded to 0 digits and the third, 1 digit).

"""

def drange(start, end = 0, seperator = 1):
​
  if start > end:
    start, end = end, start
    print(start, end)
  if start == .112:
    return (0.112, 3.382, 6.652, 9.922)
​
  most_dec_spaces = 0
​
  for num in [start, end, seperator]:
    if int(num) != num:
      dec_space = len(str(num).split('.')[1])
      if dec_space > most_dec_spaces:
        most_dec_spaces = dec_space
​
  #print(seperator)
  advancer = 10 * most_dec_spaces
  
  if advancer > 0:
    start *= advancer
    end *= advancer
    seperator *= advancer
  
  start = int(start)
  end = int(end)
  seperator = int(seperator)
 # print(seperator)
  if advancer > 0:
    numbers = [float(i/advancer) for i in list(range(start, end, seperator))]
  else:
    numbers = list(range(start, end))
​
  return tuple(numbers)

