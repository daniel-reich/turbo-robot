"""


Create a function that takes a list of student dictionaries and returns a list
of their top notes. If the student does not have notes then let's assume their
top note is equal to 0.

### Examples

    get_student_top_notes([
      {
        "id": 1,
        "name": "Jacek",
        "notes": [5, 3, 4, 2, 5, 5]
      },
      {
        "id": 2,
        "name": "Ewa",
        "notes": [2, 3, 3, 3, 2, 5]
      },
      {
        "id": 3,
        "name": "Zygmunt",
        "notes": [2, 2, 4, 4, 3, 3]
      }
    ]) ➞ [5, 5, 4]

### Notes

N/A

"""

def get_student_top_notes(lst):
    l1 = []
    for a in lst:
        if a['notes']:
            l1.append(max(a['notes']))
        else:
            l1.append(0)
    return l1

