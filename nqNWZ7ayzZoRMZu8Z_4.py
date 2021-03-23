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
  avg = []
  for i in students:
    if len(i['notes'])>0:
      temp = round(sum(i['notes'])/len(i['notes']))
    else:
      temp = 0
    avg.append({'name':i['name'],'avgNote':temp})
  return avg

