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
  l = len(s)
  if l == 11:
    return s[0] == "1" and s.isnumeric()
  if l == 12:
    return {s[3],s[7]} in [{"/"},{"-"},{"."},{" "}] and (s[0:3] + s[4:7] + s[8:12]).isnumeric()
  if l == 15:
    return s[0] == "+" and {s[2],s[6],s[10]} in [{"-"}] and (s[1:2]+s[3:6]+s[7:10]+s[11:15]).isnumeric()
  if l == 14:
    if s[0]+s[4:6]+s[9] == "() -":
      return (s[1:4]+s[6:9]+s[10:14]).isnumeric()
    return s[0] == "1" and {s[1],s[5],s[9]} in [{"/"},{"-"},{"."},{" "}] and (s[2:5] + s[6:9]+ s[10:14]).isnumeric()
  if l == 16:
    return s[0] == "1" and (s[1:3]+s[6:8]+s[11]) == " () -" and (s[3:6]+s[8:11]+s[12:16]).isnumeric()
  if l == 10:
    return s.isnumeric()
  return False

