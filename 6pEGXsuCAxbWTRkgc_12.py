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
  solution_string = ''
  for counter in range(n):
    if counter == n - 1:
      if solution_string == '' or 'not' in solution_string[-5:]:
        solution_string += "LOVES ME"
      else:
        solution_string += "LOVES ME NOT"
    elif counter % 2 == 0:
      solution_string += 'Loves me, '
    else:
      solution_string += 'Loves me not, '
​
  return solution_string

