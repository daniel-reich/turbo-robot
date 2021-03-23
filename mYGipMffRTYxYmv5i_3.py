"""


 **Mubashir** needs your help to make a simple equation. Create a function
which takes three numbers: `a`, `b` and `c`, and returns an equation as a
string using simple arithmetic operators `(+, -, *, /)`.

Return any one of the possible answers to pass the tests. If there is no
equation between a,b and c then return `""`.

### Examples

    simple_equation(1, 2, 3) ➞ "1+2=3" or "2+1=3" or "3-2=1" or "3-1=2"
    
    simple_equation(2, 2, 4) ➞ "2+2=4" or "2*2=4" or "4/2=2" or "4-2=2"
    
    simple_equation(6, 2, 3) ➞ "2*3=6" or "3*2=6" or "6/2=3" or "6/3=2"

### Notes

N/A

"""

import itertools
def simple_equation(a,b,c):
    numbers = [a,b,c]
    for eachcombo in itertools.permutations(numbers,2):
        first_num = eachcombo[0]
        second_num = eachcombo[1]
        if c != first_num and c != second_num:
            if first_num + second_num == c:
                return '{}+{}={}'.format(first_num,second_num,c)
            elif first_num - second_num == c:
                return '{}-{}={}'.format(first_num,second_num,c)
            elif first_num * second_num == c:
                return '{}*{}={}'.format(first_num,second_num,c)
            try:
                if first_num // second_num == c:
                    return '{}/{}={}'.format(first_num,second_num,c)
            except Exception as e:
                continue
        elif b != first_num and b != second_num:
            if first_num + second_num == b:
                return '{}+{}={}'.format(first_num,second_num,b)
            elif first_num - second_num == b:
                return '{}-{}={}'.format(first_num,second_num,b)
            elif first_num * second_num == b:
                return '{}*{}={}'.format(first_num,second_num,b)
            try:
                if first_num // second_num == b:
                    return '{}/{}={}'.format(first_num,second_num,b)
            except Exception as e:
                continue
        elif a != first_num and a != second_num:
            if first_num + second_num == a:
                return '{}+{}={}'.format(first_num,second_num,a)
            elif first_num - second_num == a:
                return '{}-{}={}'.format(first_num,second_num,a)
            elif first_num * second_num == a:
                return '{}*{}={}'.format(first_num,second_num,a)
            try:
                if first_num // second_num == a:
                    return '{}/{}={}'.format(first_num,second_num,a)
            except Exception as e:
                continue
    return ''

