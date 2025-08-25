marks = int(input("Enter the student's marks (out of 100): "))


if marks >= 90 and marks <= 100:
    print("Grade: A-")
elif marks >= 80 and marks < 90:
    print("Grade: A")
elif marks >= 70 and marks < 80:
    print("Grade: B+")
elif marks >= 60 and marks < 70:
    print("Grade: B")
elif marks >= 50 and marks < 60:
    print("Grade: c+")
elif marks >=40 and marks <50:
    print("Grade:D")
else:
    print("Grade: F")
