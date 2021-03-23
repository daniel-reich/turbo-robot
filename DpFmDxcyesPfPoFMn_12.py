"""


The International Standard Book Number (ISBN) is a unique identifying number
given to each published book. ISBNs assigned after January 2007 are 13 digits
long (ISBN-13), however books with 10-digit ISBNs are still in wide use.

An ISBN-10 is verified this way:

    isbn10 = "0330301624"

Line up the digits with the numbers 10 to 1:

| | | | | | | | |  
---|---|---|---|---|---|---|---|---|---  
0| 3| 3| 0| 3| 0| 1| 6| 2| 4  
10| 9| 8| 7| 6| 5| 4| 3| 2| 1  
  
Multiply each digit with the number below it (the 10th digit in an ISBN can be
an X. This last X simply means 10).

Sum up the products:

    0 + 27 + 24 + 0 + 18 + 0 + 4 + 18 + 4 + 4 = 99

If the sum is divisible by **11** , the ISBN-10 is _valid_.

An ISBN-13 is verified this way:

    isbn13 = "9780316066525"

Line up the digits with alternating 1s and 3s:

| | | | | | | | | | | |  
---|---|---|---|---|---|---|---|---|---|---|---|---  
9| 7| 8| 0| 3| 1| 6| 0| 6| 6| 5| 2| 5  
1| 3| 1| 3| 1| 3| 1| 3| 1| 3| 1| 3| 1  
  
Multiply each digit with the number below it and get the sum:

    9 + 21 + 8 + 0 + 3 + 3 + 6 + 0 + 6 + 18 + 5 + 6 + 5 = 90

If the sum is divisible by **10** , the ISBN-13 is _valid_.

Create a function that takes a string of numbers (possibly with an X at the
end) and...

  1. Return `"Invalid"` if it is not a valid ISBN-10 or ISBN-13.
  2. Return `"Valid"` if it is a valid ISBN-13.
  3. If it is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.

Convert a valid ISBN-10 to ISBN-13 by tacking 978 to the start, then changing
the last digit (the check digit) so that the resulting number passes the
ISBN-13 check.

### Examples

    isbn13("9780316066525") ➞ "Valid"
    
    isbn13("0330301824") ➞ "Invalid"
    
    isbn13("0316066524") ➞ "9780316066525"

### Notes

N/A

"""

def fixisbn(isbn, txt):
    rounded = round(isbn, -1)
    digit = int(txt[12]) + rounded - isbn
    return txt[:12] + str(digit)
​
def isbn10(txt):
    result = "Invalid"
    multiplier = 10
    isbn = 0
    for char in txt:
        if char == "X":
            isbn += 10 * multiplier
        else:
            isbn += int(char) * multiplier
            multiplier-=1
​
    if (isbn%11) == 0:
        txt = "978" + txt
        txt = txt.replace("X","0")
        isbn = getisbn(txt)
        result = fixisbn(isbn,txt)
​
    return result
​
def getisbn(txt):
    isbn = 0
    multiplier = 1
    for char in txt:
        isbn += int(char) * multiplier
        if multiplier == 1:
            multiplier = 3
        else:
            multiplier = 1
    return isbn
​
def isbn13(txt):
    isbn = 0
    if len(txt) == 10:
        return isbn10(txt)
    else:
        isbn = getisbn(txt)
        return "Valid" if (isbn%10==0) else "Invalid"

