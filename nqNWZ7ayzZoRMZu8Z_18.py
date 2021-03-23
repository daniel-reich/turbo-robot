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
  ans=[]
  for i in students:
    a=round(sum([j for j in i['notes']])/len(i['notes'])) if i['notes'] else 0
    ans.append({'name':i['name'],'avgNote':a})
  return ans

