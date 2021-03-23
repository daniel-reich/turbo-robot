"""


Create a function that can nest a flat list to represent an incremental depth
level sequence.

### Examples

    incremental_depth([1, 2]) ➞ [1, [2]]
    
    incremental_depth([1, 2, 3, 4, 5]) ➞ [1, [2, [3, [4, [5]]]]]
    
    incremental_depth([1, 3, 2, 6]) ➞ [1, [3, [2, [6]]]]
    
    incremental_depth(["dog", "cat", "cow"]) ➞ ["dog", ["cat", ["cow"]]]

### Notes

  * The elements do not matter to the function, you should increment by index.
  * Expect the array length to be from 2-20.

"""

def incremental_depth(lst):
    ret = []
    for num,ele in enumerate(lst):
        num = int(num)
        if num == 0:
            ret.append(ele)
        else:
        #why this site doesn't support f-string?f*ck this
            ele = [ele]
            if num == 1:
                eval('ret.append(ele)')
            else:
                eval('ret'+ ("[1]" * (num-1)) + '.append(ele)')
    return ret
    
    
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

