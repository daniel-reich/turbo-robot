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
    is_valid = False
    seps = ('', ' ', '.', '-', '/', '0')
    for sep in seps:
        sep = re.escape(sep)
        if sep == '\\-':
            pattern = '(\\+?{1}{0})?{2}{0}{2}{0}{3}'.format(sep,'\d{1}','\d{3}','\d{4}')
        elif sep == '0':
            pattern = '({1} )?{4}{2}{5} {2}{0}{3}'.format(re.escape('-'),'\d{1}','\d{3}','\d{4}',re.escape('('),re.escape(')'))
        else:
            pattern = '({1}{0})?{2}{0}{2}{0}{3}'.format(sep,'\d{1}','\d{3}','\d{4}')
        is_valid = is_valid or bool(re.fullmatch(pattern, s))
    return is_valid

