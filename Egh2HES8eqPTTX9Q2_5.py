"""


Write a function that accepts a string and an `n` and returns a cipher by
rolling each character forward (n > 0) or backward (n < 0) `n` times.

Note: Think of the letters as a connected loop, so rolling `a` backwards once
will yield `z`, and rolling `z` forward once will yield `a`. If you roll 26
times in either direction, you should end up back where you started.

### Examples

    rolling_cipher("abcd", 1) ➞ "bcde"
    
    rolling_cipher("abcd", -1) ➞ "zabc"
    
    rolling_cipher("abcd", 3) ➞ "defg"
    
    rolling_cipher("abcd", 26) ➞ "abcd"

### Notes

  * All letters are lower cased.
  * No spacing.
  * Each character is rotated the same number of times.

"""

def rolling_cipher(txt, n):
  x=chr(ord(txt[0])+n)+chr(ord(txt[0])+n+1)+chr(ord(txt[0])+n+2)+chr(ord(txt[0])+n+3)
  for i in x:
    if ord(i)>ord('z'):
      x=x.replace(i, chr(ord(i)-26))
    if ord(i) < ord('a'):
      x = x.replace(i, chr(ord(i) + 26))
  return x

