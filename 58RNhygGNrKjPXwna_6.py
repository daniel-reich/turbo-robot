"""


Write a function that returns the **longest non-repeating substring** for a
string input.

### Examples

    longest_nonrepeating_substring("abcabcbb") ➞ "abc"
    
    longest_nonrepeating_substring("aaaaaa") ➞ "a"
    
    longest_nonrepeating_substring("abcde") ➞ "abcde"
    
    longest_nonrepeating_substring("abcda") ➞ "abcd"

### Notes

  * If multiple substrings tie in length, return the one which occurs **first**.
  *  **Bonus** : Can you solve this problem in **linear time**?

"""

def allPossible(string, length): #Return all possible continuous strings of given length 
    limit = len(string) - length + 1
    words = []
    for i in range(limit):
        words.append(string[i: i + length])
    return words
​
def repeats(string): #returns True if there are repeats within the string, False otherwise
    letters = []
    for i in string:
        if i in letters:
            return True
        letters.append(i)
    return False
​
def longest_nonrepeating_substring(string):
    for i in range(len(string), 0, -1):
        words = allPossible(string, i)
        for word in words:
            if repeats(word) == False:
                return word

