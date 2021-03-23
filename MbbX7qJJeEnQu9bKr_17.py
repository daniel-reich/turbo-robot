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
  counts = {ch:text.count(ch) for ch in set(text)}
  if len(set(counts.values())) == 1:
    return 'No Repetition'
    
  m_count = max(counts.values())
  return [k for k, v in counts.items() if v == m_count]

