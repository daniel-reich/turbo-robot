"""


Create a function that takes an Arabic number and converts it into a Roman
number.

### Examples

    convert_to_roman(2) ➞ "II"
    
    convert_to_roman(12) ➞ "XII"
    
    convert_to_roman(16) ➞ "XVI"

### Notes

  * All roman numerals should be returned as uppercase.
  * The largest number that can be represented in this notation is 3,999.

"""

import re
def convert_to_roman(num):
    string_list = []
    M = num // 1000
    C = (num % 1000) // 100
    X = (num % 1000) % 100 // 10
    I = (num % 1000) % 100 % 10
​
    for m in range(0,M):
        string_list.append("M")
    
    for c in range(0,C):
        string_list.append("C")
​
    for x in range(0,X):
        string_list.append("X")
​
    for i in range(0,I):
        string_list.append("I")
​
    return_str = "".join(string_list)
​
    return_str = re.sub(r"CCCCCCCCC",r"CM", return_str)
    return_str = re.sub(r"CCCCCCCC",r"DCCC", return_str)
    return_str = re.sub(r"CCCCCCC",r"DCC", return_str)
    return_str = re.sub(r"CCCCCC",r"DC", return_str)
    return_str = re.sub(r"CCCCC",r"D", return_str)
    return_str = re.sub(r"CCCC",r"CD", return_str)
    return_str = re.sub(r"XXXXXXXXX",r"XC", return_str)
    return_str = re.sub(r"XXXXXXXX",r"LXXX", return_str)
    return_str = re.sub(r"XXXXXXX",r"LXX", return_str)
    return_str = re.sub(r"XXXXXX",r"LX", return_str)
    return_str = re.sub(r"XXXXX",r"L", return_str)
    return_str = re.sub(r"XXXX",r"XL", return_str)
    return_str = re.sub(r"IIIIIIIII",r"IX", return_str)
    return_str = re.sub(r"IIIIIIII",r"VIII", return_str)
    return_str = re.sub(r"IIIIIII",r"VII", return_str)
    return_str = re.sub(r"IIIIII",r"VI", return_str)
    return_str = re.sub(r"IIIII",r"V", return_str)
    return_str = re.sub(r"IIII",r"IV", return_str)
    return return_str

