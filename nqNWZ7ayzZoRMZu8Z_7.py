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
  adict = {}
  newlist = []
  for eachstudent in students:
    adict['name'] = eachstudent['name']
    try:
      adict['avgNote'] = round(sum(eachstudent['notes']) / len(eachstudent['notes']))
    except ZeroDivisionError as zero_err:
      adict['avgNote'] = 0
    newlist.append(adict)
    adict = {}
  return newlist

