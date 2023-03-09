# Andrew, we spoke about marking my documentation, research and consistency based on my project assignment and apply that to my problem sheet assignments. See my email from Feb 2nd 2023. I am an experienced coder so may not have much/any references for these tasks.

![image](https://user-images.githubusercontent.com/16778503/219499061-23b8d445-1023-4579-a5e6-9bcf020dda79.png)

# pands_problem_sheet
This is the repo for the weekly taks for the Higher Diploma in Data Analytics.

## Tasks
* [Weekly tasks](#weekly-tasks)
    * [Hello World](#hello-world)
    * [Bank](#bank)
    * [Accounts](#accounts)
    * [Collatz](#collatz)
    * [Weekday](#weekday)
    * [Square root](#square-root)
    * [Es](#es)

======
### ***Hello World***

    Write a program that displays Hello World! when it is run.

This program uses a print function to display Hello World!



<details>
           <summary>How To Run</summary>
           <p>

Command line :

```
λ python helloworld.py 
```
Output :
```
Hello World!
```

</p>
</details>

- - - -

 ### ***Bank***

    Write a program called bank.py which reads in two money amounts (in cent) and adds the two amounts.
    It should print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount  
    
This program just adds the input vales and outputs the result.

<details>
           <summary>How To Run</summary>
           <p>

Command line :

```
λ python bank.py
```
Output :
```
Enter amount 1 (in cents) : 65
```
```
Enter amount 2 (in cents) : 180
```
```
The sum of 65 cents and 180 cents is : €2.45
```
</p>
</details>

----

### ***Accounts***

    Program to take a string account number as input and output the account number, hiding all characters as X except last 4 characters.
   I have made the assumption that an account number must be at least 5 characters long.

This program looks at the length of the account replaces all characters except the last 4 with X. Then it just appends the last 4 digits to the X's.

<details>
           <summary>How To Run</summary>
           <p>

Command line :

```
λ python accounts.py
```
Output :
```
Enter Account Number: 1234567890
```
```
XXXXXX7890
```
If user enters an account number less than 5, they will get an error and it prompts them to try again using a while loop to validate length:            
```
Enter Account Number: 1234
```
```
Account Number must contain at least 5 characters. Try again:
```
</p>
</details>

----

  ### ***Collatz***
    
    Write a program that asks the user to input any positive integer and outputs the successive 
    values of the following calculation. At each step calculate the next value by taking the 
    current value and, if it is even, divide it by two, but if it is odd, multiply it by three 
    and add one. Have the program end if the current value is one.



Using a *while* loop we are checking if a number is odd or even. Then using if/else statements,  it's going to do recursive calculations until the value is 1. \
The program checks if the number is even using modulus. If remainder is zero, the number is even so the program divides the value by 2. \
If the remainder is odd, we multiply the number by 3 and add 1. 

<details>
           <summary>How To Run</summary>
           <p>
         
Command Line :

```
λ python collatz.py
```
Output :
```
Enter a positive integer: 5
```
```
5 16 8 4 2 1
```

If user does not enter a positive Integer, they are informed and prompted to try again:

```
Enter a positive integer: x
```
```
Error! Enter a positive integer.
Enter a positive integer:
```
</p>
</details>

----























  ### ***Weekday***

    Write a program that outputs whether or not today is a weekday.

For this program it is neccessary to import *datetime* module so we can manipulete date and time.

Even though the Programming and scripting [video](https://web.microsoftstream.com/video/77f26693-82ed-4006-8c22-c61d37e2f77f) gave the initial idea, a little bit of research on [Python documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.now) helped to crack the code.\
There it was found that by implementing *date.weekday()*, where Monday is 0 and Sunday is 6, it can easily be checked, with the help of *if* statement, whether today is weekday or weekend.

It's important to run the program on both the weekday and weekend to get a correct result.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 5-weekday.py
```
This program does not requre any user input, it just outputs the result.
On the weekday result is:
```
Yes, unfortunately today is a weekday.
```
On the weekend result is:
```
It is the weekend, yay!
```
</p>
</details>

----

  ### ***Square root***

    Write a program that takes a positive floating-point number as input and outputs an 
    approximation of its square root.
    You should create a function called sqrt that does this.

Addition to the task: 
    
    The weekly task is trickier than the previous ones but I really suggest you try to crack it.
    You'll find a simple algorithm for the problem if you Google "Newton's method for square roots".
    I really recommend trying to code it up yourself rather than looking at others' implementations.

This program required hours of research. Websites used for research and understandig are [Geeksforgeeks.org](https://www.geeksforgeeks.org/program-for-newton-raphson-method/), [StackOverflow](https://stackoverflow.com/questions/12850100/finding-the-square-root-using-newtons-method-errors), [Hackernoon](https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo), [Math.ubc.ca](https://www.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/), but the most helpfull one was a Youtube video by [Mechtutor com](https://www.youtube.com/watch?v=szQUIRPrAgQ). 

The most challenging part was the understanding how the method works, and the coding after that was just implementing mathematical formulas.

Like in the Collatz task, here I also implemented checking if the user input indeed is the positive floating-point number. This was done with an *if* statement checking if the number was smaller than zero. If it is, number was changed into a postive one using absolute value with the help of *abs()* function.

Function was created with a keyword *def sqrt()*, and later called with the keywords *sqrt(x)*. In the function variable *n* is defined as an initial guess that first iteration equals to the number we want to root (variable *x* that was the user input). Next, *while* loop is checking 2 conditions of convergence. When conditions are no longer true, function returns the value of variable *x*. Function is called when the result is outputed.

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 6-squareroot.py
```
User input :
```
Input positive floating-point number: -20.5
```
In case of putting in a negative integer the program will respond with a message that a number is negative and fix it for the user, giving the output straight away as well:
```
Oops, your input is a negative number. I'm sure it's a mistake.
I'll fix it for you: 20.5
The square root of  20.5 is approx.   4.528
```
</p>
</details>

- - - -

  ### ***Es***

    Write a program that reads in a text file and outputs the number of e's it contains.
    The program should take the filename from an argument on the command line. 

This program reads a text file called by user as an argument in the command line. The requirement is that a requested file is in the same directory (folder) as is this program.

To make that possible *sys* method was imported. Using the *sys.argv[1]* variable, it is defined that the filename is second argument when calling a program ( *sys.argv[0]* is the program we are trying to start ).\
References for this part of program go to [Python documentation](https://docs.python.org/3.8/library/sys.html) and [Geeksforgeeks.org](https://www.geeksforgeeks.org/command-line-arguments-in-python/#sys).

With the *open( filename,'r' )* function we are opening a file that we called in the command line argument, and making it available just for reading.
For counting the lower case letter 'e' the method *count()* was used, and the argument is a string *"e"*. Reference for the *count()* method is [Programiz](https://www.programiz.com/python-programming/methods/string/count).

<details>
           <summary>User point of view</summary>
           <p>

User call of the program is :

```
λ python 7-es.py moby-dick.txt
```

Output is simply the number of letter "e" in the called file :

```
116960
```
</p>
</details>

- - - -
