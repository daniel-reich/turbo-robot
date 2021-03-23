"""


Create a function that takes in a year and returns the correct century.

### Examples

    century(1756) ➞ "18th century"
    
    century(1555) ➞ "16th century"
    
    century(1000) ➞ "10th century"
    
    century(1001) ➞ "11th century"
    
    century(2005) ➞ "21st century"

### Notes

  * All years will be between `1000` and `2010`.
  * The 11th century is between 1001 and 1100.
  * The 18th century is between 1701-1800.

"""

def century(year):
 a=[]
 for e in range(0,3000,100):
    a.append(e)
 for i in range(len(a)):
    if a[i]>2000:
        return str(int(str(year)[:2])+1)+'st'+' century'
        break
    elif a[i]==year:
        return str(int(str(year)[:2]))+'th'+' century'
        break
    elif a[i]>year:
        return str(int(str(year)[:2])+1)+'th'+' century'
        break

