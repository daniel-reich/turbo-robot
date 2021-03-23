"""


Create a function that takes a list and returns a string.

  *  **0** Repeat the actual decrypted value (using like this : 014 to repeat 14 times). 
    * _Warning: When you start a repeat you can't stop it to add other numbers._
  *  **1, 2, 3, 4** = g, o, l, e
  *  **5** Corresponding to up case of letter before this.
  *  **6** Add a point to the end.
  *  **7** Change case of the first letter.
  *  **8** Reverse the string.
  *  **9** Clear the actual decrypted string.

### Examples

    num_to_google(["12213467"]) ➞ "Google."
    
    num_to_google(["12213467", "321"]) ➞ "Google.log"
    
    num_to_google(["12213467", "321", "122906"]) ➞ "Google.log"
    
    num_to_google(["15", "2502", "15", 3545]) ➞ "GOOGLE"
    
    num_to_google(["15", "2502", "15", 35, 45]) ➞ "GOOGLE"
    
    num_to_google([15, 202, 1, 3, 4]) ➞ "Google"

### Notes

N/A

"""

def num_to_google(lst):
    result = []
    for element in lst:
        element = str(element)
        if "9" in element:
            continue
        for i in range(len(element)):
            if element[i] == "0":
                result.append(result[-1]*int(element[i:]))
                result.pop(-2)
                break
            elif element[i] == "1":
                result.append("g")
            elif element[i] == "2":
                result.append("o")
            elif element[i] == "3":
                result.append("l")
            elif element[i] == "4":
                result.append("e")
            elif element[i] == "5":
                result[-1] = result[-1].upper()
            elif element[i] == "6":
                result.append(".")
            elif element[i] == "7":
                result[0] = result[0].swapcase()
            elif element[i] == "8":
                result = result[::-1]
    return "".join(result)

