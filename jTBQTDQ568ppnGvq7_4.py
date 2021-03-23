"""


Write a function that sorts a list of integers by their digit length in
**descending order** , then settles ties by sorting numbers with the same
digit length in **ascending order**.

### Examples

    digit_sort([77, 23, 5, 7, 101])
    ➞ [101, 23, 77, 5, 7]
    
    digit_sort([1, 5, 9, 2, 789, 563, 444])
    ➞ [444, 563, 789, 1, 2, 5, 9]
    
    digit_sort([53219, 3772, 564, 32, 1])
    ➞ [53219, 3772, 564, 32, 1]

### Notes

N/A

"""

def digit_sort(lst):
  tenthou, thou, hun, ten, digi = [],[],[],[],[]
  for i in lst:
    if i < 10: digi.append(i)
    elif i < 100: ten.append(i)
    elif i < 1000: hun.append(i)
    elif i < 10000: thou.append(i)
    else: tenthou.append(i)
  return sorted(tenthou) + sorted(thou) + sorted(hun) + sorted(ten) + sorted(digi)

