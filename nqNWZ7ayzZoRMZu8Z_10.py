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
  def format_dict(dic):
    name = dic['name']
    try:
      average = float(round(sum(dic['notes']) / len(dic['notes'])))
    except ZeroDivisionError:
      average = 0
    
    return {'name': name, 'avgNote': average}
  
  return [format_dict(dic) for dic in students]

