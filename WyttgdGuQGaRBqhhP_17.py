"""


Given an _incomplete palindrome_ as a string, return the **minimum letters
needed** to be added on to the **end** to make the string a **palindrome**.

### Examples

    min_palindrome_steps("race") ➞ 3
    # Add 3 letters: "car" to make "racecar"
    
    min_palindrome_steps("mada") ➞ 1
    # Add 1 letter: "m" to make "madam"
    
    min_palindrome_steps("mirror") ➞ 3
    # Add 3 letters: "rim" to make "mirrorrim"

### Notes

Trivially, words which are already palindromes should return `0`.

"""

def min_palindrome_steps(txt):
    txt1 = []
    if len(txt) == 1:
        return 0
    for each in txt[::-1]:
        txt1.append(each)
    else:
        lst = []
        print("txt1 is ", txt1)
        p = 0
        for x in range(0, len(txt) + 1):
            y = 0
            lst_new = []
            try:
                while x-y >= 0 and x+y <= len(txt) and txt1[x + y] == txt1[x - y]:
                    print("x+y is", x+1, "x-y is", x-1, "x is", x, "y is", y)
                    if y == 0:
​
                        y+=1
                    elif y!=0:
                        lst_new.append(txt1[x+y])
                        lst_new.append(txt1[x-y])
                        print("lst_new is", lst_new)
                        y += 1
                if x-y<0 or x+y>len(txt) and y > len(lst) and lst != []:
                    lst = lst_new
                    print(lst)
                    print(len(lst))
                    p = x
            except IndexError:
                continue
            if y > len(lst) and lst != []:
                lst = lst_new
                print(lst)
                print(len(lst))
        if lst == []:
            if txt1[1] == txt1[0]:
                return len(txt)-2
            else:
                print("already paliendrome")
                return len(txt) - 1
        else:
            answer = len(txt) - (len(lst)+1)
            return answer
​
print(min_palindrome_steps("m"))

