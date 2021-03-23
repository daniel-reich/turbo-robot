"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive** numbers (regardless
of orientation: whether **ascending** or **descending** ), otherwise, return
`False`.

### Examples

    is_consecutive("121314151617") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 12, 13, 14, 15, 16, 17
    
    is_consecutive("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_consecutive("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_consecutive("326325324323") ➞ True
    # Contains a set of consecutive descending numbers
    # if grouped into 3's : 326, 325, 324, 323
    
    is_consecutive("667666") ➞ True
    # Consecutive descending numbers: 667 and 666.
    
    is_consecutive("999897959493") ➞ False

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent** to each other, and the string has **at least two** of them.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/Ym27MyQQMRWGvEGeP).

"""

def is_consecutive(s):
  return any([all([num - decoupe(s,p)[i+1] == 1 for i, num in enumerate(decoupe(s,p)[:-1])]) or 
        all([num - decoupe(s,p)[i+1] == -1 for i, num in enumerate(decoupe(s,p)[:-1])])
         for p in range(1,len(s)//2+1)])
​
def decoupe(string,p):
  if len(string)%p == 0:
    return [int(string[p*i:p*(i+1)]) for i in range(len(string)//p)]
  else:
    return [1,3]

