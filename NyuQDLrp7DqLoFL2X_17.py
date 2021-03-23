"""


Google's logo can be stretched depending on how many pages it lets you skip
forward to.

![Image of Goooooooooogle](https://edabit-
challenges.s3.amazonaws.com/Google.png)

Let's say we wanted to _change_ the number of pages that Google could skip to.
Create a function where given a _number of pages_ `n`, return the word
"Google" but with the correct number of "o"s.

### Examples

    googlify(10) ➞ "Goooooooooogle"
    
    googlify(23) ➞ "Gooooooooooooooooooooooogle"
    
    googlify(2) ➞ "Google"
    
    googlify(-2) ➞ "invalid"

### Notes

If `n` is _equal to_ or _less than_ **1** , return `invalid`.

"""

def googlify(n):
  if n > 1:
    return "G" + ("o" * n) + "gle"
  else:
    return 'invalid'

