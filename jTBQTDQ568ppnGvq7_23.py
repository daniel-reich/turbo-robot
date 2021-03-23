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
  x = sorted(lst, key=lambda x: len(str(x)), reverse = True)
  while True:
    c = 0
    for i in range(len(x)-1):
      if len(str(x[i])) == len(str(x[i+1])):
        if x[i] > x[i+1]:
          x[i],x[i+1] = x[i+1], x[i]
          c += 1
    if c == 0:
      break
  return x

