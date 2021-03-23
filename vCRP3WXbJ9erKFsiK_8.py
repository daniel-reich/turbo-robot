"""


It's time to send and receive secret messages.

Create a single function that takes a string **or** a list and returns a coded
or decoded message.

The first letter of the string, or the first element of the list represents
the Character Code of that letter. The next elements are the differences
between the characters: e.g. `A` +3 --> `C` or `z` -1 --> `y`.

### Examples

    dif_ciph("Hello") ➞ [72, 29, 7, 0, 3]
    # H = 72, the difference between the H and e is 29 (upper- and lowercase).
    # The difference between the two l's is obviously 0.
    
    dif_ciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"
    
    dif_ciph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]

### Notes

The input of the function will always be a string **or** a list with numbers.

"""

def cipher(input_arg):
    output = [ord(input_arg[0])]
    for i in range(len(input_arg) - 1):
        output.append(ord(input_arg[i + 1]) - ord(input_arg[i]))
    return output
​
​
def decipher(input_arg):
    result = ''
    current_sum = 0
    for i in range(len(input_arg)):
        current_sum += input_arg[i]
        result += chr(current_sum)
    return result
​
​
def dif_ciph(input):
    if type(input) == list:
        return decipher(input)
    return cipher(input)

