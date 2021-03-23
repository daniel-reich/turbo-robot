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

def divisible(arg, S=0):
​
  if S == 0 and arg == 1:
    S = 1
  elif S == 0 and arg == 0:
    S = 0
  elif S == 1 and arg == 0:
    S = 2
  elif S == 1 and arg == 1:
    S = 0
  elif S == 2 and arg == 0:
    S = 1
  elif S == 2 and arg == 1:
    S = 2
​
  def helper(p):
    return divisible(p, S)
    
  if arg == "state":
    return "S{0}".format(S)
  elif arg == "stop":
    if S == 0:
      return "accept"
    else : return "reject"
  else : return helper

