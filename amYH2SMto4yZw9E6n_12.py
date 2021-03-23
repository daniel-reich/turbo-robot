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
  numbers={str(i) for i in range(10)}
  if '  ' in s: return False
  if s.isdigit():
    if s[0]=='1': s=s[1:]
    return len(s)==10
  if s[0]=='+':
    if s[1]!='1': return False
    s=s[1:]
  if s[0]=='1': s=s[2:]
  if s[0]=='(':
    if s[4:6]!=') ' or s[-5]!='-': return False
    s=s[1:].replace(')','').replace('-',' ')
  delim = {'.', ')', '(', '-', '/', ' '}
  if len(set(s)-numbers-delim): return False
  if len(set(s)-numbers)!=1: return False
  for i in '-/.':
    s=s.replace(i,' ')
  s=s.split()
  return len(s[0])==len(s[1])==len(s[2])-1

