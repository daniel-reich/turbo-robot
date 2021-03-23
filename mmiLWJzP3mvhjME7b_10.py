"""


Create a function which checks if a binary number is divisible by three by
implementing the following [finite-state
automaton](https://en.wikipedia.org/wiki/Finite-state_machine):

![](https://edabit-challenges.s3.amazonaws.com/500px-
DFA_example_multiplies_of_3.svg.png)

The function should implement the following commands:

  * `0`, `1` ➞ The next digit in the number.
  * `"state"` ➞ The automaton's current state: `"S0"`, `"S1"`, or `"S2"`.
  * `"stop"` ➞ Whether the automaton accepts or rejects the number that's been given. The function should either return `"accept"` or `"reject"`.

### Examples

    divisible(1)(1)(0)(1)(0)("stop") ➞ "reject"
    # 26 is not divisible by 3, and 26 == 0b11010
    
    divisible("state") ➞ "S0"
    # The automaton should start at S0
    
    divisible(1)(0)(1)("state") ➞ "S2"

### Notes

  * The function should be capable of handling arbitrarily long binary numbers.
  * The function will only be fed valid inputs.
  * The function should terminate after a `"state"` or `"stop"` command.
  * In this case, acceptance occurs if the state at termination is `"S0"`, whereas rejection occurs if the state at termination is `"S1"` or `"S2"`.
  * The int function is disabled to prevent conversion from binary to decimal.

"""

def divisible(val):
  state = 'S0'
  if val == 'state':
      return state
  if val == 'stop':
      return 'accept'
​
  if val == 1:
      state = 'S1'
​
  def inner(val):
      nonlocal state
​
      if val == 'state':
          return state
      if val == 'stop':
          if state == 'S0':
              return 'accept'
          else:
              return 'reject'
​
      if state == 'S0' and val == 1:
          state = 'S1'
      elif state == 'S1':
          if val == 0:
              state = 'S2'
          else:
              state = 'S0'
      elif state == 'S2' and val == 0:
          state = 'S1'
​
      return inner
​
  return inner

