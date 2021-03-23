"""


In this challenge, sort a list containing a series of dates given as strings.
Each date is given in the format `DD-MM-YYYY_HH:MM`:

    "12-02-2012_13:44"

The priority of criteria used for sorting will be:

  * Year
  * Month
  * Day
  * Hours
  * Minutes

Given a list `lst` and a string `mode`, implement a function that returns:

  * if `mode` is equal to `"ASC"`, the list `lst` sorted in ascending order.
  * if `mode` is equal to `"DSC"`, the list `lst` sorted in descending order.

### Examples

    sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ➞ ["10-02-2016_12:30", "10-02-2018_12:15", "10-02-2018_12:30"]
    
    sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ➞ ["10-02-2018_12:30", "10-02-2018_12:15", "10-02-2016_12:30"]
    
    sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ➞ ["01-01-1999_00:55", "09-02-2000_10:03", "10-02-2000_18:29"]

### Notes

  * Remember: the date is in the format `DD-MM-YYYY_HH:MM`.
  * You can expect only valid formatted dates, without exceptions to handle.

"""

def sort_dates(arr, mode):                      # Sort the sort_dates
  """ Given a mode [ascending or descending], sort the times DD-MM-YYYY_HH:MM """
​
  arr = " ".join(arr).replace("_","-").replace(":","-").split()
  for i, x in enumerate(arr):
    arr[i] = x.split("-")
  arr = sorted(sorted(sorted(sorted(sorted(arr, key = lambda x: x[4]), key = lambda x: x[3]), key = lambda x: x[0]), key = lambda x: x[1]), key = lambda x: x[2]) if mode=="ASC" else sorted(sorted(sorted(sorted(sorted(arr, key = lambda x: x[4]), key = lambda x: x[3]), key = lambda x: x[0]), key = lambda x: x[1]), key = lambda x: x[2])[::-1]
  return ["-".join(x[0:3]) + "_" + x[3] + ":" + x[4] for x in arr]

