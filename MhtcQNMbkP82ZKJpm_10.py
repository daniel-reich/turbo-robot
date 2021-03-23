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
  valid_notes = [1,2,3,4,5]
  one, two, three, four, five = 0,0,0,0,0
  for i in range(0, len(students)):
    for note in students[i].get("notes"):
      if note == 1:
        one = one + 1
      elif note == 2:
        two = two + 1
      elif note == 3:
        three = three + 1
      elif note == 4:
        four = four + 1
      elif note == 5:
        five = five + 1
  final_dict = {}
  for i in range(0, len(valid_notes)):
    if five > 0:
      final_dict.update({5:five})
    if four > 0:
      final_dict.update({4:four})
    if three > 0:
      final_dict.update({3:three})
    if two > 0:
      final_dict.update({2:two})
    if one > 0:
      final_dict.update({1:one})
  return final_dict

