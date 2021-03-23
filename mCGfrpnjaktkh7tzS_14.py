"""


In this challenge you will be given a relation between two numbers, _written
as a string_. Write a function that determines if the relation is `True` or
`False`.

### Examples

    is_it_true("2=2") ➞ True
    
    is_it_true("8<7") ➞ False
    
    is_it_true("5=13") ➞ False
    
    is_it_true("15>4") ➞ True

### Notes

  * Tests will only have three types of relations: `=`, `>`, and `<`
  * Many approaches work here, but the `eval()` function is particularly useful!

"""

def is_it_true(relation):
  return bool(eval(relation.replace('=', '==')))

