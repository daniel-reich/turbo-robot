"""


You have two lists. One shows the names of the people `names`, while the other
shows their occupation `jobs`. Your task is to create a dictionary displaying
each person to their respective occupation.

Person| Job  
---|---  
Annie| Teacher  
Steven| Engineer  
Lisa| Doctor  
Osman| Cashier  
  
### Example

    names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
    jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]
    
    assign_person_to_job(names, jobs) ➞ {
      "Dennis": "Butcher",
      "Vera": "Programmer",
      "Mabel": "Doctor",
      "Annette": "Teacher",
      "Sussan": "Lecturer"
    }

### Notes

  * The two lists have the same length.
  * The index of a name in the `names` list is the same as the index of the person's job in the `jobs` list, as shown in the table above.
  * Check **Resources** for some useful information that can help with this challenge.

"""

def assign_person_to_job(pl, jl):
  return dict(zip(pl,jl))

