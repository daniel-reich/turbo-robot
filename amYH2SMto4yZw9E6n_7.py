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
  dash_amount = s.count('-')
  possibilities = {'+3d': '+i-iii-iii-iiii', '3d':'i-iii-iii-iiii', '2d': 'iii-iii-iiii', 'pncc': '(iii) iii-iiii', 'pcc': 'i (iii) iii-iiii', '3.': 'i.iii.iii.iiii', '2.': 'iii.iii.iiii', '3/': 'i/iii/iii/iiii', '2/': 'iii/iii/iiii', '3sp': 'i iii iii iiii', '2sp': 'iii iii iiii', 'nonewcc': 'iiiiiiiiiii', 'nonewocc': 'i' * 10}
​
  if dash_amount == 3:
    if '+' in s:
      typ = '+3d'
    else:
      typ = '3d'
  elif dash_amount == 2:
    typ = '2d'
  elif dash_amount == 1:
    if '(' in s:
      if s[0] == '(':
        typ = 'pncc'
      else:
        typ = 'pcc'
  elif dash_amount == 0:
    if '.' in s:
      if s.count('.') == 3:
        typ = '3.'
      else:
        typ = '2.'
    elif '/' in s:
      if s.count('/') == 3:
        typ = '3/'
      else:
        typ = '2/'
    else:
      if ' ' in s:
        if s.count(' ') == 3:
          typ = '3sp'
        else:
          typ = '2sp'
      else:
        if len(s) == 11:
          typ = 'nonewcc'
        elif len(s) == 10:
          typ = 'nonewocc'
        else:
          return False
​
  try:
    t = typ
  except UnboundLocalError:
    return False
    
  actual = ''
  
  if len(s) != len(possibilities[typ]):
    return False
    
  for item in s:
    try:
      test = int(item)
      actual += 'i'
    except ValueError:
      actual += item
      
  return actual == possibilities[typ]

