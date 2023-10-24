

def task_1():
    # Input a Python list of student heights
    student_heights = input().split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    # 🚨 Don't change the code above 👆
    suma=0
    srednia=0
    for student_height in student_heights:
        suma+=student_height
    srednia=round(suma/len(student_heights))
    print(f"total height = {suma}")
    print(f"number of students = {len(student_heights)}")
    print(f"average height = {srednia}")
    # Write your code below this row 👇
#task_1()

def task_2():
    # Input a list of student scores
    student_scores = input().split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])

    # Write your code below this row 👇
    max=0
    for student_score in student_scores:
        if(student_score>max):
            max=student_score
    print(f"The highest score in the class is: {max}")
#task_2()

def lesson():
    for number in range(0,10,3):
        print(number)

def task_3():
    target = int(input()) # Enter a number between 0 and 1000
    # 🚨 Do not change the code above ☝️

    # Write your code here 👇
    suma=0
    for num in range(1,target+1):
        if(num%2==0):
            suma+=num
    print(suma)

#task_3()

def task_4():
    for num in range(1,101):
        if num%3==0 and num%5!=0:
            print("Fizz")
        elif num%5==0 and num%3!=0:
            print("Buzz")
        elif num%3==0 and num%5==0:
            print("FizzBuzz")
        else:
            print(num)
task_4()