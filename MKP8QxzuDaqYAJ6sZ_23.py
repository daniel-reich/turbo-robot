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
    caps1 = [x[0] for x in names] 
    caps2 = []
    for y in aliases:
        a = y.split(' ')
        for i in a:
            caps2 += i[0]
    index = 0
    for x in caps1:
        if x != caps2[index] or x != caps2[index+1]:
            return False
        index += 2
    return True

