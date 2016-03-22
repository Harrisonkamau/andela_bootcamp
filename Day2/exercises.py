'''
Define a function called data_type, to take one argument. Compare and return results, based on the argument supplied to the function.
Complete the test to produce the perfect function that accounts for all expectations.

For strings, return its length.
For None return string 'no value'
For booleans return the boolean
For integers return a string showing how it compares to hundred e.g.
For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
For lists return the 3rd item, or None if it doesn't exist
'''



# solutions
def data_type(data):
    if type(data) == bool:
        return data
    elif type(data) == int:
        if data < 100:
            return 'less than 100'
        elif data == 100:
            return 'equal to 100'
        else:
            return 'more than 100'

    elif type(data) == list:
        if len(data) >= 4:
            return data[3]
        else:
            return None
    elif type(data) == str and len(data) != 0:
        return len(data)
    else:
        return 'no value'


student = {
    'name': 'Harrison',
    'langs': ['Python', 'JavaScript', 'PHP'],
    'age': 23
}

'''
Task 1
Create a function add_student that takes a student dictionary as a parameter,
and adds the student in a list of students
'''
# solution
students = []
def add_student(student):
    students.append(student)
#
'''
    Task 2
    Write a function oldest_student that finds the oldest student.
'''
#
def oldest_student(students):
    oldest = 0 # This variable assumes the oldest student is 0 years
    for student in students:
        if student['age'] > oldest:
            oldest = student['age']
    return oldest
student1 = {'name': 'Joy', 'langs': ['Python', 'JavaScript', 'PHP'], 'age': 32}
student2 = {'name': 'Gracie', 'langs': ['Python', 'JavaScript', 'PHP'], 'age': 12}
add_student(student1)
add_student(student2)

print oldest_student(students)

'''
Task 3
Write a function student_lang that takes in a parameter lang and returns a
list containing names of students who know that language.
'''

def student_lang(lang):
    for student in students:
        if lang in student['langs']:
            return student['name']

print student-lang('Python')
