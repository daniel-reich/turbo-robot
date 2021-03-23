"""


Given two positive integers `n` and `k`, generate all binaries between the
integers 0 and (2^n) - 1 , inclusives. These binaries will be sorted in
descending order according to the number of existing 1s on it, if there is a
tie, we choose the lowest numerical value. Return the k-th element from the
sorted list created.

For `n = 3` and `k = 5` for exemple, the numbers from 0 to 7 (7 = (2^3) - 1),
make the binary list:

    ["0b0", "0b1", "0b10", "0b11", "0b100", "0b101", "0b110", "0b111"]

When sorted by the rules, we have:

    ["0b111", "0b11", "0b101", "0b110", "0b1", "0b10", "0b100", "0b0"]

And "0b1" is the fifth element on it.

### Examples

    k_th_binary_inlist(3, 5) ➞ "0b1"
    # ["0b111", "0b11", "0b101", "0b110", "0b1", "0b10", "0b100", "0b0"]
    
    k_th_binary_inlist(4, 10) ➞ "0b1010"
    # ["0b1111", "0b111", "0b1011", "0b1101", "0b1110", "0b11", "0b101", "0b110", "0b1001", "0b1010", "0b1100", "0b1", "0b10", "0b100", "0b1000", "0b0"]
    
    k_th_binary_inlist(5, 16) ➞ "0b11100"
    # ["0b11111", "0b1111", "0b10111", "0b11011", "0b11101", "0b11110", "0b111", "0b1011", "0b1101", "0b1110", "0b10011", "0b10101", "0b10110", "0b11001", "0b11010", "0b11100", "0b11", "0b101", "0b110", "0b1001", "0b1010", "0b1100", "0b10001", "0b10010", "0b10100", "0b11000", "0b1", "0b10", "0b100", "0b1000", "0b10000", "0b0"]

### Notes

N/A

"""

def k_th_binary_inlist(n, k):
    bin_list=[bin(x) for x in range (2**n)]
    bin_list.sort(key = number_of_ones, reverse = True)
    return bin_list[k-1]
    
def number_of_ones(x):
    return x.count("1")

