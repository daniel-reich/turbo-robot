"""


Your task is to write a program which allows teachers to create a _multiple
choice test_ in a class called `Testpaper` and to be also able to assign a
_minimum pass mark_. The testpaper's subject should also be included. The
attributes are in the following order:

  1. `subject`
  2. `markscheme`
  3. `pass_mark`

As well as that, we need to create student objects to take the test itself!
Create another class called `Student` and do the following:

  * Create an attribute called `tests_taken` and set the default as `'No tests taken'`.
  * Make a method called `take_test()`, which takes in the testpaper object they are completing and the student's answers. Compare what they wrote to the mark scheme, and **append to the/create a** dictionary assigned to `tests_taken` in the way as shown in the point below.
  * Each key in the dictionary should be the _testpaper subject_ and each value should be a string in the format seen in the examples below ( _whether or not the student has failed, and their percentage in brackets)_.

### Examples

    paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
    paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
    paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")
    
    student1 = Student()
    student2 = Student()
    student1.tests_taken ➞ "No tests taken"
    student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
    student1.tests_taken ➞ {"Maths" : "Passed! (80%)"}
    
    student2.take_test(paper2, ["1C", "2D", "3A", "4C"])
    student2.take_test(paper3, ["1A", "2C", "3A", "4C", "5D", "6C", "7B"])
    student2.tests_taken ➞ {"Chemistry" : "Failed! (25%)", "Computing" : "Failed! (43%)"}

### Notes

  * Round percentages to the **nearest whole number**.
  * Remember that the attribute `tests_taken` should return 'No tests taken' when no tests have been taken yet.

"""

class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
​
class Student:
    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken = tests_taken
​
    def take_test(self, paper, student_ans):
        markscheme_dict = to_dict(list(paper.markscheme))
        student_ans_dict = to_dict(list(student_ans))
        subject, result = calc_report(student_ans_dict, markscheme_dict, paper.pass_mark, paper.subject)
        if self.tests_taken == 'No tests taken':
            self.tests_taken = {subject: result}
        else:
            self.tests_taken.update({subject: result})
​
​
def calc_report(student_ans_dict, markscheme_dict, pass_mark, subject):
    right = 0
    wrong = 0
    for i in student_ans_dict.keys():
        if student_ans_dict[i] == markscheme_dict[i]:
            right += 1
        else:
            wrong += 1
    percent = int(round((right / (len(markscheme_dict)) * 100), 0))
    int_pass_mark = int(pass_mark[:-1])
    if percent >= int_pass_mark:
        status = 'Passed!'
    else:
        status = 'Failed!'
​
    percent_str = '({}%)'.format(str(percent))
    result = '{} {}'.format(status, percent_str)
    return subject, result
​
​
def to_dict(ls):
    # ls = ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A']
    d = {}
    for item in ls:
        ques = item[0:len(item) - 1]
        ans = item[-1]
        d[ques] = ans
    return d

