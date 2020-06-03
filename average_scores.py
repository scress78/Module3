def average():
    score1 = int(input("Input score one: "))
    score2 = int(input("Input score two: "))
    score3 = int(input("Input score three: "))
    student_average = int((score1+score2+score3)/3)
    return student_average


last_name = input("Input Last Name: ")
first_name = input("Input First Name: ")
age = int(input("Input Age: "))

if __name__ == '__main__':
    average_score = average()

print(f'{last_name}, {first_name} Age: {age} Average Grade: {average_score:.2f}')
