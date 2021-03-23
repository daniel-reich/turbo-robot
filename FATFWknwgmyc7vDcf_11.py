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

MONTH = ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]
​
def case1(sentence, sep, month, pos):
    if pos < 2 or pos > len(sentence) - 2:
        return sentence
    chunk = sentence[pos-2:pos+4+2]
    try:
        day = int(chunk[:2])
        year = int(chunk[-2:])
        year = 2000 + year if year < 24 else 1900 + year
        return sentence[:pos+4] + str(year) + sentence[pos+6:]
    except:
        return sentence
​
def case2(sentence, month, pos):
    chunk = sentence[pos+len(month):pos+len(month)+9]
    if chunk[:2] != ", " or chunk[4] != "." or chunk[-1] != ".":
        return sentence
    try:
        day = int(chunk[2:4])
        year = int(chunk[6:8])
        year = 2000 + year if year < 24 else 1900 + year
        return sentence[:pos] + month + chunk[:-3] + str(year) + "." + sentence[pos+len(month)+9:]
    except:
        return sentence
​
def small_favor(sentence):
    for month in MONTH:
        positions = [k for k in range(len(sentence)-len(month)) if sentence[k:k+len(month)] == month]
        for pos in positions:
            sentence = case2(sentence, month, pos)
    for sep in ['.', '/']:
        for m in range(1, 13):
            month = str(m).zfill(2)
            a = sep + month + sep
            positions = [k for k in range(len(sentence)-4) if sentence[k:k+4] == a]
            for pos in positions:
                sentence = case1(sentence, sep, month, pos)
    return sentence

