"""


Create a function which returns the _total_ of all odd numbers up to and
including `n`. `n` will be given as an _odd number_.

### Examples

    add_odd_to_n(5) ➞ 9
    # 1 + 3 + 5 = 9
    
    add_odd_to_n(13) ➞ 49
    
    add_odd_to_n(47) ➞ 576

### Notes

Curiously, the answers are all _square numbers_!

"""

def add_odd_to_n(num):
  sum_lst = []
  for x in range(0, num+1):
    if x % 2 != 0:
      sum_lst.append(x)
  return sum(sum_lst)
