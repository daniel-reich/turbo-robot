"""


Given two strings, return a `string` containing only the letters shared
between the two.

### Examples

    shared_letters("house", "home") ➞ "eho"
    
    shared_letters("Micky", "mouse") ➞ "m"
    
    shared_letters("house", "villa") ➞ ""

### Notes

  * If none of the letters are shared, return an empty string.
  * The function should be **case insensitive** (e.g. comparing `A` and `a` should return `a`).
  * Sort the resulting string alphabetically before returning it.

"""

def shared_letters(a, b):
  return ''.join(sorted(set([x for x in a.lower() if x in b.lower()])))

