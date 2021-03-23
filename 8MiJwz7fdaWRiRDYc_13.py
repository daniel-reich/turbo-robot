"""


A number `n` is **apocalyptic** if 2^n contains a string of 3 consecutive 6s
(666 being the presumptive "number of the beast").

Create a function that takes a number `n` as input. If the number is
apocalyptic, find the index of 666 in 2^n, and return `"Repent! X days until
the Apocalypse!"` (X being the index). If not, return `"Crisis averted. Resume
sinning."`.

### Examples

    apocalyptic(109) ➞ "Crisis averted. Resume sinning."
    
    apocalyptic(157) ➞ "Repent! 9 days until the Apocalypse!"
    # 2^157 -> 182687704666362864775460604089535377456991567872
    # 666 at 10th position (index 9)
    
    apocalyptic(175) ➞ "Crisis averted. Resume sinning."
    
    apocalyptic(220) ➞ "Repent! 6 days until the Apocalypse!"

### Notes

N/A

"""

def apocalyptic(n):
    number = pow(2,n)
    number = str(number)
    if len(number) >= 3:
        for i in range(len(number)-3):
            if number[i:(i+3)] == "666":
                return "Repent! " + str(i) + " days until the Apocalypse!"
    return "Crisis averted. Resume sinning."

