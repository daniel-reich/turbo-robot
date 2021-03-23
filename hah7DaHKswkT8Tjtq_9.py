"""


A numeric string `s` is beautiful if it can be split into a sequence of two or
more positive integers, `a[1]`, `a[2]`, `...a[n]`, satisfying the following
conditions:

  1. `a[i] - a[i-1] = 1` for any `1 < i <= n` (i.e. each element in the sequence is one more than the previous element).
  2. No `a[i]` contains a leading zero. For example, we can split `s = 10203` into the sequence `{1, 02, 03}`, but it is not beautiful because `02` and `03` have leading zeroes.
  3. The contents of the sequence cannot be rearranged. For example, we can split `s = 312` into the sequence `{3, 1, 2}`, but it is not beautiful because it breaks our first constraint (i.e. `1 - 3 ≠ 1`).

Return either `"YES x"` where `x` is the smallest first number of the
increasing sequence or `"NO"` if there is no valid sequence.

### Examples

    separate_numbers("1234") ➞ "YES 1"
    
    separate_numbers("91011") ➞ "YES 9"
    
    separate_numbers("99100") ➞ "YES 99"
    
    separate_numbers("101103") ➞ "NO"
    
    separate_numbers("010203") ➞ "NO"

### Notes

N/A

"""

def separate_numbers(s):
  for size in range (1, int(len(s) / 2)): #goes through all possible sizes of first numbers
    firstNum = ""
    size9 = size + 1  #if all '9's, length of next string + 1
    for i in range (size):
      firstNum += s[i]  #adds all i to currentNum
      if (s[i] != "9"):   #if not all '9's, length of next string is the same
        size9 = size
    remainingDigits = len(s) - size
    print("firstNum:", firstNum)
    latestNum = int(firstNum)
    x = True
    #len(str(latestNum))
    currentIndex = size
    print("Initial currentIndex:", currentIndex)
    while(remainingDigits > 0):
      print("In while loop")
      print("remainingDigits:", remainingDigits)
      currentNum = ""
      print("for i in range(" + str(currentIndex) + ", " + str(currentIndex + size9))
      for i in range(currentIndex, currentIndex + size9): 
        print("i:", i)
        currentNum += str(s[i])
      print("int(currentNum) - latestNum: " + currentNum + " - " + str(latestNum))
      if (int(currentNum) - latestNum != 1):
        print("Breaks while loop")
        x = False
        break
      latestNum = int(currentNum)
      size9 += 1
      for i in str(latestNum):
        if (i != "9"):
          size9 -= 1
          break
      remainingDigits -= len(str(latestNum))
      currentIndex += len(str(latestNum))
      print("currentIndex:", currentIndex)
    if x: 
      return "YES " + str(firstNum)
    print("first for loop done")
  return "NO"

