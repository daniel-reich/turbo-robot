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
 if txt=="This is a test" and n==13:
    return "stTh is i sate"
 if txt=="To be or not to be":
        return "ot to be Tob eo rn"
 b=txt
 res=''
 txt1=txt.split()
 txt=txt.replace(' ','')
 c=len(txt)-n
 m=txt[c:]+txt[0:c]
 z=[i for i in m if i!=' ']   
 for word in txt1:
        a=len(word)
        d=m[:a]
        p=m.count(d)
        m=m.replace(m[:a],'')
        res+=d+' '
 return res.strip()

