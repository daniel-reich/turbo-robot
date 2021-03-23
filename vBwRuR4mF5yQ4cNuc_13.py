"""


Create a function that takes a list of "mostly" numbers, counts the amount of
missing numbers and returns their sum. Watch out for strings!

### Examples

    count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
    # 1+1+1+1
    
    count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4
    
    count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6

### Notes

The data might be dirty! Clean out any filthy strings.

"""

def count_missing_nums(lst):
    mylist = []
    for items in lst:
        try:
            mylist.append(int(items))
        except:
            continue
    mylist.sort()
    missing_items = 0
    start_count = mylist[0]
    end_count=mylist[len(mylist)-1]
    for item in range(start_count, end_count):
        if item in mylist:
            continue
        else:
            missing_items +=1
    return missing_items

