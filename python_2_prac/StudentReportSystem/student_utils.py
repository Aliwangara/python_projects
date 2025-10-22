

def calculate_average(marks):
    return sum(marks)/len(marks)


def get_grade(average):
    if average >= 80:
        return  "A"
    elif average >=70 and average<=79:
        return "B"
    elif average >=60 and average<=69:
        return "C"
    elif average >= 50 and average <= 59:
        return "D"
    else:
        return "E"

