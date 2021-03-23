"""


Given a string `text`. Write a function that returns the character with the
highest frequency. If more than 1 character has the same highest frequency,
return all those characters as an array sorted in ascending order. If there is
no repetition in characters, return `"No Repetition"`.

### Examples

    max_occur("Computer Science") ➞ ['e']
    
    max_occur("Edabit") ➞ "No Repetition"
    
    max_occur("system admin") ➞ ['m', 's']
    
    max_occur("the quick brown fox jumps over the lazy dog") ➞ [' ']

### Notes

Try to make use of the concept used in counting sort.

"""

def max_occur(text):
  max_number = 0
  for eachletter in text:
    if text.count(eachletter) > max_number:
      max_number = text.count(eachletter)
  if max_number == 1:
    return 'No Repetition'
  return list([x for x in set(list([x for x in text if text.count(x) == max_number]))])

