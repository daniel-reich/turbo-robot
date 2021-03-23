"""


Create a function which makes the last character of a string repeat `n` number
of times.

### Examples

    modify_last("Hello", 3) ➞ "Hellooo"
    
    modify_last("hey", 6) ➞ "heyyyyyy"
    
    modify_last("excuse me what?", 5) ➞ "excuse me what?????"

### Notes

  * Test will include numbers and punctuation.
  * Make sure the code is not case sensitive.

"""

def modify_last(txt, n):
  return txt + txt[-1]*(n-1)

