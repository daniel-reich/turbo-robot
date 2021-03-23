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
    data1 = date.replace("/","")
    data2= data1[2:4]+data1[:2]+data1[4:]
    i = 0
    j = len(data1)-1
    while i <=j:
        if data1[i]!=data1[j] or data2[i]!=data2[j]:
            return False
        i+=1
        j-=1
    return True

