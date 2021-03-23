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
  s = set(''.join(lst))
  s1 = [{'name': x, 'count': ''.join(lst).count(x)} for x in s]
  maxn = max(s1, key=lambda x: x.get('count')).get('count')
  s2 = filter(lambda x: x.get('count') == maxn, s1)
  return sorted([x.get('name') for x in s2])

