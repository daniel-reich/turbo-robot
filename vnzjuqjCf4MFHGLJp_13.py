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
    lst = [len(x) for x in txt.split()]
    string = txt.replace(" ", "")
    for x in range(0, n):
        string = string[-1] + string[:-1]
​
    s = 0
    for x in lst:
        string = string[:x + s] + " " + string[x + s:]
        s += x + 1
    return string.strip(" ")

