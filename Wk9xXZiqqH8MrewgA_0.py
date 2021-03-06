"""


Write a function that converts a bitmap image of a digital clock (represented
as a string of the form: `hh:mm`) into its representational bit string. A
bitmap image is a by-product of parsing bits (`0`'s and `1`'s) from a canvas
which is basically an image in black on a white background, where `0`
represents the white background and `1` represents the black pixel (it's what
an image is composed of, technically). The general idea of this challenge is
to encode a bitstring that reflects the image of a digital clock (of this
format: `hh:mm`). The images below are basic examples of how these are
conceived.

The clock face shows the time in a black on white background where each
character is three cells wide and five cells deep. Notice there is a space
between the numbers represented by a column of blank cells:

![Time 2135](https://edabit-challenges.s3.amazonaws.com/2-CPZCo90s.png)

![Time 0647](https://edabit-challenges.s3.amazonaws.com/1-JUGyThgYu.gif)

![Time 1859](https://edabit-challenges.s3.amazonaws.com/3-IUPlkMjnHD.png)

Each image is 17 bits wide by 5 bits deep. Each row is encoded as a 17
character string of `1`s and `0`s and the five rows are then concatenated into
an 85 character string. For example, the above image is encoded as follows:

    row 1 = "11100100001110111"
    row 2 = "10101100100010100"
    row 3 = "10100100001110111"
    row 4 = "10100100100010001"
    row 5 = "11101110001110111"
    
    bitmap -> "1110010000111011110101100100010100101001000011101111010010010001000111101110001110111"

Looking at the above rows and examining it carefully, you should be able to
see the clock digits in the pattern of `1`'s. The first three columns show the
number `0`, followed by a column of all `0`s representing a space between the
numbers, then comes another three columns representing the number `1`, then
three columns representing the character `:`, then three columns representing
`3`, a column of zeroes representing a space and finally three columns
representing the number `5`. The resulting time is `01:35`.

### Example

    toBitString("05:44") ??? "1110111000101010110101000101010101101011100011101111010001010001000111101110000010001"
    
    toBitString("12:13") ??? "0100111000010011111000010101100001010011100001001110100100010010000111101110001110111"
    
    toBitString("12:17") ??? "0100111000010011111000010101100001010011100001000010100100010010000111101110001110001"
    
    toBitString("06:46") ??? "1110100000101010010101000101010100101011100011101111010101010001010111101110000010111"

### Notes

This is a reversal of this
[challenge](https://edabit.com/challenge/mQRuBEp8tauB6jaDN) which was
published by @persolut.

"""

def to_bit_string(time):
  bitmap = {"0": [7, 5, 5, 5, 7], "1": [2, 6, 2, 2, 7], "2": [7, 1, 7, 4, 7],
    "3": [7, 1, 7, 1, 7], "4": [5, 5, 7, 1, 1], "5": [7, 4, 7, 1, 7], "6": [4, 4, 7, 5, 7],
    "7": [7, 1, 1, 1, 1], "8": [7, 5, 7, 5, 7], "9": [7, 5, 7, 1, 1], ":": [0, 2, 0, 2, 0]}
  b = [[('00'+bin(s)[2:])[-3:] for s in x] for x in [bitmap[n] for n in time]]
  c = [[(k+'0') if not i else ('0'+k) if i == 4 else k for k in x] for i, x in enumerate(b)]
  return ''.join(''.join(list(x)) for x in zip(*c))

