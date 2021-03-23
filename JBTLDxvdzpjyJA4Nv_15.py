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

def checkdup(str):
    result = False
    if len(str) == 1:
        return False
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            result = True
    return result
​
​
def super_reduced_string(txt):
    result = ""
    count = 1
    while checkdup(txt):
        for i in range(len(txt) - 1):
            if txt[i] == txt[i + 1]:
                count += 1
            else:
                if count % 2 == 1:
                    result = result + txt[i]
                count = 1
            if i == len(txt)-2 and count > 1:
                if count % 2 == 1:
                    result = result + txt[i]
        if txt[-1] != txt[-2]:
            result = result + txt[-1]
        txt = result
        result = ""
​
    return "Empty String" if txt == "" else txt

