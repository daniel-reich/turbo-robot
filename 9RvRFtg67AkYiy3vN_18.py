"""


Create a **left rotation** and a **right rotation** function that returns all
the left rotations and right rotations of a string.

### Examples

    left_rotations("abc") ➞ ["abc", "bca", "cab"]
    
    right_rotations("abc") ➞ ["abc", "cab", "bca"]
    
    left_rotations("abcdef")
    ➞ ["abcdef", "bcdefa", "cdefab", "defabc", "efabcd", "fabcde"]
    
    right_rotations("abcdef")
    ➞ ["abcdef", "fabcde", "efabcd", "defabc", "cdefab", "bcdefa"]

### Notes

N/A

"""

def left_rotations(txt):
    temp = ""
    resultText= ""
    result = []
    result.append(txt)
    newTxt = list(txt)
​
    for i in range(len(txt) - 1):
        temp = newTxt[0]
        newTxt.remove(newTxt[0])
        newTxt.append(temp)
        result.append(resultText.join(newTxt))
    return result
def right_rotations(txt):
    temp = ""
    resultText = ""
    result = []
    result.append(txt)
    newTxt = list(txt)
    print(newTxt)
​
    for i in range(0,len(txt) - 1):
        temp = newTxt[len(txt) - 1]
        newTxt.pop()
        newTxt.insert(0,temp)
        result.append(resultText.join(newTxt))
    return result

