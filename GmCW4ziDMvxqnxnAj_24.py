"""


Given a dictionary of _student names_ and a list of their _test scores over
the semester_ , return a list of all the students who passed the course ( _in
alphabetical order_ ). However, there is one more thing to mention: **the pass
mark is 100% in everything!**

###  Examples

    who_passed({
      "John" : ["5/5", "50/50", "10/10", "10/10"],
      "Sarah" : ["4/8", "50/57", "7/10", "10/18"],
      "Adam" : ["8/10", "22/25", "3/5", "5/5"],
      "Barry" : ["3/3", "20/20"]
    }) ➞ ["Barry", "John"]
    
    who_passed({
      "Zara" : ["10/10"],
      "Kris" : ["30/30"],
      "Charlie" : ["100/100"],
      "Alex" : ["1/1"]
    }) ➞ ["Alex", "Charlie", "Kris", "Zara"]
    
    who_passed({
      "Zach" : ["10/10", "2/4"],
      "Fred" : ["7/9", "2/3"]
    }) ➞ []

### Notes

  *  **All** of a student's test scores must be _100%_ to pass.
  * Remember to return a list of student names _alphabetically_.

"""

def who_passed(d):
    pas=[]
    for key, value in d.items():
        if all([eval(x)==1.0 for x in d[key]]):
            pas.append(key)
    return sorted(pas)

