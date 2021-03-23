"""


Create a function that takes the month and year (as integers) and returns the
number of days in that month.

### Examples

    days(2, 2018) ➞ 28
    
    days(4, 654) ➞ 30
    
    days(2, 200) ➞ 28
    
    days(2, 1000) ➞ 28

### Notes

Don't forget about leap years!

"""

def day_amount(month, year):
  if month==2:
    if year%4==0:
      if year%100==0:
        if year%400==0:
          return(29)
        else:
          return(28)
      else:
        return(29)
    else:
      return(28)
  elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    return(31)
  else:
    return(30)

