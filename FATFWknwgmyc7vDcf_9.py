"""


My friend required some help with an assignment in school and I thought this
would be a nice addition to be added as a challenge here as well.

Create a function that takes a sentence and returns a modified sentence abided
by these rules:

  * If you encounter a **date** within the sentence, **in the format DD/MM/YY** or **DD.MM.YY** , you have to change it over to **DD/MM/YYYY** or **DD.MM.YYYY** (same separator char).
  * If you encounter a **date** within the sentence, **in the format MonthName, DD. YY.** you have to change it over to **MonthName, DD. YYYY.**
  * If you encounter an **invalid MonthName** then leave it as is.
  *  **For this challenge there is an arbitrary rule that if YY is less than 25 the year-prefix will be 20, otherwise, the year-prefix will be 19**.
  * Meaning 08/11/20 -> 08/11/2020 or 02/11/95 -> 02/11/1995

### Examples

    small_favor("I was born on 11/02/98")
    ➞ "I was born on 11/02/1998"
    
    small_favor("I was born on 11/02/98 and what about you?")
    ➞ "I was born on 11/02/1998 and what about you?"
    
    small_favor("I was born on 02.11.19")
    ➞ "I was born on 02.11.2019"
    
    small_favor("I was born on February, 02. 98.")
    ➞ "I was born on February, 02. 1998."
    
    small_favor("I was born on January, 01. 15. and today is October, 08. 20.")
    ➞ "I was born on January, 01. 2015. and today is October, 08. 2020."
    
    small_favor("I was born on Fakemonthy, 01. 15. dont change invalid dates")
    ➞ "I was born on Fakemonthy, 01. 15. dont change invalid dates"

### Notes

Don't forget to apply the arbitrary year-prefix rule defined above.

  * DD/MM/YY -> DD/MM/YYYY
  * DD.MM.YY -> DD.MM.YYYY
  * Month, DD. YY. -> Month, DD. YYYY.
  * DD|MM|YY -> DD|MM|YY ( **invalid separator** , means it remains unchanged)

"""

import re
​
def replace_year(match):
  date_parts = list(match.groups())
  separator = date_parts[1]
  del date_parts[1]
  
  if int(date_parts[2]) < 25:
    date_parts[2] = "20" + date_parts[2]
  else:
    date_parts[2] = "19" + date_parts[2]
  return separator.join(date_parts)
​
def replace_year_with_month_format(match):
  date_parts = list(match.groups())
  
  if int(date_parts[2]) < 25:
    date_parts[2] = "20" + date_parts[2]
  else:
    date_parts[2] = "19" + date_parts[2]
  return date_parts[0] + ', ' + date_parts[1] + '. ' + date_parts[2] + '.'
​
def small_favor(sentence):
  firstPass = re.sub(r'([0-9]{2})([/.])([0-9]{2})[/.]([0-9]{2})', replace_year, sentence)
  
  return re.sub(r'(January|February|October), ([0-9]{2}). ([0-9]{2}).', replace_year_with_month_format, firstPass)

