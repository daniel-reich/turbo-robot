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

from collections import deque
​
​
def shift_letters(txt, n):
    li = deque([a for a in txt if a != ' '])
    listOfSpaces = get_index(list(txt))
    li.rotate(n)
    li = list(li)
    for a in listOfSpaces:
        li.insert(a, ' ')
    return ''.join(li)
​
​
def get_index(lst):
    res = []
    position = 0
    while True:
        try:
            position = lst.index(' ', position)
            res.append(position)
            position += 1
        except ValueError:
            break
    return res

