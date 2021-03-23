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
    position_hash, current_start, max_sub_length, max_sub_start = {}, 0, 0, 0
    for i in range(len(txt)):
        if txt[i] not in position_hash: position_hash[txt[i]] = i
        else:
            if position_hash[txt[i]] >= current_start:
                if max_sub_length < i - current_start: max_sub_length, max_sub_start = i - current_start, current_start
                current_start = position_hash[txt[i]] + 1
            position_hash[txt[i]] = i
    if max_sub_length < i + 1 - current_start: max_sub_length, max_sub_start = i + 1 - current_start, current_start
    return txt[max_sub_start: max_sub_start + max_sub_length]

