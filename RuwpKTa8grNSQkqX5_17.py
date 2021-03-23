"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

from decimal import *
def fractions(decimal):
  pattern = decimal.split('(')[1].split(')')[0]
  number = Decimal(decimal.split('(')[0]+pattern)
  non_rep_count = len(decimal.split('(')[0].split('.')[1]) 
  rep_count =len(pattern)
  number1 = number *10**(non_rep_count)
  number2 = number * 10**(non_rep_count+rep_count) + Decimal('0.'+pattern)
  div=gcd(int(number2-number1),(10**(non_rep_count+rep_count)-10**(non_rep_count)))
  return str(int(int(number2-number1)/div)) + \
  '/' + str(int((10**(non_rep_count+rep_count)-10**(non_rep_count))/div))
​
def gcd(n1, n2):
  while n2:
    n1, n2 = n2, n1 % n2
  return n1

