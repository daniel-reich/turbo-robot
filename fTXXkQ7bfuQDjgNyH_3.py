"""


Each year has 365 or 366 days. Given a string `date` representing a Gregorian
calendar date formatted as `month/day/year`, return the _day-number_ of the
year.

### Examples

    day_of_year("11/16/2020") ➞ 321
    
    day_of_year("1/9/2019") ➞ 9
    
    day_of_year("3/1/2004") ➞ 61
    
    day_of_year("12/31/2000") ➞ 366

### Notes

All input strings in tests are valid dates.

"""

months = ["NAN", 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
​
def day_of_year(date):
  return (
  int(date.split("/")[1]) +
  
  months[int(date.split("/")[0])] +
  
  (int(date.split("/")[2])%4==0 
  and (int(date.split("/")[2])%100!=0 or int(date.split("/")[2])%400==0)
  and int(date.split("/")[0])>2
  and 1)
  )

