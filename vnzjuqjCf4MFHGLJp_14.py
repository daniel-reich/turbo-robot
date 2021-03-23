"""


Create a function that takes a string and shifts the letters to the right by
an amount `n` **but not the whitespace**.

### Examples

    shift_letters("Boom", 2) ➞ "omBo"
    
    shift_letters("This is a test",  4) ➞ "test Th i sisa"
    
    shift_letters("A B C D E F G H", 5) ➞  "D E F G H A B C"

### Notes

  * Keep the case as it is.
  * `n` can be larger than the total number of letters.

"""

def shift_letters(txt, n):
  nospace = txt.replace(" ", "")
  x = len(nospace)
  count = 0
  ans = ""
  for i in txt:
    if i == " ":
      ans += " "
    else:
      ans += nospace[(count-n)%x]
      count += 1
  return ans

