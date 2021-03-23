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
  od = sum(int(i) if i in "13579" else -int(i) for i in s)
  if not od:
    return 'Even and Odd are the same'
  if od > 0:
    return "Odd is greater than Even"
  return "Even is greater than Odd"

