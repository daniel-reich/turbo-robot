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

def palindromic_date(string):
    d = string.split("/")
    w = d[1] + d[0] + d[2]
    if "".join(d) == "".join(d)[::-1] and w == w[::-1]:
        return True
    return False

