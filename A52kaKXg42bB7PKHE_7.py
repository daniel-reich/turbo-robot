"""


Write a function that sorts list while keeping the list structure. Numbers
should be first then letters both in ascending order.

### Examples

    num_then_char([
      [1, 2, 4, 3, "a", "b"],
      [6, "c", 5], [7, "d"],
      ["f", "e", 8]
    ]) ➞ [
      [1, 2, 3, 4, 5, 6],
      [7, 8, "a"],
      ["b", "c"], ["d", "e", "f"]
    ]
    
    num_then_char([
      [1, 2, 4.4, "f", "a", "b"],
      [0], [0.5, "d","X",3,"s"],
      ["f", "e", 8],
      ["p","Y","Z"],
      [12,18]
    ]) ➞ [
      [0, 0.5, 1, 2, 3, 4.4],
      [8],
      [12, 18, "X", "Y", "Z"],
      ["a", "b", "d"],
      ["e", "f", "f"],
      ["p", "s"]
    ]

### Notes

Test cases will contain integer and float numbers and single letters.

"""

def num_then_char(sample):
        
    def sortBoth(lst):
        letters = []
        nums = []
        for i in lst:
            if type(i) == int or type(i) == float:
                nums.append(i)
            else:
                letters.append(i)
        output = []
        letters = sorted(letters)
        nums = sorted(nums)
        for num in nums:
            output.append(num)
        for letter in letters:
            output.append(letter)
        return output
    lstCount = 0
    lengths = []
    for lst in sample:
        lstCount += 1
        lengths.append(len(lst))
​
   # print(lstCount, lengths)
​
    # def lstGetter(lst, subsets):
    #     output = []
    #     start = 0
    #     before = 0
    #     for s in subsets:
​
    full = []
    for lst in sample:
        for e in lst:
            full.append(e)
​
    full = sortBoth(full)
    output = []
    for l in lengths:
        lst = []
        for i in range(l):
        # print(i)
            lst.append(full[i])
        output.append(sortBoth(lst))
        #print(output)
        full = full[i + 1:]
    return output

