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

def is_palindrome_possible(STR1: str):
    STR_LST = list(STR1)
    AorB =  [str(STR1.count(i) % 2) for i in STR_LST]
    Zero_and_Ones = [AorB.count(i) for i in ['0','1']]
    return True if Zero_and_Ones[0] % 2 == 0 and Zero_and_Ones[1] in [0, 1] else False

