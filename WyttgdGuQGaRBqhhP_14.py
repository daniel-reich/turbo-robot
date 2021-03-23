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
  # deal with one-letter text
  if len(txt)==1:
    return 0
    
  # for every letter in the second half, check if it 
  # can be the middle of a possible palindrome
  for mid in range(len(txt)//2, len(txt)-1):
    after_mid  = txt[mid:]
    before_mid = txt[mid+1-len(after_mid):mid+1]
    print("%s %d %s %s" % (txt, mid, after_mid, before_mid))
    if (after_mid[::-1] == before_mid):
      return (mid + 1 - len(before_mid))
  
  # take into account how many times the last letter appears in sequence
  last_char = len(txt)-1
  while last_char - 1 >= 0 and txt[last_char - 1] == txt[last_char]:
    last_char -= 1
      
  return len(txt) - 1 - (len(txt) - 1 - last_char)

