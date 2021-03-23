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

def is_correct_aliases(names, aliases):
    if len(names) != len(aliases):
        return False
    for i in range(len(names)):
        name = names[i]
        alias = aliases[i].split()
        if len(alias) != 2:
            return False
        letter = name[0].upper()
        if (not 'A' <= alias[0][0] <= 'Z') or (not 'A' <= alias[1][0] <= 'Z') or \
           alias[0][0] != letter or alias[1][0] != letter:
            return False
    return True

