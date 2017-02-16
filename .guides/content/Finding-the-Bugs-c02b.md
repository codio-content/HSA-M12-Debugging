## Finding the Bugs

Python will attempt to highlight the offending line in your program, or source code. You should use this location as a hint for where to start looking for your problem. First check the area highlighted. Then check the entire line. Lastly, check the line or lines before the line highlighted. The location marked is where Python noticed there was a problem, so the actual problem could come before! 
Other useful Tips for identifying errors in your programs are:
#### 1. Setting breakpoints
At various intervals in the code, breakpoints can be set. Breakpoints are triggered when the program reaches the specified line of source code, before it is executed. 
A breakpoint makes your program stop at that point. You can set breakpoints with the break command and its variants. The place where your program should stop can be specified by file and line number or by function name.

Setting a breakpoint will cause the debugger to stop on a given line of code, whenever that code is reached.
Once set, a breakpoint remains in project until removed. Breakpoints can only be set on executable lines of code. Comments, declarations of methods, and empty lines are not valid locations for breakpoints.

By setting a breakpoint, you can then isolate at what point the program is going wrong. 


#### 2. Using a debugger
The debugger that we are using for this course is built into the IDE.  Having a built in debugger is beneficial because it's less productive to spend a lot of time looking for issues when a debugger would easily find little mistakes like typos.
A visual debugger integrated into an IDE, like we are using also gives you convenient access to smart editing and all the other features of the IDE, in a single integrated development environment (hence the name).
    
Debugging is a very important and useful skill to develop.  You will often make mistakes when writing code and a big part of programming is learning the most effective way to identify those mistakes. 

Here's an example program that we will review together. Take a closer look at this program to see if you can spot the error before we run it. 

In the next section we will run this program in the compiler to see exactly where the error has occurred.
