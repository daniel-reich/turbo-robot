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
  blank = []
  split = current.split('V')
  integer = float(split[0])
  for i in fuses:
    x = i.split('V')
    y = int(x[0])
    blank.append(y)
  blank.append(integer)
  new = sorted(blank)
  index = new.index(integer)
  return str(int(new[index+1]))+'V'

