"""


Python has a beautiful built-in function `sorted` that sorts an iterable,
usually an array of numbers, sorting them in ascending order, but using `key=`
you can sort the iterable in different ways.

Create a function that takes an array of integers as an argument and returns
the same array in ascending order. Using `sorted()` would be easy, but for
this challenge YOU have to sort the array creating your own algorithm.

### Examples

    sort_array([2, -5, 1, 4, 7, 8]) ➞ [-5, 1, 2, 4, 7, 8]
    
    sort_array([23, 15, 34, 17, -28]) ➞ [-28, 15, 17, 23, 34]
    
    sort_array([38, 57, 45, 18, 47, 39]) ➞ [18, 38, 39, 45, 47, 57]

### Notes

  * The arrays can contain either positive or negative elements.
  * The arrays will only contain integers.
  * The arrays won't contain duplicate numbers.
  * This is a challenge to enhance your ability, using the sorted built-in won't enhance your skills.

"""

def sort_array(lst):
  ans = []
  while lst:
    m = lst[0]
    for x in lst:
      if x < m:
        m = x
    ans.append(m)
    lst.remove(m)
  return ans

