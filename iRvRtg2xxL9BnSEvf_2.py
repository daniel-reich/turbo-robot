"""


Create a `Person` class which will have _three properties_ :

  * Name
  * List of foods they like
  * List of foods they hate

In this class, create the method `taste()`:

  * It will take in a food name as a string.
  * Return **{person_name} eats the {food_name}**.
  * If the food is in the person's _like list_ , add **'and loves it!'** to the end.
  * If it is in the person's _hate list_ , add **'and hates it!'** to the end.
  * If it is in neither list, simply add an _exclamation mark_ to the end.

### Examples

    p1 = Person("Sam", ["ice cream"], ["carrots"])
    p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
    
    p1.taste("cheese") ➞ "Sam eats the cheese!"
    
    p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

### Notes

  * A person can have an empty list for foods they hate and/or love.
  * Check the **Resources** for some helpful tutorials on Python classes.

"""

class Person:
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate
​
    def taste(self, var):
        a = var in self.like
        b = var in self.hate
        x = {
            (1, 0): " and loves it!",
            (0, 1): " and hates it!",
            (0, 0): "!"
        }[a, b]
        return "{} eats the {}{}".format(self.name, var, x)

