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

def shift_letters(text,n):
    n = n%(len(text))
    spaces=[]
    for i in text:
        if i ==" ":
            spaces.append(text.index(i))
            text=text.replace(" ","*",1)
    # print(spaces)
    text = text.replace("*","")
    # print(text)
    l = len(text)
    n = n%(len(text))
    text = text[l-n:] + text[:l-n]
    # print(text,n,l)
    for i in spaces:
        text=text[0:i]+ " " + text[i:]
        # print(text)
    return text

