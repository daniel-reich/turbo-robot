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

def longest_nonrepeating_substring(txt):
    longest = ""
    index = 0
    while len(txt) > 0:
        index += 1
        if len(txt[ : index]) != len(set(txt[ : index])):
            if len(txt[ : index - 1]) > len(longest):
                longest = txt[ : index - 1]
            txt = txt[1 :]
            index = 0
        if index == len(txt):
            if len(txt) > len(longest):
                longest = txt
            txt = []
    return longest

