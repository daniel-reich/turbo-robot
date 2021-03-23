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
    new, c = "", 0
    sent =  "".join(txt.split())
    sent = sent[-n%len(sent):] + sent[:-n%(len(sent))]
    for i in txt:
        if i == " ": new += " "
        else: new += sent[c]; c += 1
    return new

