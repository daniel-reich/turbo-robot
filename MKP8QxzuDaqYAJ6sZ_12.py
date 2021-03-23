"""


You are in the process of creating a chat application and want to add an
**anonymous name** feature. This anonymous name feature will create an alias
that consists of two capitalized words beginning with the same letter as the
users first name.

Create a function that determines if the list of users is mapped to a list of
anonymous names correctly.

### Examples

    is_correct_aliases(["Adrian M.", "Harriet S.", "Mandy T."], ["Amazing Artichoke", "Hopeful Hedgehog", "Marvelous Mouse"]) ➞ True
    
    is_correct_aliases(["Rachel F.", "Pam G.", "Fred Z.", "Nancy K."], ["Reassuring Rat", "Peaceful Panda", "Fantastic Frog", "Notable Nickel"]) ➞ True
    
    is_correct_aliases(["Beth T."], ["Brandishing Mimosa"]) ➞ False
    # Both words in "Brandishing Mimosa" should begin with a "B" - "Brandishing Beaver" would do the trick.

### Notes

Both words in the alias should be capitalized.

"""

import re
def is_correct_aliases(names, aliases):
  return all(re.match(r'^{}\w+ {}\w+$'.format(names[i][0], names[i][0]), aliases[i]) \
    for i in range(len(names)))

