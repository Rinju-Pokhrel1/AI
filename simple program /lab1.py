marks1 = int(input("enter the marks in first subject:"))
marks2 = int(input("enter the marks in second subject:"))
marks3 = int(input("enter the marks in third subject:"))


pass_marks = 33
total_marks_possible = 300
passing_total_percentage = 40
passing_total_marks = total_marks_possible * (passing_total_percentage / 100)

passed_subject1 = marks1 >= pass_marks
passed_subject2 = marks2 >= pass_marks
passed_subject3 = marks3 >= pass_marks


total_marks_obtained = marks1 + marks2 + marks3


passed_total = total_marks_obtained >= passing_total_marks

print("QN.2 Rinju Pokhrel")
final_result = passed_subject1 and passed_subject2 and passed_subject3 and passed_total
  
if final_result:
    print("Congratulations! You have passed.")
else:
    print("Sorry, you have failed. Please try again.")
print("total marks is :",total_marks_obtained)
