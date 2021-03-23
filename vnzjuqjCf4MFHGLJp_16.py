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

def shift_letters(string, n):                 # Letter shifting
  """ Return the string with all letter shifted to the right n times """
  index, string, new_str = [i for i, x in enumerate(string) if x==" "], [x for x in string if x.isalpha()], []
  n %= len(string)
  new_str = [string[i] for i in range(-n, len(string)-n)]
  for i in index: new_str.insert(i," ")
  return "".join(new_str)

