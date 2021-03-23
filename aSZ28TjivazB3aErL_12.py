"""


Check if the given string consists of **only letters and spaces** and if every
letter is in **lower case**.

### Examples

    letters_only("PYTHON") ➞ False
    
    letters_only("python") ➞ True
    
    letters_only("12321313") ➞ False
    
    letters_only("i have spaces") ➞ True
    
    letters_only("i have numbers(1-10)") ➞ False
    
    letters_only("") ➞ False

### Notes

  * Empty arguments will always return `False`.
  * Input values will be mixed _(symbols, letters, numbers)_.

"""

def letters_only(s):
  return all([s.replace(" ", "").isalpha(), s.islower()])

