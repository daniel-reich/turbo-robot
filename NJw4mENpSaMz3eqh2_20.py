"""


In this challenge, you have to establish if a given number is undulating. A
number `n` is undulating when the following conditions are **all true** :

  * `n` has at least three digits.
  * `n` has exactly two different digits.
  * The two digits of `n` are alternating without repeating groups.

If we think of the first digit of an undulating number as an "A", and the
second digit as a "B", we notice a sequence of the form "ABA" that can repeat
infinite times and ends either with an "A" or with a "B", but without clusters
of "AA" or "BB" in it.

Given a positive integer `n`, implement a function that returns `True` if `n`
is an Undulating number, or `False` if it's not.

### Examples

    is_undulating(121) ➞ True
    # A = 1, B = 2
    # The sequence ABA is valid
    
    is_undulating(373737) ➞ True
    # A = 3, B = 7
    # The sequence ABABABAB is valid
    
    is_undulating(12) ➞ False
    # Less than three digits
    
    is_undulating(12122) ➞ False
    # The sequence ABABB is not valid
    
    is_undulating(85856) ➞ False
    # More than two different digits

### Notes

N/A

"""

def is_undulating(n):
 x=str(n)
 if len(x)<3:
  return False
 if len(x)%2==0:
  if x.count(x[0])!=len(x)/2 or x.count(x[1])!=len(x)/2:
   return False
 if len(x)%2==1:
  if len(x)-x.count(x[0])!=1 or len(x)-x.count(x[1])!=2:
   return False
 for i in range(len(x)):
  if i!=len(x)-1:
   if x[i]==x[i+1]:
    return False
 return True

