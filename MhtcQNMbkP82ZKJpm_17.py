"""


Create a function that takes a list of students and returns an dictionary
representing their notes distribution. Have in mind that all invalid notes
should not be count in the distribution. Valid notes are: `1, 2, 3, 4, 5`

### Example

    get_notes_distribution([
      {
        "name": "Steve",
        "notes": [5, 5, 3, -1, 6]
      },
      {
        "name": "John",
        "notes": [3, 2, 5, 0, -3]
      }
    ] ➞ {
      5: 3,
      3: 2,
      2: 1
    })

### Notes

N/A

"""

from collections import Counter
def get_notes_distribution(students):
  print(students)
  students_list_of_lists = [s['notes'] for s in students]
  res = dict(Counter([item for sublist in students_list_of_lists\
  for item in sublist if item in [1,2,3,4,5]]))
  return res

