"""


Create a function that takes a list of dictionary like `{ name: "John", notes:
[3, 5, 4]}` and returns a list of dictionary like `{ name: "John", avgNote: 4
}`. If student has no notes (an empty array) then `avgNote` is zero.

### Examples

    [
      { name: "John", notes: [3, 5, 4]}
    ] ➞ [
      { name: "John", avgNote: 4 }
    ]

### Notes

Round the `avgNote` to a whole number.

"""

def avg_note(students):
  result = []
  for student in students:
    if student["notes"] == []:
      result.append({"name":student["name"], "avgNote":0})
      continue
    average = 0
    for score in student["notes"]:
      average += score
    average /= len(student["notes"])
    average = round(average)
    result.append({"name":student["name"], "avgNote":average})
  return result

