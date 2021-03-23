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

def isbn13(txt):
    if len(txt) == 10:
        if not divisible_by_eleven(multiply_isbn10(txt)):
            return 'Invalid'
        else:
            txt = '978' + txt
            txt = txt[:-1] + '0'
            while not divisible_by_ten(multiply_isbn13(txt)):
                txt = str(int(txt)+1)
            return txt
    elif len(txt) == 13:
        if divisible_by_ten(multiply_isbn13(txt)):
            return 'Valid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'
​
def multiply_isbn10(number):
    total = 0
    number = str(number)
    for count, num in enumerate(number):
        if num == 'x' or num == 'X':
            num = 10
        total += int(num) * isbn_10_keys[count+1]
    return total
​
def multiply_isbn13(number):
    total = 0
    number = str(number)
    for count, num in enumerate(number):
        total += int(num) * isbn_13_keys[count+1]
    return total
​
def divisible_by_ten(number):
    if int(number) % 10 == 0:
        return True
    return False
​
def divisible_by_eleven(number):
    if int(number) % 11 == 0:
        return True
    return False
​
isbn_10_keys = {1:10, 2:9, 3:8, 4:7, 5:6, 6:5, 7:4, 8:3, 9:2, 10:1}
isbn_13_keys = {1:1, 2:3, 3:1, 4:3, 5:1, 6:3, 7:1, 8:3, 9:1, 10:3, 11:1, 12:3, 13:1}
​
print(isbn13('031606652X'))

