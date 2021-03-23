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
    if s[0] == "+":
        s = s[1:]
    s = s[::-1]
    s = numeric(s, 4)
    for _ in range(2):
        s = delimiter(s)
        s = numeric(s, 3)
​
    if s == "" or s == "(":
        return True
    s = delimiter(s)
    if s == "1":
        return True
    return False
    
def numeric(s, x):
    for i in range(x):
        if not s[i].isnumeric() or len(s) < x:
            s = "FALSE"
    s = s[x :]
    return s
    
def delimiter(s):
    if s[: 2] in ["( ", " )"]:
        s = s[2 :]    
    elif s[0] in [" ", "-", ".", "/"]:
        s = s[1 :]
    return s

