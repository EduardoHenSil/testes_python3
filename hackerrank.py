from functools import reduce


def get_data():
    avg = average()
    next(avg)
    try:
        avg.send(input())
    except StopIteration as si:
        return si.value


def average():
    student = yield
    student_splited = student.split()
    return student_splited[0], reduce(lambda a, b: float(a) + float(b), student_splited[1:]) / 3


if __name__ == '__main__':
    qtd_students = int(input())
    students = dict([student for student in [get_data() for qtd in range(qtd_students)]])
    choice = input()
    try:
        print('{:.2f}'.format(students[choice]))
    except KeyError:
        pass
