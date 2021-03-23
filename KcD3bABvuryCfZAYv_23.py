"""


Write a function that returns the most frequent character in a list of words.

### Examples

    most_frequent_char(["apple", "bandage", "yodel", "make"])
    ➞ ["a", "e"]
    
    most_frequent_char(["music", "madness", "maniac", "motion"])
    ➞ ["m"]
    
    most_frequent_char(["the", "hills", "are", "alive", "with", "the", "sound", "of", "music"])
    ➞ ["e", "h", "i"]

### Notes

  * If multiple characters tie for most frequent, list all of them in alphabetical order.
  * Words will be in lower case.

"""

def most_frequent_char(lst):
    joined_list = ''.join(lst)
    most_frequent = max(joined_list, key=joined_list.count)
​
    output = set(most_frequent)
​
    for character in joined_list:
        if joined_list.count(character) == joined_list.count(most_frequent):
            output.add(character)
    return sorted(list(output))

