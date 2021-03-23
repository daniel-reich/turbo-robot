"""


Write a function that returns `True` if the phone number is in a valid format.
Valid formats are as follows:

 **With Country Code**|  **Without Country Code**  
---|---  
+1-892-445-7663| 892-445-7663  
1-892-445-7663| (892) 445-7663  
1 (892) 445-7663| 892.567.8901  
1.892.567.8901| 1/892/567/8901  
1 892 567 8901| 892/567/8901  
18925678901| 892 567 8901  
  
### Examples

    validate("578-332-1114") ➞ True
    
    validate("57-332-1114") ➞ False
    
    validate("577 332  1114") ➞ False
    # More than one space in between digits clusters.
    
    validate("57 332 1114") ➞ False
    # Unacceptable digit cluster length.
    
    validate("157%332-1114") ➞ False
    # Unacceptable delimiter.

### Notes

  * The country code will always be `+1` or `1`.
  * Each phone number will contain either 10 or 11 digits (depending on whether the country code exists).
  * There must either be exactly one space, a delimiter, or no space at all between the digit clusters.
  * You do not have to worry about extensions.

"""

import re
def validate(s):
    if '  ' in s:
        return False
    x=re.split('[.+/)( -]',s)
    y=[i for i in x if i!='']
    if y[0].isnumeric() and y[0]==s:
        return True
    print(y)
    a=sum(len(i) for i in y)
    if y[0]=='1':
        y.pop(0)
        if a!=11:
            return False
    if len(y[0])!=3 or len(y[1])!=3 or len(y[2])!=4:
        return False
    if not ''.join(y).isnumeric():
        return False
    return True

