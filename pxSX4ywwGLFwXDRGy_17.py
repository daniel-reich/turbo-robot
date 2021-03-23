"""


Remove enemies from the list of people, even if the enemy shows up twice.

### Examples

    remove_enemies(["Fred"], []) ➞ ["Fred"]
    
    remove_enemies(["Adam", "Emmy", "Tanya", "Emmy"], ["Emmy"]) ➞ ["Adam", "Tanya"]
    
    remove_enemies(["John", "Emily", "Steve", "Sam"], ["Sam", "John"]) ➞ ["Emily", "Steve"]

### Notes

All names to be removed will be in the enemies list; simply return the list,
no fancy strings.

"""

def remove_enemies(names, enemies):
  while True:
    if not enemies:
      return names
    for name in enemies:
      if not names.count(name):
        flag = True
      else:
        flag = False
        names.remove(name)
    if flag:
      return names

