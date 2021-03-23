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
    longest_string = ''
    current_string = ''
    for i in range(len(txt)):
        for x in txt[i:]:
            if x not in current_string:
                current_string+=x
            else:
                current_string = ''
                break
            if len(current_string) > len(longest_string):
                longest_string = current_string
    return longest_string

