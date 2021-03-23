"""


Create a function to determine if the sum of all the individual even digits
are greater than the sum of all the indiviudal odd digits in a string of
numbers.

  * If the sum of odd numbers is greater than the sum of even numbers, return `"Odd is greater than Even"`.
  * If the sum of even numbers is greater than the odd numbers, return `"Even is greater than Odd"`.
  * If the sum of both even and odd numbers are equal, return `"Even and Odd are the same"`.

### Examples

    even_or_odd("22471") ➞ "Even and Odd are the same"
    
    even_or_odd("213613") ➞ "Even and Odd are the same"
    
    even_or_odd("23456") ➞ "Even is greater than Odd"

### Notes

The input will be a string of numbers.

"""

def even_or_odd(s):
  diff = sum(int(i) for i in s if not int(i) % 2) - sum(int(i) for i in s if int(i) % 2)
  return 'Even is greater than Odd' if diff > 0 else \
    'Odd is greater than Even' if diff < 0 else 'Even and Odd are the same'

