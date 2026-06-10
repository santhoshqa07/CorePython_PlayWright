marks = input("Enter marks: ")
Grade = ''
if(int(marks) >= 90 and int(marks) <= 100):
    Grade = "A"
elif(int(marks) >= 80 and int(marks) < 90):
    Grade = "B"
elif(int(marks) >=60 and int(marks) < 80):
    Grade = "C"
elif(int(marks) >=40 and int(marks) < 60):
    Grade = "D"
else:
    Grade = "F"

print("The Grade of the student is:"+Grade)

