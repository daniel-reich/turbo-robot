"""


Write a function that takes in a string and returns all possible combinations.
Return the final result in **alphabetical order**.

### Examples

    unravel("a[b|c]") ➞ ["ab", "ac"]
    
    unravel("a[b|c]de[f|g]") ➞ ["abdef", "acdef", "abdeg", "acdeg"]
    
    unravel("a[b]c[d]") ➞ ["abcd"]
    
    unravel("a[b|c|d|e]f") ➞ ["abf", "acf", "adf", "aef"]
    
    unravel("apple [pear|grape]") ➞ ["apple grape", "apple pear"]

### Notes

Think of each element in every block (e.g. `[a|b|c]`) as a **fork in the
road**.

"""

import re
def ravel_list(lst):
    
    current_result = []
    
    if isinstance(lst[0],str):
        current_result.append(lst[0])
    else:
        for e in lst[0]:
            current_result.append(e) 
    
    if len(lst) == 1:
        result = current_result
        result.sort()
        return result
    
    next_result = ravel_list(lst[1:]) 
    
    result = []
    for i in range(len(current_result)):
        for j in range(len(next_result)):
            result.append(current_result[i]+next_result[j])
​
    result.sort()
    
    return result
   
    
def unravel(text):
    new_text = re.findall(r'[^\[\]]+',text)
    new_text2 = []
    for e in new_text:
        if '|' in e:
            temp = e.split('|')
            new_text2.append(temp)
        else:
            new_text2.append(e)
    
    #print(new_text2)
    result = ravel_list(new_text2)
    return result

