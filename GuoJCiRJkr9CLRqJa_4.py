"""


Given two lists, which represent two sandwiches, return whether both
sandwiches use the same type of bread. The bread will always be found at the
start and end of the list.

### Examples

    has_same_bread(
      ["white bread", "lettuce", "white bread"],
      ["white bread", "tomato", "white bread"]
    ) ➞ True
    
    has_same_bread(
      ["brown bread", "chicken", "brown bread"],
      ["white bread", "chicken", "white bread"]
    ) ➞ False
    
    has_same_bread(
      ["toast", "cheese", "toast"],
      ["brown bread", "cheese", "toast"]
    ) ➞ False

### Notes

  * The lists will always be **three** elements long.
  * The first piece of bread on one sandwich must be the same as the first piece of bread on the other sandwich. The same goes for the last piece of bread.

"""

def has_same_bread(lst1, lst2):
  return lst1[0]==lst2[0] and lst1[-1]==lst2[-1]

