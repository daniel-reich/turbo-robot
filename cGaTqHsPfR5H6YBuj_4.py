"""


Given a list of ingredients `i` and a flavour `f` as input, create a function
that returns the list, but with the elements `bread` around the selected
ingredient.

### Examples

    make_sandwich(["tuna", "ham", "tomato"], "ham") ➞ ["tuna", "bread", "ham", "bread", "tomato"]
    
    make_sandwich(["cheese", "lettuce"], "cheese") ➞ ["bread", "cheese", "bread", "lettuce"]
    
    make_sandwich(["ham", "ham"], "ham") ➞ ["bread", "ham", "bread", "bread", "ham", "bread"]

### Notes

  * You will always get valid inputs.
  * Make two separate sandwiches if two of the same elements are next to each other (see example #3).

"""

b="bread"
make_sandwich=lambda l,f:sum([[[e],[b,e,b]][e==f]for e in l],[])

