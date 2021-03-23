"""


Given a list of numbers, return whether it is possible to make the number
**7** by adding any _three different numbers_ together.

### Examples

    lucky_seven([2, 4, 3, 8, 9, 1]) ➞ True
    
    lucky_seven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ True
    
    lucky_seven([0, 0, 0, 2, 3]) ➞ False
    # You cannot repeat the same number to make 2 + 2 + 3 = 7
    
    lucky_seven([4, 3]) ➞ False
    # You need three different numbers.

### Notes

  * Tests will only include numbers.
  * Trivially, any list with a length of less than two automatically fails the test.

"""

def lucky_seven(lst):
  for i in range(len(lst)):
    for j in range(i, len(lst)):
      for z in range(j, len(lst)):
        if i != j and i != z and j != z:
          if lst[i] + lst[j] + lst[z] == 7:
            return True
  return False

