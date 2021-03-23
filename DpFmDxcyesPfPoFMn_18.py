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

def is_isbn10(num):
    return (11-(sum((10 - i) * int(num[i]) for i in range(len(num)-1)) % 11)) % 11 == 10 if num[-1] == "X" else 11 - sum((10 - i) * int(num[i]) for i in range(len(num)-1)) % 11 == int(num[-1])
​
​
def check_digit(num):
    check = 10 - sum(1 * int(num[i]) if i % 2 == 0 else 3 *
                     int(num[i]) for i in range(len(num)-1)) % 10
    return check if 0 <= check < 10 else ""
​
​
def is_isbn13(num):
    return 10 - sum(1 * int(num[i]) if i % 2 == 0 else 3 * int(num[i]) for i in range(len(num)-1)) % 10 == int(num[-1])
​
​
def isbn13(txt):
    if len(txt) == 13:
        return "Valid" if is_isbn13(txt) else "Invalid"
    if is_isbn10(txt):
        check = check_digit("978" + txt)
        if check != "":
            if is_isbn13("978" + txt[:-1] + str(check)):
                return "978" + txt[:-1] + str(check)
    return "Invalid"

