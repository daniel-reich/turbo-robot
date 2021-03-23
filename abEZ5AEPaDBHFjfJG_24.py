"""


Create a function that takes a string and returns `True` or `False` depending
on whether or not the given formula is correct.

### Examples

    formula("6 * 4 = 24") ➞ True
    
    formula("18 / 17 = 2") ➞ False
    
    formula("") ➞ None

### Notes

  * You have to figure out what `a` is.
  * Ignore the spaces.
  * If the input is an empty string `""`, return `None`.
  * You do not need to dynamically find the value of `a` (it's a constant and the same accross all tests).

"""

def formula(txt):
  formula_chunks = txt.replace(' ', '').replace('a', '4').split('=')
  chunk_iter = iter(formula_chunks)
  first_chunk = next(chunk_iter)
  try:
    while txt:
      result = eval(first_chunk) == eval(next(chunk_iter))
      if not result: return result
    return None
  except StopIteration:
    return result

