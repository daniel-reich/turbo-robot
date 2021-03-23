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
    lst_sub = []
    for i in range(len(txt)):
        cache_list = []
        j = i + 1
        cache_list.append(txt[i])
        while j < len(txt) and txt[j] not in cache_list:
            cache_list.append(txt[j])
            j += 1
        lst_sub.append(cache_list)
    cl = [len(i) for i in lst_sub]
    op_lst = lst_sub[cl.index(max(cl))]
    op_str = ""
    for c in op_lst:
        op_str += c
    return op_str

