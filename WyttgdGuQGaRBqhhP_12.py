"""


Given an _incomplete palindrome_ as a string, return the **minimum letters
needed** to be added on to the **end** to make the string a **palindrome**.

### Examples

    min_palindrome_steps("race") ➞ 3
    # Add 3 letters: "car" to make "racecar"
    
    min_palindrome_steps("mada") ➞ 1
    # Add 1 letter: "m" to make "madam"
    
    min_palindrome_steps("mirror") ➞ 3
    # Add 3 letters: "rim" to make "mirrorrim"

### Notes

Trivially, words which are already palindromes should return `0`.

"""

def min_palindrome_steps(txt):
  if txt==txt[::-1]:  return 0
  l = [txt+txt[::-1][x:] for x in range(len(txt)-1,-1,-1)]
  p = [l[x] for x in range(len(l)) if l[x]==l[x][::-1]]
  return len(p[0])-len(txt)

