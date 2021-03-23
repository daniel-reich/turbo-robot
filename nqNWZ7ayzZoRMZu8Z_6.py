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
    ans = []
    for d in students:
        if len(d["notes"]) > 0:
            ans.append({"name": d["name"], "avgNote": int(round(sum(d["notes"]) / float(len(d["notes"])), 0))})
        else:
            ans.append({"name": d["name"], "avgNote": 0})
    return ans

