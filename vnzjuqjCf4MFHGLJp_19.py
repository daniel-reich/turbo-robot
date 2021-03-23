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
    l=len(txt)
    sp=[i for i in range(len(txt)) if txt[i]==' ']
    txt=txt.replace(' ','')
    for i in range(n):
        txt=txt[-1]+txt[:-1]
    for i in range(l):
        if i in sp:
            txt=txt[:i]+' '+txt[i:]
    return txt

