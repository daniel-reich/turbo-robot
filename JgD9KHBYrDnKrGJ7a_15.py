"""


 **Mubashir** is not good in python programming. By mistake, he swapped **keys
and data values** in the dictionary.

Given a dictionary, return a dictionary with the original `values` and the
list of `keys`. See below example for a better understanding:

### Given Dictionary

    dict = {
      "Mubashir": "Name",
      "31": "Age",
      "Male": "Sex",
      "Pilot": "Job",
      "Matt": "Name",
      "40": "Age",
      "Programmer": "Job"
    }

### Modified Dictionary

    dict = {
      "Name": ["Mubashir", "Matt"],
      "Age": ["31", "40"],
      "Sex": ["Male"],
      "Job": ["Pilot", "Programmer"]
    }

### Notes

N/A

"""

def swap_dict(adict):
    empty_dict = {}
    for eachkey in adict:
        empty_dict[adict[eachkey]] = []
    for eachkey in adict:
        empty_dict[adict[eachkey]].append(eachkey)
    return empty_dict

