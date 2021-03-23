"""


Steve has a string of lowercase characters in range `ascii[["a".."z"]]`. He
wants to reduce the string to its shortest length by doing a series of
operations. In each operation, he selects a pair of adjacent lowercase letters
that match, and he deletes them. For instance, the string **aab** could be
shortened to **b** in one operation.

Steve’s task is to delete as many characters as possible using this method and
print the resulting string. If the final string is empty, return `"Empty
String"`.

### Case

    super_reduced_string("aaabccddd") ➞ "abd"

Explanation:

    "aaabccddd" -> "abccddd" -> "abddd" -> "abd"

### Examples

    super_reduced_string("cccxllyyy") ➞ "cxy"
    
    super_reduced_string("aa") ➞ "Empty String"
    
    super_reduced_string("baab") ➞ "Empty String"
    
    super_reduced_string("fghiiijkllmnnno") ➞ "fghijkmno"
    
    super_reduced_string("chklssstt") ➞ "chkls"

### Notes

N/A

"""

def dfs(txt, ans):
    if len(txt) <= 1:
        return ans if len(ans) > 0 else "Empty String"
    for i in range(1, len(txt)):
        if txt[i-1] == txt[i]:
            txt2 = txt[:i-1] + txt[i+1:]
            if len(txt2) < len(ans):
                ans = txt2
            ans = dfs(txt2, ans)
    return ans if len(ans) > 0 else "Empty String"
​
def super_reduced_string(txt):
    return dfs(txt, txt)

