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
    temptxt = [i for i in txt if i != ' ']
    [temptxt.insert(0, temptxt.pop()) for _ in range(n)]
    [temptxt.insert(i, ' ') for i in [i[0] for i in enumerate(txt) if i[1] == ' ']]
    return ''.join(temptxt)

