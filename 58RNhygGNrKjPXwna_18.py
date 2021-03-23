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
    l_run = []
    cur_longest = []
    for i in txt:
        if i not in l_run:
            l_run.append(i)
        else:
            if len(l_run) > len(cur_longest):
                cur_longest = l_run[:]
            l_run.append(i)
            del l_run[:l_run.index(i) + 1]
    if len(l_run) > len(cur_longest):
        cur_longest = l_run
    return ''.join(cur_longest)

