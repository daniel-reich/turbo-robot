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
    notes = []
    for student in students:
        avgNote = student['notes']
        if avgNote:
            avgNote = sum(avgNote)/len(avgNote)
        else:
            avgNote = 0
        notes.append({"name": student['name'], "avgNote": round(avgNote)})
    return notes

