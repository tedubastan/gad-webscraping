# def a(nr_1, nr_2):
#     return nr_1 + nr_2
#
#
# print('--- id(a)', id(a))
# print('--- id(lambda)', id(lambda nr_1, nr_2: nr_1 + nr_2))
#
# my_sum_from_a = a(5, 7)
# print('--- id(a)', id(a))
# print('--- id(lambda)', id(lambda: 2))
# my_sum_from_lambda = (lambda nr_1, nr_2: nr_1 + nr_2)(5, 7)
# print('--- id(a)', id(a))
# print('--- id(lambda)', id(lambda nr_1, nr_2: nr_1 + nr_2))
# print('--- id(lambda)', id(lambda: 6))
#
# print('my_sum_from_a', my_sum_from_a)
# print('--- id(a)', id(a))
# print('my_sum_from_lambda', my_sum_from_lambda)
# print('--- id(a)', id(a))
#
# # # other complex code
# # # ...
# # # ...


students = [{
    'name': 'Student 1',
    'grade': 7.20,
}, {
    'name': 'Student 2',
    'grade': 7.90,
}, {
    'name': 'Student 3',
    'grade': 5.40,
}, {
    'name': 'Student 4',
    'grade': 5.40,
}, {
    'name': 'Student 5',
    'grade': 10.00,
}, {
    'name': 'Student 6',
    'grade': 3.20,
}, {
    'name': 'Student 3',  # student_name = ['Student', '3']
    'grade': 1.20,
}]

students.sort(key=lambda student_item: student_item['grade'], reverse=True)
# print('students', students)


def split_name(student):
    student_name = student['name'].split(' ')  # will be a list of items

    return {
        'first_name': student_name[0],
        'last_name': student_name[1],
        'grade': student['grade']
    }

# aux_students = []
# for student in students:
#     aux_students.append(split_name(student))
# students = aux_students


# students = list(map(split_name, students))
# print('students', students)


# numbers = (1, 2, 3, 4, 5)
# numbers_2 = tuple(map(lambda nr: nr * 2, numbers))  # map returns object of type 'map' (which is iterable)
# numbers_3 = tuple(map(lambda nr: nr ** 2 if nr % 2 == 0 else [1, 2, 3], numbers))
# print('numbers', numbers)
# print('numbers_2', numbers_2)
# print('numbers_3', numbers_3)

# promoted_students = list(filter(lambda student: student['grade'] > 5.00, students))
# print('promoted_students', promoted_students)


# promoted_students = list(
#     filter(
#         lambda student: student['grade'] > 5.00,
#         map(split_name, students)
#     )
# )
# print('promoted_students', promoted_students)

# numbers_1 = (1, 2, 3, 4, 5)
# numbers_2 = tuple(map(lambda nr: nr * 2, numbers_1))
# numbers_3 = tuple(map(lambda nr: nr ** 2, numbers_1))

# zip_object = zip([10, 20, 30, 40, 50, 60, 70], numbers_1, numbers_2, numbers_3)
# print('zip_object', list(zip_object))


# import itertools
# zip_data = itertools.zip_longest([10, 20, 30, 40, 50, 60, 70], numbers_1, numbers_2, numbers_3, fillvalue=True)
# print(list(zip_data))


# students = [split_name(student) for student in students]  # replace map function
# students = [student for student in students if student['grade'] > 5.00]  # replace filter function
# students = [split_name(student) for student in students if student['grade'] > 5.00]  # replace map&filter at once :-o
# print('students', students)

dict_keys = ('a', 'b', 'c', 'd', 'e')
numbers = (1, 2, 3, 4, 5)
# objective: {'a': 1, 'b': 4, 'c': 9 ... }

# my_dict = dict(zip(dict_keys, [nr ** 2 for nr in numbers]))
my_dict = {
    key: value
    for key, value in zip(dict_keys, [nr ** 2 for nr in numbers])
}
print('NEW my_dict', my_dict)
