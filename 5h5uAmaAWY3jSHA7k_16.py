"""


A **mountain** is a list with **exactly one peak**.

  * All numbers to the left of the **peak** are increasing.
  * All numbers to the right of the **peak** are decreasing.
  * The peak CANNOT be on the boundary.

A **valley** is a list with **exactly one trough**.

  * All numbers to the left of the **trough** are decreasing.
  * All numbers to the right of the **trough** are increasing.
  * The trough CANNOT be on the boundary.

Some examples of **mountains** and **valleys** :

    Mountain A:  [1, 3, 5, 4, 3, 2]   # 5 is the peak
    Mountain B:  [-1, 0, -1]   # 0 is the peak
    Mountain B:  [-1, -1, 0, -1, -1]   # 0 is the peak (plateau on both sides is okay)
    
    Valley A: [10, 9, 8, 7, 2, 3, 4, 5]   # 2 is the trough
    Valley B: [350, 100, 200, 400, 700]  # 100 is the trough

Neither **mountains** nor **valleys** :

    Landscape A: [1, 2, 3, 2, 4, 1]  # 2 peaks (3, 4), not 1
    Landscape B: [5, 4, 3, 2, 1]  # Peak cannot be a boundary element
    Landscape B: [0, -1, -1, 0, -1, -1]  # 2 peaks (0)

Based on the rules above, write a function that takes in a list and returns
either `"mountain"`, `"valley"`, or `"neither"`.

### Examples

    landscape_type([3, 4, 5, 4, 3]) ➞ "mountain"
    
    landscape_type([9, 7, 3, 1, 2, 4]) ➞ "valley"
    
    landscape_type([9, 8, 9]) ➞ "valley"
    
    landscape_type([9, 8, 9, 8]) ➞ "neither"

### Notes

  * A **peak** is not exactly the same as the **max** of a list. The **max** is a unique number, but a list may have multiple peaks. However, if there exists only one peak in a list, then it is true that the peak = max.
  * See comments for a hint.

"""

def landscape_type(numbers):
    validator = PeekTroughValidator(numbers)
    return validator.validate()
    
class PeekTroughValidator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.max = max(numbers)
        self.min = min(numbers)
        
    def validate(self):
        
        
        try:
            self._validate_peek()
            return 'mountain'
        except ValueError:
            try:
                self._validate_trough()
                return 'valley'
            except ValueError:
                return 'neither'
        
        
​
    def _validate_peek(self):
        
        index = self.numbers.index(self.max)
        self._validate_boundaries(index)
        
        self._validate_side(self.numbers[:index], 'increase')
        self._validate_side(self.numbers[index+1:], 'decrease')
​
    def _validate_trough(self):
        
        index = self.numbers.index(self.min)
        self._validate_boundaries(index)
        
        self._validate_side(self.numbers[:index], 'decrease')
        self._validate_side(self.numbers[index+1:], 'increase')
    
    def _validate_boundaries(self, index):
        if index == 0 or index == len(self.numbers) - 1:
            raise ValueError
    
    def _validate_side(self, list_, type_):
        for index, val in enumerate(list_):
            
            if index == 0:
                pass
            
            elif type_ == 'increase' and val < last_val:
                raise ValueError
​
            elif type_ == 'decrease' and val > last_val:
                raise ValueError
                
            last_val = val

