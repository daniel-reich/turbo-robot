"""


Write a function that counts the number of times a specific digit occurs in a
range ( **inclusive** ). The function will look like:

    digit_occurrences(start, end, digit) ➞ number of times digit occurs

### Examples

    digit_occurrences(51, 55, 5) ➞ 6
    # [51, 52, 53, 54, 55] : 5 occurs 6 times
    
    digit_occurrences(1, 8, 9) ➞ 0
    
    digit_occurrences(-8, -1, 8) ➞ 1
    
    digit_occurrences(71, 77, 2) ➞ 1

### Notes

  * Ranges can be negative.
  * `start <= end`

"""

def digit_occurrences(start, end, digit):
  return sum([[y for y in str(x)].count(str(digit)) for x in range(start,end+1)])

