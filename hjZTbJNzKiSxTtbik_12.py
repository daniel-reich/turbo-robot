"""


Create a function that sorts words by a given string.

### Examples

    sort_by_string(["poof", "floof", "loop"], "flatp")
    ➞ ["floof", "loop", "poof"]
    
    sort_by_string(["small", "big", "medium"], "sazymtb")
    ➞ ["small", "medium", "big"]
    
    sort_by_string(["apple", "banana", "cherry", "date"], "dbca")
    ➞ ["date", "banana", "cherry", "apple"]

### Notes

  * The string may have excess letters (see examples #1 and #2).
  * There will be unique starting letters in each list.

"""

def sort_by_string(lst, txt):
  newSort = []
  for letter in txt:
    for word in lst:
      if word[0] == letter:
        newSort.append(word)
  return newSort

