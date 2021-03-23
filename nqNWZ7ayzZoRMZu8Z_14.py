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
  res=[{} for _ in range(len(students))]
  for i in range(len(res)):
    res[i]['name']=students[i]['name']
    res[i]['avgNote']=round(sum(students[i]['notes'])/len(students[i]['notes'])) if students[i]['notes'] else 0
  return res

