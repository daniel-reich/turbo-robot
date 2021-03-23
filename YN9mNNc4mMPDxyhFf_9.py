"""


A student learning Python was trying to make a function. His code should
concatenate a passed string `name` with string `"Edabit"` and store it in a
variable called `result`. He needs your help to fix this code.

### Examples

    name_string("Mubashir") ➞ "MubashirEdabit"
    
    name_string("Matt") ➞ "MattEdabit"
    
    name_string("python") ➞ "pythonEdabit"

### Notes

  * Don't forget to return the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def name_string(name):
    b = "Edabit"
    result = name + b
    return result
print(name_string('Mubashir'))
print(name_string('Matt'))
print(name_string('python'))

