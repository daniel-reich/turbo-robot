"""


Create a function to convert a list of percentages to their decimal
equivalents.

### Examples

    convert_to_decimal(["1%", "2%", "3%"]) ➞ [0.01, 0.02, 0.03]
    
    convert_to_decimal(["45%", "32%", "97%", "33%"]) ➞ [0.45, 0.32, 0.97, 0.33]
    
    convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) ➞ [0.33, 0.981, 0.5644, 1]

### Notes

N/A

"""

import re
def convert_to_decimal(perc):
    num = re.findall('\d*\.?\d+', "".join(perc))
    answer = []
    
    for i in num:
        if "." in i:
            answer.append(float(i)/100)
        else:
            answer.append(int(i)/100)
​
    return answer

