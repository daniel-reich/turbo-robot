"""


Given a dictionary with students and the grades that they made on the tests
that they took, determine which student has the best Test Average. The `key`
will be the student's name and the `value` will be a list of their grades. You
will only have to **return the student's name**. You do not need to return
their Test Average.

### Examples

    get_best_student({
      "John": [100, 90, 80],
      "Bob": [100, 70, 80]
    }) ➞ "John"
    
    # John's avg = 90
    # Bob's avg = 83.33
    
    get_best_student({
      "Susan": [67, 84, 75, 63],
      "Mike": [87, 98, 64, 71],
      "Jim": [90, 58, 73, 86]
    }) ➞ "Mike"

### Notes

All students in a dictionary will have the same amount of test scores. So no
student will have taken more tests than another.

"""

def get_best_student(dic):
    lis = []
    for i in dic.values():
        l = []
        for j in i:
            l.append(j)
        avg = sum(l)//len(l)
        lis.append(avg)
    
    maxavg = max(lis)
    ind = lis.index(maxavg)
        
    l = 0
    for i in dic.keys():
        if(l == ind):
            return i
            break
        else:
            l+=1 
get_best_student({
  "John": [100, 90, 80],
  "Bob": [100, 70, 80]
})

