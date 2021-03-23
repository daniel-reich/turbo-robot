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

def shift_letters(txt,num):
 space= [n for n,i in enumerate(txt) if i==" "]
 newstring= [i for n,i in enumerate(txt)]
​
 while num!=0:
  if newstring[-1]==" ":
      num=num+1
  newstring.insert(0,newstring[-1])
  newstring.pop(-1)
  num=num-1
 newstring= [i for i in newstring if i!=" "]
​
 for n in space:
      newstring[n:n]=" "
 return "".join(newstring)

