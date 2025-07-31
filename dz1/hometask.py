def task1():
    a = int(input("firs number : "))
    b = int(input("second number : "))

    def sum_from_min_to_max(_min,_max):
        i = _min
        while _min < _max:
            i += _min
            _min += 1

    c = 0

    if a < b:
        c = sum_from_min_to_max(a,b)
    elif a > b:
        c = sum_from_min_to_max(b,a)
    else:
        print("you typed two identical numbers : ", a)
    print("sum of all numbers between first and second : ", c)

def task2():
    arr = []
    i = 1
    print("enter a number : ", end = "")
    while True:
        try:
            i = int(input())
        except ValueError:
            break
        arr.append(i)

    arr.sort()

    print("whole typed list")
    for a in arr:
        print(a, end = " ")
    print()

    print("smallest :\t", arr[0],"\n","greatest :\t", arr[-1])

    return None

def task3():
    student_list = [
        #("Имя","Фамилия","[оценки по питону]","[оценки по математике]","посещаемость"),
        ("Mixail",  "Kovalev",    [7,8,5,6,7,7],  [8,8,7],      0.8),
        ("Sofia",   "Kozlova",    [9,7,8,8,9],    [6,7,5,6],    0.65),
        ("Anna",    "Novikova",   [5,6,5,7,5],    [9,8,9,8,10], 0.7),
        ("Alexandr","Melnikov",   [9,10,9,9],     [8,9,9,9],    0.9),
        ("Maria",   "Ivanov",     [3,4,3,3,2],    [3,2,3,5],    0.5),
        ("Artem",   "Smirnov",    [2,3,3,4,2],    [7,8,6,7,7],  0.6)
    ]

    def stud_low_attend(stud):
        if stud[4] < 0.75:
            print("studen with low attendency rate : ", stud[0], stud[1])
        return None
    
    def stud_highest_grade(stud_list):

        av_0 = (sum(stud_list[0][2]) / len(stud_list[0][2]) + sum(stud_list[0][3]) / len(stud_list[0][3])) / 2
        ans = stud_list[0][0] + " " + stud_list[0][0]

        for i in stud_list:
            av = (sum(i[2]) / len(i[2]) + sum(i[3]) / len(i[3])) / 2

            if av_0 < av:
                av_0 = av
                ans = i[0] + " " + i[1]

        return ans
    
    def stud_care_python(stud):
        if (sum(stud[2]) / len(stud[2])) < (sum(stud[3]) / len(stud[3])):
            print(stud[0], stud[1], "need to pay more attention to Python")
        return None
    
    def ui(task_to_do):
        if task_to_do == 1:
            for stud in student_list:
                stud_low_attend(stud)
        elif task_to_do == 2:
            print(stud_highest_grade(student_list))
        elif task_to_do == 3:
            for stud in student_list:
                stud_care_python(stud)
        else:
            print("invalid input")

        return None

    t = int(input("tupe task you want to perform, 1 to 3 :" \
    " print students with low attendancy rate; print best student; scold student with low python marks "))

    ui(t)

    return None

task = int(input("type number of task you want to check, 1 to 3: "))

if task == 1:
    task1()
elif task == 2:
    task2()
elif task == 3:
    task3()