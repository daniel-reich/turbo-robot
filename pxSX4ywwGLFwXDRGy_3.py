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
  return list(i for i in names if i not in enemies)

