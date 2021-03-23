"""


The 2nd of February 2020 is a palindromic date in both _dd/mm/yyyy_ and
_mm/dd/yyyy_ format (02/02/2020). Given a `date` in _dd/mm/yyyy_ format,
return `True` if the date is **palindromic** in **both date formats** ,
otherwise return `False`.

### Examples

    palindromic_date("02/02/2020") ➞ True
    
    palindromic_date("11/12/2019") ➞ False
    
    palindromic_date("11/02/2011") ➞ False
    # Although 11/02/2011 is palindromic in dd/mm/yyyy format,
    # it isn't in mm/dd/yyyy format (02/11/2011)

### Notes

  * All dates will be valid in both date formats.
  * The `date` must be palindromic in **both** _dd/mm/yyyy_ and _mm/dd/yyyy_ formats to pass.

"""

def palindromic_date(date):
  a = ''.join(date.split('/'))
  b = a[2:4] + a[0:2] + a[4:]
  if a == a[::-1] and a[::-1] == b:
    return True
  else:
    return False

