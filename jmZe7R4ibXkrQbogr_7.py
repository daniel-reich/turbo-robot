"""


Write a **regular expression** that checks to see if a password is valid. For
a password to be valid, it must meet the following requirments:

  1. The password must contain at least one uppercase character.
  2. The password must contain at least one lowercase character.
  3. The password must contain at least one number.
  4. The password must contain at least one special character `! ? * #`
  5. The password must be at least 8 characters in length.

### Examples

    "Password*12" ➞ True
    
    "passWORD12!" ➞ True
    
    "Pass" ➞ False

### Notes

  * The lowercase char, uppercase char, special char, and number can appear at any part of the password.
  *  **You will only be writing a regular expression; do not write a function.**

"""

import re
r = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\!\?\*#])(?=.{8})"

