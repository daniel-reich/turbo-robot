"""


Your friend is trying to write a function that removes all vowels from a
string. They write:

    def remove_vowels(string):
      vowels = "aeiou"
        for vowel in vowels[1]:
          string.replace(vowel, "", 1)
        return string

However, it seems that it doesn't work? Fix your friend's code so that it
actually **does** remove all vowels.

### Examples

    remove_vowels("ben") ➞ "bn"
    
    remove_vowels("hello") ➞ "hllo"
    # The "e" is removed, but the "o" is still there!
    
    remove_vowels("apple") ➞ "appl"
    # The "e" is removed, but the "a" is still there!

### Notes

All letters will be lowercase.

"""

# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
  vowels = "aeiou"
  for i in range(len(vowels)):
    string = string.replace(vowels[i], "")
  return string

