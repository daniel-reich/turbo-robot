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

def shift_letters(text, n):
  only_words = list(filter(lambda x : x.isalpha(), text))
  first_letter = only_words[-1]
  text = [i for i in text]
  
  for i in range(len(text)):
    if text[i] != " " and n != 0:
      text[i] = first_letter
      only_words = iter(only_words)
      first_letter = next(only_words)
      
  if n == 1 or n == 0:
    return "".join(text)
    
  return shift_letters("".join(text), n - 1)

