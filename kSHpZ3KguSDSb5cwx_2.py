"""


Your local bank has decided to upgrade its ATM machines by incorporating
motion sensor technology. The machines now interpret a series of consecutive
dance moves in place of a PIN number.

Create a function that converts a customer's PIN number to its dance
equivalent. There is one dance move per digit in the PIN number. A list of
dance moves is given in the code.

### Examples

    dance_convert("0000") ➞ ["Shimmy", "Shake", "Pirouette", "Slide"]
    
    dance_convert("3856") ➞ [ "Slide", "Arabesque", "Pop", "Arabesque" ]
    
    dance_convert("9999") ➞ [ "Arabesque", "Shimmy", "Shake", "Pirouette" ]
    
    dance_convert("32a1") ➞ "Invalid input."

### Notes

  * Each dance move will be selected from a list by index based on the current digit's value plus that digit's index value. If this value is greater than the last index value of the dance list, it should cycle to the beginning of the list.
  * Valid input will always be a string of four digits. Output will be a list of strings.
  * If the input is not four valid integers, return the string, "Invalid input."

"""

def dance_convert(pin):
    moves = ["Shimmy", "Shake", "Pirouette", "Slide",
             "Box Step", "Headspin", "Dosado", "Pop",
             "Lock", "Arabesque"]
​
    # Invalid input characters!
    invalidInputs = "ABDEFGHIJKLMNOPQRSTUVWXYZ+- abcdefghijklmnopqrstuvwxyz"
​
    # Check the inputs
    if len(list(filter(invalidInputs.__contains__, pin))) >= 1 or len(pin) < 4:
        return "Invalid input."
​
    digitsList = list(map(int, pin))
    result = []
    # Handle the input where all the digits are the same
    wrapAroundIndex = digitsList[0]
    if len(set(digitsList)) == 1:
        for i in range(4):
            numWrapAround = (((wrapAroundIndex - 0)) % len(moves) + 0)
            wrapAroundIndex += 1
            result.append(moves[numWrapAround])
    if len(result) == 4:
        return result
​
    # Normal digits where they are not the same
    for digit in digitsList:
        numWrapAround = (((digit - 0) + digitsList.index(digit)) % len(moves) + 0)
        result.append(moves[numWrapAround])
    return result

