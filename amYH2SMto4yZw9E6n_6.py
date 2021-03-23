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

from itertools import groupby
def validate(s):
    a, c = [], []
    clusters = [[1,3,3,4],[3,3,4]]
    valid = ' -()/.+'
    for key, group in groupby(s, key=lambda x: x.isdigit()):
        if key:
            a.append(list(group))
        else:
            container = list(group)
            c.extend(container)
            if c[-1] not in valid:
                return False
            if len(container) > 1 and container[0] == container[1]:
                return False
    
    if not c:
        d = sum(a, [])
        if len(d) == 11 or len(d) == 10:
            return True
​
    return [len(x) for x in a] in clusters and not(not s[0].isdigit() and s[0] not in valid)

