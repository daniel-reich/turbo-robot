"""


Given a word, create a function which returns whether or not it's possible to
**create a palindrome** by _rearranging the letters in the word_.

### Examples

    is_palindrome_possible("rearcac") ➞ True
    # You can make "racecar"
    
    is_palindrome_possible("suhbeusheff") ➞ True
    # You can make "sfuehbheufs" (not a real word but still a palindrome)
    
    is_palindrome_possible("palindrome") ➞ False
    # It's impossible

### Notes

  * Trivially, words which are already palindromes return `True`.
  * Words are given in all _lowercase_.

"""

def is_palindrome_possible(txt):
  def is_even(n):
    return n%2==0
  
  s = list(set(txt))
  counts = []
  one = 0
  
  for item in s:
    c = txt.count(item)
    if c != 1:
      counts.append(c)
    if c == 1:
      one += 1
  
  if one > 1:
    return False
  
  for count in counts:
    if is_even(count) == False:
      return False
  return True

