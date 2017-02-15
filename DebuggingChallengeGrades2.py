__author__ = 'mcclure'

#input first nine weeks grade
#input second nine weeks grade
#input semester test grade 
First9Weeks = 95
Second9Weeks = 90
SemesterTest = 92

#calculate the Semester Grade
SemesterGrade = (First9Weeks * .4 ) + (Second9Weeks * .4) + (SemesterTest * .2)

#output First Semester Grade 
print("Your Final First Semester Grade is: ", SemesterGrade)
