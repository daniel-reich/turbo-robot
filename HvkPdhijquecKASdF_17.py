"""


Create a function that takes a dictionary of student names and returns a list
of student names in **alphabetical order**.

### Examples

    get_student_names({
      "Student 1" : "Steve",
      "Student 2" : "Becky",
      "Student 3" : "John"
    }) ➞ ["Becky", "John", "Steve"]

### Notes

  * Don't forget to `return` your result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def get_student_names(students):
  alph_names=[];
  
  for i in students:
    alph_names.append(students[i]);
    
  alph_names.sort();
  return alph_names;

