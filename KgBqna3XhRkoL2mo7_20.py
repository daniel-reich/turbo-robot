"""


Given a string `s` consisting from digits and `#`, translate `s` to English
lowercase characters as follows:

  * Characters ("a" to "i") are represented by ("1" to "9").
  * Characters ("j" to "z") are represented by ("10#" to "26#").

### Examples

    decrypt("10#11#12") ➞ "jkab"
    
    decrypt("1326#") ➞ "acz"
    
    decrypt("25#") ➞ "y"

### Notes

N/A

"""

def decrypt(s):
    result = ''
    if "#" not in s:
        for num in s:
            result += chr(ord("a") + int(num) - 1)
        return result
    left = 0
    right = 1
    while right < len(s):
        if right == len(s) -1:
            if s[right] != "#":
                for j in range(left, right+1):
                    result += chr(ord("a") + int(s[j]) - 1)
                return result
            elif s[right] == "#":
                if right - left >= 3:
                    for j in range(left, right  - 2):
                        result += chr(ord("a") + int(s[j]) - 1)
                    result += chr(ord("j") + int(s[right-2:right]) - 10)
                elif right - left ==2:
                    result += chr(ord("j") + int(s[left:right]) - 10)
                return result
        elif s[right] != "#":
            right += 1
        elif s[right] == "#":
            if right - left >= 3:
                for j in range(left, right-2):
                    result += chr(ord("a") + int(s[j]) - 1)
                result += chr(ord("j") + int(s[right-2:right]) - 10)
            elif right - left == 2:
                result += chr(ord("j") + int(s[right - 2:right]) - 10)
            left = right +1
            right += 1
    return result

