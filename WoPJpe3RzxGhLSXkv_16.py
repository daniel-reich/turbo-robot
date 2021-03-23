"""


In this challenge you must create a program which takes a number `n` and
returns the length or number of digits in all numbers from 1 to `n`
concatenated.

### Examples

    concatenation_sum(5) ➞ 5
    
    concatenation_sum(10) ➞ 11
    
    concatenation_sum(13) ➞ 17

### Notes

Keep in mind that the output is the number of digits in the concatenated
number. For example, if the input was `5`, the output would be `5` because
`12345` has `5` digits. Similarly when the input is `13` the ouput is `17`
because `12345678910111213` has `17` digits.

"""

def rough_digit_length(goal):
  digit_length = lambda expon: ((10 ** (expon+1)) - (10 ** expon)) * (expon + 1) + digit_length(expon-1) if expon > 0 else 9
​
  dic = {10**(num+1):digit_length(num) for num in range(goal)}
​
  return dic
​
rdl = rough_digit_length(16)
​
def concatenation_sum(n):
​
  if n < min(rdl.keys()):
    return n
  else:
    closest = max([num for num in rdl.keys() if num <= n])
    digits = rdl[closest]
​
    digits += (n + 1 - closest) * len(str(n))
​
    return digits

