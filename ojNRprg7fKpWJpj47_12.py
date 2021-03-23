"""


Given a sentence, create a function which shifts the first letter of each word
to the next word in the sentence (shifting right).

### Examples

    shift_sentence("create a function") ➞ "freate c aunction"
    
    shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"
    
    shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"
    
    shift_sentence("edabit") ➞ "edabit"

### Notes

  * The last word shifts its first letter to the first word in the sentence.
  * All sentences will be given in lowercase.
  * Note how single words remain untouched (example #4).

"""

def shift_sentence(txt):
    lst = txt.split(' ')
    arr = []
    for i in lst:
        arr.append(i[0])
​
    arr_new = arr.copy()
    for i in range(len(arr)):
        if i != (len(arr)-1):
            arr_new[i+1] = arr[i]
        else:
            arr_new[0] = arr[i]
    
    print(arr_new)
    result = ''
    count = 0
    for i in arr:
        if count == 0:
            result = result + arr_new[count] + lst[count][1:]
        else:
            result = result + ' ' + arr_new[count] + lst[count][1:]
        count += 1
    
    return result

