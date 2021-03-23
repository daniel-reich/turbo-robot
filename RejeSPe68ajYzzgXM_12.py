"""


Create a function that, when given a list of individual [finite-state
automaton](https://en.wikipedia.org/wiki/Finite-state_machine) instructions,
generates an FSA in the form described in [this
challenge](https://edabit.com/challenge/86CrsZ2rRMnCsDSza). Each instruction
will be a list of three elements: The first element will be the current state,
the second element will be the input to which the instruction pertains, and
the third element will be the new state.

For example, the instruction `["S0", 1, "S1"]` indicates that, if the current
state is `"S0"`, upon receiving a `1` as input, the new state will be `"S1"`.
A deconstruction of the FSA from [this
challenge](https://edabit.com/challenge/mmiLWJzP3mvhjME7b) can be seen below:

### Examples

    divisible = [
      ["S0", 0, "S0"], ["S0", 1, "S1"],
      ["S1", 0, "S2"], ["S1", 1, "S0"],
      ["S2", 0, "S1"], ["S2", 1, "S2"]
    ]
    
    combine(divisible) ➞ {
      "S0": ["S0", "S1"],
      "S1": ["S2", "S0"],
      "S2": ["S1", "S2"]
    }

### Notes

  * Every FSA will use a binary alphabet.
  * All states will be of the form `Sn`, where `n` is an integer, e.g. `S2`.

"""

def combine(lst):
  
  Details = lst
  Details = sorted(Details)
  
  Draft_One = {}
    
  Batch = []
  Counter = 0
  Length = len(Details)
    
  while (Counter < Length):
        
    Item = Details[Counter]
        
    if (Batch == []):
      Batch.extend(Item)
      Counter += 1
        
    elif (Item[0] == Batch[0]):
      Batch.extend(Item)
      Counter += 1
        
    else:
      Draft_One[Batch[0]] = Batch
      Batch = Item
      Counter += 1
​
  Draft_One[Batch[0]] = Batch
​
  Draft_Two_Keys = []
  Draft_Two_Values = []
    
  for x,y in Draft_One.items():
    Draft_Two_Keys.append(x)
    Draft_Two_Values.append(y)
​
  Counter = 0
  Length = len(Draft_Two_Values)
    
  while (Counter < Length):
        
    Item = Draft_Two_Values[Counter]
    First = Item[2]
    Second = Item[5]
    Revised = []
    Revised.append(First)
    Revised.append(Second)
    Draft_Two_Values[Counter] = Revised
    Counter += 1
        
  Dictionary = {}
    
  Counter = 0
  Length = len(Draft_Two_Values)
    
  while (Counter < Length):
    Key = Draft_Two_Keys[Counter]
    Value = Draft_Two_Values[Counter]
    Dictionary[Key] = Value
    Counter += 1
    
  return Dictionary

