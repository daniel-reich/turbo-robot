"""


The function is given an array of characters. **Recursively compress** the
array into a string using the following rules. For each group of consecutively
repeating characters:

  * If the number of repeating characters is one, append the string with only this character.
  * If the number `n` of repeating characters `x` is greater than one, append the string with `"x" + str(n)`.

### Examples

    compress(["t", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "s", "s", "s", "h"]) ➞ "te14s3h"
    
    compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"
    
    compress(["a"]) ➞ "a"
    
    compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"
    
    compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"

### Notes

  * You are expected to solve this challenge using the concept of **recursion**.
  * Check out the **Resources** tab for more details on _recursion_.
  * An **iterative** version of this challenge (which was originally published by @Evgeny SH) can be found via this [link](https://edabit.com/challenge/6RHxTTndfASnPyp8Z).

"""

def compress(c):
​
  return compress_old(c)
  
  
def compress_old(chars):
  ct,last=0,''
  out=''
  for c in chars:
    if last==c:
      ct+=1
    else:
      out+=last+ (str(ct) if ct>1 else '' )
      ct,last=1,c
  return out+last+(str(ct) if ct>1 else '' )

