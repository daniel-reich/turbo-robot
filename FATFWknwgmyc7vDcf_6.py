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
def subs(m):
  res = m.group(1)+ m.group(2) + m.group(3)+ m.group(4)
  if int(m.group(5)) <= 20:
    res = res + "20" + m.group(5)
  else:
    res = res + "19" + m.group(5)
  return res
​
​
def small_favor(sentence):
  regex = r"(0[1-9]|1[0-9]|2[0-9]|3[0-1])(/|\.)(0[1-9]|1[0-2])(/|\.)([0-9][0-9])" 
  sentence = re.sub(regex,subs,sentence)
  regex = r"(January|February|March|April|May|June|July|August|September|October|November|December)(/|\.|, )(0[1-9]|1[0-9]|2[0-9]|3[0-1])(/|\. )([0-9][0-9])"
  # print(re.search(regex, sentence).group(2))
  return re.sub(regex,subs,sentence)
