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

def shift_letters(s, n):
    spaces = list(t[0] for t in enumerate(s) if t[1] == ' ')
    chrs = s.replace(' ', '')
    shift = n % len(chrs)
    chrs = chrs[-shift:] + chrs[:-shift]
    chunks = [0] + [spaces[i] - i for i in range(len(spaces))] + [len(chrs)]
    return ' '.join(chrs[chunks[i]:chunks[i+1]] for i in range(len(spaces)+1))

