"""


Create a function that takes an Arabic number and converts it into a Roman
number.

### Examples

    convert_to_roman(2) ➞ "II"
    
    convert_to_roman(12) ➞ "XII"
    
    convert_to_roman(16) ➞ "XVI"

### Notes

  * All roman numerals should be returned as uppercase.
  * The largest number that can be represented in this notation is 3,999.

"""

def convert_to_roman(num):
    place = {
        "0" : ["I","V","X"],
        "1" : ["X","L","C"],
        "2" : ["C","D","M"],
        "3" : ["M"]
        }
        
    answer = ""
    l= []
    for i in str(num) :
        l.insert(0,i)
        
    for i in range(len(l)) :
        if l[i] != "0" and int(i)<3:
            newList = place[str(i)]
            p1,p2,p3 = newList[0],newList[1],newList[2]
            numToRomain = {
                "1" : p1,
                "2" : p1*2, 
                "3" : p1*3,
                "4" : p1+p2,
                "5" : p2,
                "6" : p2+p1,
                "7" : p2+p1*2,
                "8" : p2+p1*3,
                "9" : p1+p3,
            }
            answer = numToRomain[l[i]] + answer
        elif l[i] != "0" and int(i)==3:
            newList = place[str(i)]
            p1 = newList[0]
            numToRomain = {
                "1" : p1,
                "2" : p1*2, 
                "3" : p1*3,
                "4" : p1*4,
            }
            answer = numToRomain[l[i]] + answer
    return answer

