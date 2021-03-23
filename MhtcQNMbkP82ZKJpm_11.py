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
​
def get_notes_distribution(students):
    ans = {}
    for student in students:
        C = Counter(student["notes"])
        for note, cnt in C.items():
            if 1 <= note <= 5:
                ans[note] = ans.get(note, 0) + cnt
    return ans

