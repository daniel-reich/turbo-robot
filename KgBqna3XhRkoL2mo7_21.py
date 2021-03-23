"""


Given a string `s` consisting from digits and `#`, translate `s` to English
lowercase characters as follows:

  * Characters ("a" to "i") are represented by ("1" to "9").
  * Characters ("j" to "z") are represented by ("10#" to "26#").

### Examples

    decrypt("10#11#12") ➞ "jkab"
    
    decrypt("1326#") ➞ "acz"
    
    decrypt("25#") ➞ "y"

### Notes

N/A

"""

from string import ascii_lowercase
​
def decrypt(s):
  numbers = []
  for c in s:
    if c == "#":
      # if hash, pop the last two numbers and combine them
      num = numbers.pop() + 10 * numbers.pop()
    else:
      # otherwise, just take the number value   
      num = int(c)
    numbers.append(num)
  # convert numbers to string
  return "".join([ascii_lowercase[n-1] for n in numbers])

