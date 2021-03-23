"""


Create a function that returns the selected **filename** from a path. Include
the **extension** in your answer.

### Examples

    get_filename("C:/Projects/pil_tests/ascii/edabit.txt") ➞ "edabit.txt"
    
    get_filename("C:/Users/johnsmith/Music/Beethoven_5.mp3") ➞ "Beethoven_5.mp3"
    
    get_filename("ffprobe.exe") ➞ "ffprobe.exe"

### Notes

  * Tests will include both absolute and relative paths.
  * For simplicity, all paths will include forward slashes.

"""

get_filename = lambda p: p.split('/')[-1]

