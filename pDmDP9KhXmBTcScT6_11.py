"""


Create a function that takes an email address and returns the name in the
address.

  * The "name" is the **letters/alphabetical characters** before the @ in the address.
  * The "name" will not always be an actual name.
  * Email addresses will end in something like `@domain.com`

### Examples

    get_name("yourname@example.com") ➞ "yourname"
    
    get_name("john64@gmail.com") ➞ "john"
    
    get_name("pamela78_Cole@hotmail.com") ➞ "pamelaCole"
    
    get_name("Chickenlololol29@yahoo.com") ➞ "Chickenlololol"

### Notes

  * Keep the original capitalization in the email address.
  * All email addresses are purely made-up. It is a coincidence if any of the test email addresses actually exists.

"""

def get_name(address):
    name_with_numbers = []
    doContinue = False
    for char in address:
        if doContinue:
            continue
        elif char == '@':
            doContinue = True
        else:
            name_with_numbers.append(char)
        complete_name = ''
    for item in name_with_numbers:
        if item.isalpha():
            complete_name += item
    return complete_name

