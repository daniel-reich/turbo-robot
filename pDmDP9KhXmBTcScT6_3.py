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

def get_name(email):
    slovo = ""
    name1 = ""
    name = list(email.split("@"))
    name1 = name[0]
    for character in name1:
        if character.lower() in "abcdefghijklmnopqrstuvwxyz":
            slovo = slovo + character
        else:
            slovo = slovo + ""
    return slovo
​
print(getname("MarkBrull_69@gmail.com"))

