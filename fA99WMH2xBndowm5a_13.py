"""


Write a **regular expression** that matches a string if and only if it is a
**valid zip code**.

### Examples

    "32554" ➞ True
    
    "92 342" ➞ False
    # Invalid: contains a whitespace
    
    "9@342" ➞ False
    # Invalid: contains a non-numeric character
    
    "923444" ➞ False
    # Invalid: length is not 5

### Notes

  * Zipcodes must be 5 digits long exactly and only contain numbers.
  * Not allowed: non-numeric characters or whitespaces.
  * This challenge is designed to use **Regex only**.

"""

x = r'\d{5}$'

