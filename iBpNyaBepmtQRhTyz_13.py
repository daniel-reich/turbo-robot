"""


The columnar cipher is a transposition cipher that works like this.

Start with a secret message:

    msg = "Meet me by the lake at midnight. Bring shovel."

Transform uppercase letters into lowercase and remove punctuation and spaces:

    msg = "meetmebythelakeatmidnightbringshovel"

Then, pick a keyword made out of distinct letters:

    keyword = "python"

Break up the message into chunks of the same length as the keyword, and write
them in rows under the keyword. Then, number the columns based on the
alphabetised order of the letters in the keyword:

p| y| t| h| o| n  
---|---|---|---|---|---  
m| e| e| t| m| e  
b| y| t| h| e| l  
a| k| e| a| t| m  
i| d| n| i| g| h  
t| b| r| i| n| g  
s| h| o| v| e| l  
4| 6| 5| 1| 3| 2  
  
Read off the enciphered message (ciphertext) from the columns, in the order
specified by the numbers:

    ciphertext = "thaiivelmhglmetgnembaitsetenroeykdbh"

If the message length is not a multiple of the keyword length, fill in each
blank space with "x". For example:

    msg = "Meet me at midnight."
    
    keyword = "python"

p| y| t| h| o| n  
---|---|---|---|---|---  
m| e| e| t| m| e  
a| t| m| i| d| n  
i| g| h| t| x| x  
  
Create a function that takes a string and a keyword. Return the ciphertext if
the string is in plaintext (i.e. broken up into normal English words and
punctuated), or the deciphered message if the string is in ciphertext. The
resulting deciphered message will not have spaces.

### Examples

    c_cipher("Meet me by the lake at midnight. Bring shovel.", "python")
    ➞ "thaiivelmhglmetgnembaitsetenroeykdbh"
    
    c_cipher("meeanbsleyamgioxebltirhxttkihnvxmhedtgex", "monty")
    ➞ "meetmebythelakeatmidnightbringshovelxxxx"
    
    c_cipher("Mission Delta Kilo Sierra has been compromised. Kill Steve. Evacuate", "cake")
    ➞ "ioliiabcrsiteuxmieksrsnpiksecesdaoraemmdlvatxsntleheooelevax"

### Notes

N/A

"""

def c_cipher(msg, keyword):
​
    def decrpyt(msg, keyword):
        list1 = [letter for letter in msg]
        answer = [[] for i in range(0, int(len(msg)/len(keyword)))]
        print("Printing List1: ")
        print(list1)
        print("=" * 20)
​
        # appending items of list1 to list2 structure
        index = 0
        counter = 0
        for digit in list1:
            answer[index].append(digit)
            counter += 1
            if counter % len(keyword) == 0:
                index +=1
​
​
        #create dictionary for keyword
        keyword_list = [i for i in keyword]
        keyword_dict = {}
        keyword_dict = {i:keyword_list.index(i) for i in keyword}
        print(keyword_dict)
​
        # iterate through list2 and add the correct
        sorted_keyword_list = sorted([i for i in keyword])
        print(sorted_keyword_list)
​
​
        column_counter = 0
        row_counter = 0
        for i in list1:
            answer[row_counter][keyword_dict.get(sorted_keyword_list[column_counter])] = i
            row_counter +=1
            if row_counter == len(answer):
                row_counter = 0
                column_counter += 1
​
        final_answer = ""
        for list_item in answer:
            for char in list_item:
                final_answer += char
        print(answer)
        print(final_answer)
        return final_answer
​
​
​
​
​
​
​
​
​
​
​
    def encrypt(msg, keyword):
        import math
        list1 = [letter.lower() for letter in msg if letter.isalnum()]
        print("Printing List1: ")
        print(list1)
        print("=" * 20)
        if len(list1) % len(keyword) != 0:
            digits = int(len(list1) / len(keyword)) + 1
​
        else:
            digits = int(len(list1) / len(keyword))
​
        list2 = [[]for i in range(0,digits)]
​
        # appending items of list1 to list2 structure
        index = 0
        counter = 0
        for digit in list1:
            list2[index].append(digit)
            counter += 1
            if counter % len(keyword) == 0:
                index +=1
​
        print("Printing List1: ")
        print(list2)
        print("=" * 20)
​
​
        #check last list length
        length_list = len(list2[-1])
        if length_list != len(keyword):
            adds = len(keyword) - length_list
            while adds > 0:
                list2[-1].append("x")
                adds -= 1
​
        #create dictionary for keyword
        keyword_list = [i for i in keyword]
        keyword_dict = {}
        keyword_dict = {i:keyword_list.index(i) for i in keyword}
        print(keyword_dict)
​
        # iterate through list2 and add the correct
        answer = ""
        sorted_keyword_list = sorted([i for i in keyword])
        print(sorted_keyword_list)
​
​
        column_counter = 0
        row_counter = 0
        for i in range(0, (len(list2) * len(keyword))):
            answer += list2[row_counter][keyword_dict.get(sorted_keyword_list[column_counter])]
            row_counter +=1
            if row_counter == len(list2):
                row_counter = 0
                column_counter += 1
​
        print(answer)
        return answer
​
​
    if msg.find(" ") >= 0:
        answer = encrypt(msg, keyword)
    else:
        answer = decrpyt(msg, keyword)
​
    return answer

