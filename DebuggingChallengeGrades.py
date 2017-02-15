__author__ = 'mcclure'

#This program is supposed to calculate the Semester Grade using the 40-40-20 method. 
# This method calculates semester grade as: 40% (First Nine Weeks Grade Average)
# + 40% (Second Nine Weeks Grade Average) + 20% (Semester Test Grade)


#HINT: Double check the math(calculation) to make sure that the program is printing the
#correct grade. Try using different values for the first and second nine weeks grades also
#to verify that the final semester grade is accurate.


#input first nine weeks grade
#input second nine weeks grade
#input semester test grade 
First9Weeks = 95
Second9Weeks = 90
SemesterTest = 92

#calculate the Semester Grade
SemesterGrade = (First9Weeks * .4) + (Second9Weeks * .4) + (SemesterTest * .2)

#output First Semester Grade 
print("Your Final First Semester Test Grade is: ", SemesterGrade)
