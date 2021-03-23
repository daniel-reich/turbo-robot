"""


Create a function which takes in a date as a string, and **returns the date a
week after**.

### Examples

    week_after("12/03/2020") ➞ "19/03/2020"
    
    week_after("21/12/1989") ➞ "28/12/1989"
    
    week_after("01/01/2000") ➞ "08/01/2000"

### Notes

  * Note that dates will be given in **day/month/year** format.
  * Single digit numbers should be **zero padded**.
  * See **Resources** for some helpful tutorials on Python dates.

"""

def week_after(d):
  date = d.split("/")
  date[0] = int(date[0]) + 7
  m = ["04", "06", "09", "11"]
  if date[1] in m and date[0] > 30:
    date[0] = date[0] - 30
    date[1] = int(date[1]) + 1
  elif date[1] == "02" and date[0] > 28:
    date[0] = date[0] - 28
    date[1] = int(date[1]) + 1
  elif date[0] > 31:
    date[0] = date[0] - 31
    date[1] = int(date[1]) + 1
  if int(date[1]) > 12:
    date[1] = 1
    date[2] = int(date[2]) + 1
  if date[0] < 10:
    date[0] = "0" + str(date[0])
  if int(date[1]) < 10 and not str(date[1]).startswith("0"):
    date[1] = "0" + str(date[1])
  return str(date[0]) + "/" + str(date[1]) + "/" + str(date[2])

