"""


For this challenge, the input will be a (long) string.

A word encountered for the first time is a stranger. A word encountered thrice
becomes an acquaintance. A word encountered 5 times becomes a friend.

Create a function that takes the string and returns a list of two lists. The
first is a list of acquaintances in the order they became an acquaintance (see
example). The second is a list of friends in the order they became a friend.
Words on the friend list should no longer be on the acquaintance list.

### Examples

    no_strangers("See Spot run. See Spot jump. Spot likes jumping. See Spot fly.")
    ➞ [["spot", "see"], []]
    # "see" was encountered first, but "spot" became an acquaintance earlier.

### Notes

  * All words should be in lowercase.
  * Punctuation should be stripped except for apostrophes (e.g. doesn't, aren't, etc).

"""

def no_strangers(text):
    '''
    Analyses text and returns 2 lists: acquaintances for words which occur 3 to
    4 times, friends for those which occur 5+ times. Words are ordered by the
    order in which words first become acquaintances or friends.
    '''
    import re
​
    def rank(words, min_val, max_val, idx):
        '''
        Returns a list containing the words in words whose frequency lie
        between min_val and max_val, sorted by the position at idx.
        '''
        selected = {word: [] for word in words if min_val <= words.count(word) <= max_val}
        for i, word in enumerate(words):
            if word in selected:
                selected[word].append(i)  # store locations of selected words
​
        return sorted((word for word in selected), key=lambda x: selected[x][idx]) 
​
    words = [word.lower() for word in re.split("[^A-Za-z0-9']+", text)]
    words = [word for word in words if word != '']  # remove empty strings
    
    return [rank(words, 3, 4, 2), rank(words, 5, len(words)+1, 4)]

