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
  A=[i for i in txt if i!=' ']
  K=[i for i,v in enumerate(txt) if v==' ']
  def slipe(A,t):
    count=1
    while count<=t:
      B=list(A[-1])
      for i in A[:-1]:
        B.append(i)
      count+=1
      A=B
    return A
  C=slipe(A,n)
  for i in K:
    C.insert(i,' ')
  return ''.join(C)

