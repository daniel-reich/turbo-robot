"""


In this challenge, you have to find the last 15 palindromes of all numbers
starting from ten and up to a given limit, including the limit in the search.

Given an integer `limit` being the upper limit of the range of interest,
implement a function that returns the last 15 palindromes numbers lower **or
equal** to `limit` as a list sorted ascendingly.

### Examples

    generate_palindromes(151) ➞ [
      11, 22, 33, 44, 55,
      66, 77, 88, 99, 101,
      111, 121, 131, 141, 151
    ]
    
    generate_palindromes(600) ➞ [
      454, 464, 474, 484, 494,
      505, 515, 525, 535, 545,
      555, 565, 575, 585, 595
    ]
    
    generate_palindromes(999999) ➞ [
      985589, 986689, 987789, 988889, 989989,
      990099, 991199, 992299, 993399, 994499,
      995599, 996699, 997799, 998899, 999999
    ]

### Notes

N/A

"""

def is_palindrome(n):
  return str(n) == str(n)[::-1]
​
def generate_palindromes(limit):
  
  palindromes = []
  for i in range(0,limit+1):
    if is_palindrome(i):
      palindromes.append(i)
  
  return sorted(palindromes[::-1][:15])

