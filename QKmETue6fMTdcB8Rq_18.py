"""


Create a recursive function that takes two parameters and repeats the string
`n` number of times. The first parameter `txt` is the string to be repeated
and the second parameter is the number of times the string is to be repeated.

### Examples

    repetition("ab", 3) ➞ "ababab"
    
    repetition("kiwi", 1) ➞ "kiwi"
    
    repetition("cherry", 2) ➞ "cherrycherry"

### Notes

The second parameter of the function is positive integer.

"""

def repetition(txt, n):
  i=0
  result = ''
  while i < n:
    result+=txt
    i += 1
    
  return result

