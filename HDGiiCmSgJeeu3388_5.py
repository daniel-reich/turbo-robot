"""


A fuse melts when a current in an electrical device exceeds the fuse's rating,
breaking the circuit and preventing the heat from building up too much (which
can cause a fire). The ideal fuse to choose is **higher** than the device's
current output, yet **as close as possible** to it as well.

Given a list of _fuse ratings_ , and the _device's current output_ , return
which of the fuses is the best for the device.

### Examples

    choose_fuse(["3V", "5V", "12V"], "4.5V") ➞ "5V"
    
    choose_fuse(["5V", "14V", "2V"], "5.5V") ➞ "14V"
    
    choose_fuse(["17V", "15V", "12V"], "9V") ➞ "12V"

### Notes

  * You will be given three possible ratings in voltage.
  * Fuses may not be in a sorted order.
  * Assume that there is a valid fuse in every test case

"""

def choose_fuse(fuses, current):
    current = "".join(list(current)[:-1])
    if "." in current:
        current = float(current)
    else:
        current = int(current)
​
    number = []
    for i in range(150):
        number.append(i)
    number = [str(i) for i in number]
​
    arr = []
    for i in fuses:
        arr.append(i.split("V"))
​
    arr2 = []
    for i in arr:
        for x in i:
            if x in number and x != "":
                arr2.append(x)
​
    arr2 = [int(i) for i in arr2]
    arr2.append(current)
    s = sorted(arr2)
​
    arr3 = s
    arr3 = [str(i) for i in arr3]
    for i in range(len(arr3)):
        arr3.append(arr3[i] + "V")
​
    answer = arr3[-3:]
​
    return answer[s.index(current)]

