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

moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
    if not pin.isdigit() or len(pin)<4:
        return "Invalid input."
    else:
        return [moves[(int(num)+i)%len(moves)] for i,num in enumerate(pin)]

