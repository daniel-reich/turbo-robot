"""


Create a function which takes in an encoded string and returns a dictionary
according to the following example:

### Examples

    parse_code("John000Doe000123") ➞ {
      "first_name": "John",
      "last_name": "Doe",
      "id": "123"
    }
    
    parse_code("michael0smith004331") ➞ {
      "first_name": "michael",
      "last_name": "smith",
      "id": "4331"
    }
    
    parse_code("Thomas00LEE0000043") ➞ {
      "first_name": "Thomas",
      "last_name": "LEE",
      "id": "43"
    }

### Notes

  * The string will always be in the same format: first name, last name and id with zeros between them.
  * `id` numbers will not contain any zeros.
  *  **Bonus:** Try solving this **using** RegEx.

"""

def parse_code(txt):
  names = [word for word in txt.split('0') if word != '']
  return {'first_name':names[0], 'last_name':names[1], 'id': names[2]}

