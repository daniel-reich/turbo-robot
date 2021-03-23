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

def get_notes_distribution(students):
  notes = {}
  for student in students:
    for value in student['notes']:
      if value in list(range(1,6)):
        try:notes[value] += 1   
        except KeyError: notes[value] = 1
  for note in notes:
    if notes[note] == 0:
      del notes[note]
  return notes

