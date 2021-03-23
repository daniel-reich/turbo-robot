"""


Create a function that takes any non-negative number as an argument and
returns it with its digits in descending order. Descending order is when you
sort from highest to lowest.

### Examples

    sort_descending(123) ➞ 321
    
    sort_descending(1254859723) ➞ 9875543221
    
    sort_descending(73065) ➞ 76530

### Notes

You can expect non-negative numbers for all test cases.

"""

def sort_decending(num):
  sol = [int(i) for i in str(num)]
  sol = sorted(sol, reverse = True)
  sol = [str(i) for i in sol]
  sol = "".join(sol)
  return int(sol)

