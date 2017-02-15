For the Teacher only. Students will not see this page. 



## Challenge 6.1 Key: 

### Error: 

The Error in this program is actually a logic error.  The program runs correctly and prints out the Grade Average. 
![challenge_6_1_error1.png](https://global-pixel.codio.io/challenge_6_1_error1.png)

However, the average that is printed is not the correct calculation.  The correct average for these grades is 93%. 

The error is in the calculation in line 21: 

![challenge_6_1_error2.png](https://global-pixel.codio.io/challenge_6_1_error2.png)


### Solution:

```
#input first nine weeks grade
#input second nine weeks grade
#input semester test grade 
First9Weeks = 95
Second9Weeks = 93
SemesterTest = 92

#calculate the Semester Grade
SemesterGrade = (First9Weeks * .4) + (Second9Weeks * .4) + (SemesterTest * .2)

#output First Semester Grade 
print("Your Final First Semester Test Grade is: ", SemesterGrade)
```




## Challenge 6.2 Key: 

### Error1: 

![challenge_6_2error2.png](https://global-pixel.codio.io/challenge_6_2error1.png)


### Solution: Missing # 4  in line 13 
```
__author__ = 'mcclure'

#input first nine weeks grade
#input second nine weeks grade
#input semester test grade 
First9Weeks = 95
Second9Weeks = 93
SemesterTest = 92

#calculate the Semester Grade
SemesterGrade = (First9Weeks) * **.4** + (Second9Weeks * .4) + (SemesterTest * .2)

#output First Semester Grade 
print("Your Final First Semester Test Grade is: ", Grade)
```

### Error2:
![challenge_6_2_error2.png](https://global-pixel.codio.io/challenge_6_2_error2.png)


### Solution: Grades variable in Line 14 not defined

There are actually 2 possible solutions for this error.  
1. Change the variable name Grade to SemesterGrade. SemesterGrade is defined on line 11.  **OR:**
2. Change the variable name SemesterGrade on line 11 to Grade. 


||| info
Either of these is a acceptable solution. 
|||



