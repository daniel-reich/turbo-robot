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
    chars = ''.join(chars)
    ans=''
    for i,char in enumerate(chars):
        if char!=chars[i-1]:ans+=" "+char
        else:ans+=char
    return ''.join(list(map(lambda x:x[0] + str(x.count(x[0])) if x.count(x[0]) !=1 else x[0] ,ans.strip().split(" "))))

