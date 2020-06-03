def average():
    score1 = int(input("Input score one "))
    score2 = int(input("Input score two "))
    score3 = int(input("Input score three "))
    average_score = int((score1+score2+score3)/3)
    return average_score




if __name__ == '__main__':
    print(average())

