"""


In **Nico Cipher** , encoding is done by creating a numeric key and assigning
each letter position of the message with the provided key.

Create a function that takes two arguments, `key` and `message`, and returns
the **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "mubashirhassan"
    key = "crazy"
    
    nico_cipher(message, key) ➞ "bmusarhiahass n"

 **Step 1:** Assign numbers to sorted letters from the key:

    "crazy" = 23154

 **Step 2:** Assign numbers to the letters of the given message:

    2 3 1 5 4
    ---------
    m u b a s
    h i r h a
    s s a n

 **Step 3:** Sort columns as per assigned numbers:

    1 2 3 4 5
    ---------
    b m u s a
    r h i a h
    a s s   n

 **Step 4:** Return encoded message **Rows-wise** :

    eMessage = "bmusarhiahass n"

### Examples

    nico_cipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"
    
    nico_cipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "
    
    nico_cipher("iloveher", "612345") ➞ "lovehir    e"

### Notes

Keys will have alphabets or numbers only.

"""

def message_to_matrix(message, key_lenght):
    matrix = []
    i = 0
    while i < len(message):
        matrix_row = []
        for _ in range(key_lenght):
            try:
                matrix_row.append(message[i])
            except:
                matrix_row.append(' ')
            i += 1
        matrix.append(matrix_row)
    return matrix
​
​
​
​
def nico_cipher(message, key):
    key_list = list(key)
    key_sort_list = sorted(key_list)
    key_num_list = []
    key_count_dict = dict()
    for letter in key_list:
        for i in range(len(key_sort_list)):
​
            if letter == key_sort_list[i]:
                if letter not in key_count_dict:
                    key_count_dict[letter] = 0
                else:
                    key_count_dict[letter] += 1
                key_num_list.append(i + key_count_dict[letter])
                break
    matrix = message_to_matrix(message, len(key))
    message_new = ''
    for row in range(len(matrix)):
        for i in range(len(key_num_list)):
            for j in range(len(key_num_list)):
                if i == key_num_list[j]:
                    message_new += matrix[row][j]
    return message_new

