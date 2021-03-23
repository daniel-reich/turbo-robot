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

def is_palindrome_possible(s):
    can_have_odd = len(s) % 2 == 1
    s = sorted(s)
    counter = 1
    prev = s[0]
​
    for i in range(1, len(s)):
        if prev != s[i]:
            if counter % 2 == 1:
                if can_have_odd:
                    can_have_odd = False
                else:
                    return False
            prev = s[i]
            counter = 1
        else:
            counter += 1
​
    return True

