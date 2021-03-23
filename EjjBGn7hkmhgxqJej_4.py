"""


A word nest is created by taking a starting word, and generating a new string
by placing the word _inside_ itself. This process is then repeated.

Nesting 3 times with the word "incredible":

    start  = incredible
    first  = incre|incredible|dible
    second = increin|incredible|credibledible
    third  = increinincr|incredible|ediblecredibledible

The final nest is `"increinincrincredibleediblecredibledible"` (depth = 3).

Given a _starting word_ and the _final word nest_ , return the _depth_ of the
word nest.

### Examples

    word_nest("floor", "floor") ➞ 0
    
    word_nest("code", "cocodccococodededeodeede") ➞ 5
    
    word_nest("incredible", "increinincrincredibleediblecredibledible") ➞ 3

### Notes

N/A

"""

def word_nest(word, nest):
  count = 0
  while len(nest) > len(word):
    nest = nest.replace(word, '')
    count += 1
  return count

