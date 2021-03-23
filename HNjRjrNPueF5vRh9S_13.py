"""


The **Hamming Code** is used to correct errors in data transmissions. Create a
function that takes a string containing the `message` and returns an encoded
message using hamming code.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    hamming_code("hey") ➞
    "000111111000111000000000000111111000000111000111000111111111111000000111"

 **Step 1:** Convert every character to its ASCII value:

    h, e, y = 104, 101, 121

 **Step 2:** Convert ASCII values to 8-bit binary:

    104, 101, 121 = 01101000, 01100101, 01111001

 **Step 3:** Triple every bit:

    01101000, 01100101, 01111001 =
    
    000111111000111000000000, 000111111000000111000111, 000111111111111000000111

 **Step 4:** Concatenate the result:

    "000111111000111000000000000111111000000111000111000111111111111000000111"

See the below examples for a better understanding:

### Examples

    hamming_code("hey") ➞
    "000111111000111000000000000111111000000111000111000111111111111000000111"
    
    hamming_code("mubashir") ➞
    "000111111000111111000111000111111111000111000111000111111000000000111000000111111000000000000111000111111111000000111111000111111000111000000000000111111000111000000111000111111111000000111000"
    
    hamming_code("matt") ➞
    "000111111000111111000111000111111000000000000111000111111111000111000000000111111111000111000000"

### Notes

N/A

"""

def hamming_code(message):
    list = []
    hamming = ""
    for i in range(len(message)):
        list.append(bin(ord(message[i]))[2:].zfill(8))
    for i in range(len(list)):
        for j in range(8):
            hamming = hamming+str(list[i][j])+str(list[i][j])+str(list[i][j])
    return hamming

