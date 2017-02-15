### Logic Errors
Logic or semantic errors can potentially be the hardest to identify since they are not recognized as errors by the compiler. The program is written “correctly” without syntax errors, but the correct output is not produced. This type of error usually does not produce any specific error message, but instead causes your program to behave incorrectly. These types of errors can be tricky to track down.  Most commonly, these errors are caused by accidentally using one variable in a place where a different variable is intended, or by simply doing some math incorrectly. 

Consider the example program on the left of your screen. The example "should" calcuate the average of the two numbers the user enters. But, because of the order of operations in arithmetic (the division is evaluated before addition) the program will not give the right answer. 
Press the button below to run the code.


{Run}(python3 logic-error-1.py)

Notice that we did not get any sort of error message or warning when we ran our code, however, we know that 4 is not the correct answer to the average of the two numbers and instead the correct answer is 3.

|||challenge
## Fix the bug!
To rectify this problem, we will simply add the parentheses to line 5 of our program: 
z = **(**x+y**)**/2

Click run to verify that your program gives the correct average of 3.

|||
