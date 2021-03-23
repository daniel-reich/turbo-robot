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
  new_list = []
  for i in students:
    new_list.append(i["notes"])
  together = []
  valid = [1, 2, 3, 4, 5]
  for i in new_list:
    for x in i:
      if x in valid:
        together.append(x)
  uniq = []
  for i in together:
    if i not in uniq:
      uniq.append(i)
  distribution = {}
  for i in uniq:
    distribution[i] = together.count(i)
  return distribution

