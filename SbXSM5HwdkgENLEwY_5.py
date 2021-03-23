"""


Implement a class `Selfie` that can store the current state of the object in
the form of binary string. It can take multiple pictures and then recover to a
state it was before. During testing an object will be provided with new
attributes and their values. It will store its state. Then the values will be
changed. Then it will be given new attributes. It will store its state again.
It will be repeated few times.

Later the states of the object will be recovered given an index. The return
value should be a new _Selfie_ with the requested historic state and the state
history of the new object should be updated with a copy of current object's
state history.

The object also knows how many states it has stored. If the index is not
within the range of stored states, the object stays as is. If the argument is
invalid, `n < 0 or n >= self.n_states()`, the current object (or a copy
thereof) should be returned.

### Examples

    p = Selfie()
    p.x = 2
    p.save_state()
    p.x = 5
    p = p.recover_state(0)
    p.x ➞ 2

### Notes

  * Use of global variables outside the class is not allowed.
  * When an object is restored to a previous state it keeps all saved states.

"""

import re
​
class Selfie:
    def __init__(self):
        self.lst_state = []
​
    def save_state(self):
        state = str(self.__dict__)
        self.lst_state.append(b''.join(ord(s).to_bytes(2, byteorder='big') for s in state))
​
    def recover_state(self, n):
        if n < self.n_states():
            bytes = self.lst_state[n]
            meh = self.lst_state[:]
            fst = ''.join(chr(b) for b in bytes)
            self.__dict__ = eval(''.join(fst[i] for i in range(1, len(fst), 2)))
            self.__dict__['lst_state'] = meh
        return self
​
    def n_states(self):
        return len(self.lst_state)

