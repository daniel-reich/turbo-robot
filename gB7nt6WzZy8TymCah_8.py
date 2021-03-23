"""


Create the _instance attributes_ `fullname` and `email` in the `Employee`
class. Given a person's first and last names:

  * Form the `fullname` by simply joining the first and last name together, separated by a space.
  * Form the `email` by joining the first and last name together with a `.` in between, and follow it with `@company.com` at the end. Make sure _the entire email_ is in **lowercase**.

### Examples

    emp_1 = Employee("John", "Smith")
    emp_2 = Employee("Mary",  "Sue")
    emp_3 = Employee("Antony", "Walker")
    emp_1.fullname ➞ "John Smith"
    
    emp_2.email ➞ "mary.sue@company.com"
    
    emp_3.firstname ➞ "Antony"

### Notes

  * The attributes `firstname` and `lastname` are already made for you.
  * See the **Resources** tab for some helpful tutorials on Python classes!

"""

class Employee:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    self.fullname = self.firstname+" "+self.lastname
    self.email = (self.firstname).lower()+"."+(self.lastname).lower()+"@company.com"
    # Complete the code!

