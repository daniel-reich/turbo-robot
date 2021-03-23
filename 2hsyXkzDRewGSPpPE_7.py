"""


Create a function that returns a base-2 (binary) representation of a base-10
(decimal) string number. To convert is simple: ((2) means base-2 and (10)
means base-10) 010101001(2) = 1 + 8 + 32 + 128.

Going from right to left, the value of the most right bit is 1, now from that
every bit to the left will be x2 the value, value of an 8 bit binary numbers
are (256, 128, 64, 32, 16, 8, 4, 2, 1).

### Examples

    binary(1) ➞ "1"
    # 1*1 = 1
    
    binary(5) ➞ "101"
    # 1*1 + 1*4 = 5
    
    binary(10) ➞ "1010"
    # 1*2 + 1*8 = 10

### Notes

  * Numbers will always be below 1024 (not including 1024).
  * The strings will always go to the length at which the most left bit's value gets bigger than the number in `decimal`.
  * If a binary conversion for `0` is attempted, return `"0"`.

"""

#edabit
#convert number to base 2
​
def binary(num):
    if num == 0:
        return str(num)
    else:
        binary_string = '' #empty string variable to hold the binary expression.
        while num >= 1: #while loop to test if the given number is greater than 1.
            binary_string += str(num%2) #add the remainder of a division by two calculation to the binary_string variable.
            num = num // 2 #floor divide the number by 2.
    return binary_string[::-1] #reverse the order of the binary_string variable.
​
def main():
    pass
​
if __name__ == "__main__":
    main()

