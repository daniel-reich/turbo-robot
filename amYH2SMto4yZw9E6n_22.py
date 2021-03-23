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

def validate(s):
​
    if len(s) == 16:
        aux = s.split()
        if len(aux[0]) == 1 and len(aux[1]) == 5 and len(aux[-1]) == 8:
            return aux[1][0] == '(' and aux[1][-1] == ')' and aux[-1][3] == '-'
​
    elif len(s) == 15:
        aux = s.split('-')
        if len(aux[0]) == 2 and len(aux[1]) == len(aux[2]) and len(aux[-1]) == 4:
            return s[0] == '+' and s[2] == s[6] == s[10]
​
    elif len(s) == 14:
        if s[1] == s[5] == s[9]:
            return True
        return s[0] == '(' and s[4:6] == ') ' and s[9] == '-'
​
    elif len(s) == 12:
        return s[3] == s[7] and s[3] in [' ', '.', '/', '-']
​
    elif len(s) in [10, 11]:
        try:
            return bool(int(s))
        except:
            pass
    return False

