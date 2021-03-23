"""


The function is given an array of characters. Compress the array into a string
using the following rules. For each group of consecutively repeating
characters:

  * If the number of repeating characters is one, append the string with only this character.
  * If the number `n` of repeating characters `x` is greater than one, append the string with `"x" + str(n)`.

### Examples

    compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"
    
    compress(["a"]) ➞ "a"
    
    compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"
    
    compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"

### Notes

N/A

"""

def compress(chars):
    last = chars[0]
    cnt = 1
    ans = ""
    for cur in chars[1:]:
        if cur == last:
            cnt += 1
        else:
            ans += last
            if cnt > 1:
                ans += str(cnt)
            last = cur
            cnt = 1
    ans += last
    if cnt > 1:
        ans += str(cnt)
    return ans

