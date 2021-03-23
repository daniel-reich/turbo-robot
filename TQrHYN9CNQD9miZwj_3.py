"""


When importing objects from a module in Python, the syntax usually is as
follows:

    from module_name import object

Given a string of an incorrect import statement, return the fixed string. All
import statements will be the wrong way round.

### Examples

    fix_import("import object from module_name") ➞ "from module_name import object"
    
    fix_import("import randint from random") ➞ "from random import randint"
    
    fix_import("import pi from math") ➞ "from math import pi"

### Notes

All **Tests** will be valid strings.

"""

def fix_import(s):
  words = s.split()
  return ' '.join(words[2:] + words[:2])

