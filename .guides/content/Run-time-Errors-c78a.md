### Run-Time Errors
A run-time error is an error that occurs during the execution of a program. These errors indicate problems with the program design. An example of a run-time error is failing to define a variable prior to using it in the program. Each and every variable must be defined in the program before it can be used. If the programmer fails to define a variable, a run-time error will occur. 
We will use the same example program to demonstrate a run-time error. 

Click the link to open the file : [run-time-error-1.py](open_file "run-time-error-1.py")  

{Run}(python3 run-time-error-1.py)

When we run the program we will get a NameError message: name a is not defined. This is because we used the variable "a" in line 7, but did not define the value of variable "a" in the inputs section of our program. 

|||challenge
## Fix the bug!

To correct the error, simply change the letter "a" to "y" in line 7 of our program. We have defined the variable y in line 4 and assigned it a value of 4 and our program should run correctly after this change.

Confirm that you have fixed the bug by clicking Run again.

|||