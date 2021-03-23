"""


Create a class that takes the following four arguments for a particular
football player:

  * `name`
  * `age`
  * `height`
  * `weight`

Also, create three functions for the class that returns the following strings:

  * `get_age()` returns "`name` is age `age`"
  * `get_height()` returns "`name` is `height`cm"
  * `get_weight()` returns "`name` weighs `weight`kg"

### Examples

     p1 = player("David Jones", 25, 175, 75)
    
     p1.get_age() ➞ "David Jones is age 25"
     p1.get_height() ➞ "David Jones is 175cm"
     p1.get_weight() ➞ "David Jones weighs 75kg"

#### Notes

`name` will be passed in as a string and `age`, `height`, `weight` will be
integers.

"""

class player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def get_age(self):
        return self.name + " is age " + str(self.age)
    def get_height(self):
        return self.name + " is " + str(self.height) + "cm"
    def get_weight(self):
        return self.name + " weighs " + str(self.weight) +"kg"

