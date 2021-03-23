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

def longest_nonrepeating_substring(string):
    start = end  = 0 
    out = final = ''
    frequency = set()
    while start < len(string):
        if end < len(string) and string[end] not in frequency:
            out += string[end]
            final = max(final, out, key=len)
            frequency.add(string[end])
            end += 1
        else:
            frequency.discard(string[start])
            out = out[1:]
            start += 1
    return final

