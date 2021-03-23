"""


Given a list of women and a list of men, either:

  * Return `"sizes don't match"` if the two lists have different sizes.
  * If the sizes match, return a list of pairs, with the first woman paired with the first man, second woman paired with the second man, etc.

### Examples

    zip_it(["Elise", "Mary"], ["John", "Rick"])
     ➞ [("Elise", "John"), ("Mary", "Rick")]
    
    zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh"])
     ➞ "sizes don't match"
    
    zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh", "Tim"])
     ➞ [("Ana", "Bob"), ("Amy", "Josh"), ("Lisa", "Tim")]

### Notes

Consider using the `zip()` function.

"""

def zip_it(women, men):
  
  # Establishing Length of Lists:
  Women_Items = len(women)
  Men_Items = len(men)
  
  # Using Zip Function:
  Pairs = zip(women,men)
  Couples = tuple(Pairs)
  
  # Taking Out Mismatch in Length Branch
  if (Women_Items != Men_Items):
    return "sizes don't match"
  
  # When Lists Are Same Length
  else:
    return list(Couples)

