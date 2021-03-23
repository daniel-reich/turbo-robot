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
    revtxt = txt[::-1]
    if(txt == revtxt):
        return True
    else:
        lis = {}
        for i in txt:
            if(i in lis):
                lis[i] += 1
            else:
                lis[i] = 1
​
        l = []
        for i in lis.values():
            if(i % 2 != 0):
                l.append(1)
​
        if(len(l)  == 1):
            return True
        elif(len(l) == 0):
            return True
        else:
            return False

