"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

def num_to_eng(n):
    eng_str = ""
    # 0 is a special case
    if n == 0:
        eng_str = "zero"
​
    else:
        # calculate the hundreds place
        space_needed = True
        if n >= 900:
            eng_str = "nine hundred"
        elif n >= 800:
            eng_str = "eight hundred"
        elif n >= 700:
            eng_str = "seven hundred"
        elif n >= 600:
            eng_str = "six hundred"
        elif n >= 500:
            eng_str = "five hundred"
        elif n >= 400:
            eng_str = "four hundred"
        elif n >= 300:
            eng_str = "three hundred"
        elif n >= 200:
            eng_str = "two hundred"
        elif n >= 100:
            eng_str = "one hundred"
        else:
            space_needed = False
​
        # 11 to 19 are special cases
        tmp = n % 100
        if tmp >= 11 and tmp <= 19:
            if space_needed:
                eng_str += " "
            if tmp == 11:
                eng_str += "eleven"
            elif tmp == 12:
                eng_str += "twelve"
            elif tmp == 13:
                eng_str += "thirteen"
            elif tmp == 14:
                eng_str += "fourteen"
            elif tmp == 15:
                eng_str += "fifteen"
            elif tmp == 16:
                eng_str += "sixteen"
            elif tmp == 17:
                eng_str += "seventeen"
            elif tmp == 18:
                eng_str += "eighteen"
            elif tmp == 19:
                eng_str += "nineteen"
        else:
            # calculate the tens place
            if space_needed:
                eng_str += " "
            if tmp >= 20 and tmp <= 99:
                space_needed = True
            if tmp >= 90:
                eng_str += "ninety"
            elif tmp >= 80:
                eng_str += "eighty"
            elif tmp >= 70:
                eng_str += "seventy"
            elif tmp >= 60:
                eng_str += "sixty"
            elif tmp >= 50:
                eng_str += "fifty"
            elif tmp >= 40:
                eng_str += "fourty"
            elif tmp >= 30:
                eng_str += "thirty"
            elif tmp >= 20:
                eng_str += "twenty"
            else:
                space_needed = False
    
            # calculate the ones place
            tmp = n % 10
            if space_needed:
                eng_str += " "
            if (tmp == 9):
                eng_str += "nine"
            elif (tmp == 8):
                eng_str += "eight"
            elif (tmp == 7):
                eng_str += "seven"
            elif (tmp == 6):
                eng_str += "six"
            elif (tmp == 5):
                eng_str += "five"
            elif (tmp == 4):
                eng_str += "four"
            elif (tmp == 3):
                eng_str += "three"
            elif (tmp == 2):
                eng_str += "two"
            elif (tmp == 1):
                eng_str += "one"
​
    print(eng_str)
    return eng_str

