"""


 _"Loves me, loves me not"_ is a traditional game in which a person plucks off
all the petals of a flower _one by one_ , saying the phrase _"Loves me"_ and
_"Loves me not"_ when determining whether the one that they love, loves them
back.

Given a number of petals, return a string which repeats the phrases _"Loves
me"_ and _"Loves me not"_ for every alternating petal, and return the _last
phrase_ in **all caps**. Remember to put a _comma_ and _space_ between
phrases.

### Examples

    loves_me(3) ➞ "Loves me, Loves me not, LOVES ME"
    
    loves_me(6) ➞ "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT"
    
    loves_me(1) ➞ "LOVES ME"

### Notes

  * Remember to return a _string_.
  * The first phrase is always _"Loves me"_.

"""

def loves_me(n):
    a=''
    a1='Loves me, '
    a2='Loves me not, '
    for x in range(n):
        if x%2==0:
            if x+1==n:
                a+=a1[:-2].upper()
            else:
                a+=a1
        else:
            if x+1==n:
                a+=a2[:-2].upper()
            else:
                a+=a2
    return a

