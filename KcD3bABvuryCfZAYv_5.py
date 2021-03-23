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
  char_dict = {}
  for word in lst:
    for char in word:
      if char in char_dict:
        char_dict[char] += 1
      else:
        char_dict[char] = 1
  max_value = max(char_dict.values())
  max_keys = []
  for key, value in char_dict.items():
    if value == max_value:
      max_keys.append(key)
  return sorted(max_keys)

