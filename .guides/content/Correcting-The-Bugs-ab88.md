We can correct this error in two ways:
1.	Define the variable <b>number4</b> in our code so that the compiler recognizes this variable when it is used in line 8. To do this, we simply add a new line of code within the inputs section of our program below line 5:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	number4 = 6 
 Below the last line of inputs, we can add this new line of code so that our program inputs now look like this:
 
Click the link to open the file : [error-2.py](open_file "error-2.py")

And now when we run the program, the bug is corrected and no error is found. Press the button below to run the code.


{Run}(python3 error-2.py)
 
2.	The second option is to change the variable number4 in our code to one of the variables that we have defined. We can alter line 8 as below:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total = number1 + number2


Click the link to view the corrected program : [error-3.py](open_file "error-3.py")
And when we run the program again with the updated variable, no error is found.
{Run}(python3 error-3.py)

