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

def shift_letters(txt, n): # right
    ws = [i for i, x in enumerate(txt) if x == ' ']
    lst = [x for x in txt if x != ' ']
    lst = [(x, (i + n) % len(lst)) for i, x in enumerate(lst)]
    lst = sorted(lst, key=lambda x: x[1])
    lst = [x[0] for x in lst]
    for x in ws:
        lst.insert(x, ' ')
    return ''.join(lst)

