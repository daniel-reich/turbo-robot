"""


Write a class called `Name` and create the following _attributes_ given a
**first name** and **last name** (as `fname` and `lname`):

  * An attribute called `fullname` which returns the first and last names.
  * A attribute called `initials` which returns the first letters of the first and last name. Put a `.` between the two letters.

Remember to allow the attributes `fname` and `lname` to be accessed
individually as well.

### Examples

    a1 = Name("john", "SMITH")
    a1.fname ➞ "John"
    
    a1.lname ➞ "Smith"
    
    a1.fullname ➞ "John Smith"
    
    a1.initials ➞ "J.S"

### Notes

  * Make sure only the first letter of each name is capitalised.
  * Check the **Resources** tab for some helpful tutorials on Python classes.

"""

class Name:
  
  def __init__(self, fname, lname ):
    self.fname = fname.capitalize()
    self.lname = lname.capitalize()
    self.fullname = self.fname + ' ' + self.lname
    self.initials = self.fname[0] + '.' + self.lname[0]

