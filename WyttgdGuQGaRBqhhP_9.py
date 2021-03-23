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
  data=list('-') # variable for Palindrome as list, '-' for begin of string
  for position in range(0,len(txt)):
    tmp=data.pop() # get next letter from Palindrome
    if ( tmp != txt[position] or tmp=='-'): # current letter and Palindrome are not the same, or Palindrome too short # start over:
      if(txt[position]==txt[position-1]): # hey, twice the same letter
        data=list('-'+txt[:position-1]) # case for ...aa
      else:
        data=list('-'+txt[:position]) # case for ...a
  return(len(data)-1) # minus -1 for '-'

