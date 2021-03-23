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
  l=[]
  for x in students:
    d={"name":x["name"]}
    if not x["notes"]:
      d["avgNote"]=0
    else:
      d["avgNote"]=round(sum(x["notes"])/len(x["notes"]),0)
    l.append(d)
  return l

