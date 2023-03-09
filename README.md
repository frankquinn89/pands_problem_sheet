# Andrew, we spoke about marking my documentation, research and consistency based on my project assignment and apply that to my problem sheet assignments. See my email from Feb 2nd 2023. I am an experienced coder so may not have much/any references for these tasks.

![image](https://user-images.githubusercontent.com/16778503/219499061-23b8d445-1023-4579-a5e6-9bcf020dda79.png)

# pands_problem_sheet
This is the repo for the weekly taks for the Higher Diploma in Data Analytics.

## How to download this repository

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click to copy the clone URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2.
7. Press Enter. Your local clone will be created.

## How to run the code

1. Make sure you have python v. 3.8 installed. This can be downloaded here from the [anaconda website](https://www.anaconda.com/distribution/).
2. Run command line.
3. Navigate to where you have the files saved in your directory.
4. Type python followed by the file name to run the program. All problems and their corresponding filenames are listed below.

## Tasks
* 
    * [Hello World](#hello-world)
    * [Bank](#bank)
    * [Accounts](#accounts)
    * [Collatz](#collatz)
    * [Weekday](#weekday)
    * [Square root](#square-root)
    * [Es](#es)
----------
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
    
This program just adds the input values and outputs the result.

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

This program looks at the length of the account, reads everything backwards from the last 4 digits and adds an X for each character. Then it just appends the last 4 digits to the X's and outputs the result.

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



Using a while loop we are checking if a number is odd or even. Then using if/else statements,  it's going to do recursive calculations until the value is 1. \
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

    Write a program that outputs a diiferent message depending on if it a weekday or weekend.

This uses the datetime module.

It uses the .weekday() function to return the of the week as an integer. 0-Monday to 6-Sunday.
If result is 0-4 then it is a weekday, otherwise it is the weekend.


<details>
           <summary>How To Run :</summary>
           <p>

Command line :

```
λ python weekday.py
```
If result is Monday-Friday (Week day):
```
Yes, unfortunately today is a weekday
```
If result is Saturday or Sunday (Weekend):
```
It's the weekend, yay!
```
</p>
</details>

----

  ### ***Square root***

    Write a program that takes a positive floating-point number as an input and outputs an 
    approximation of its square root. Do not use existing python squareroot function.
    

# Newton Method
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/

root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1. 

In the above formula, X is any assumed square root of N and root is the correct square root of N. 
Tolerance limit is the maximum difference between X and root allowed. 


Approach: The following steps can be followed to compute the answer:  
1. Assign X to the N itself.
2. Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
3. Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root and continue.
4. If the calculated root comes inside the tolerance allowed then break out of the loop.
5. Print the root.


<details>
           <summary>How To Run :</summary>
           <p>

Command line :

```
λ python squareroot.py
```
```
Enter a positive number: 9.5
```
```
The approximate square root of 9.5 is 3.1
```
There is some validation in place if the user does not input positive number using a while loop to prompt user to try again:
 ```
Enter a positive number: -9
```
 ```

Error! Enter a positive number:
```
</p>
</details>

- - - -

  ### ***Es***

    Write a program that reads in a text file and outputs the number of e's it contains.
    The program should take the filename from an argument on the command line. 
   
Note: I am assuming the user wants to get lower case e's and upper case E's.

This program reads a text file which is passed as an argument in the command line. 
Note: The file must be located in the same directory this program (es.py).

To get a file from command line we need to use sys.argv[1] variable. This is becuase sys.argv[0] would cpature the python file as first varible and try to pass that. sys.argv[1] will take second argument when calling a program.\

The open( filename,'r' ) is used to open and read the file.
I am using .count("e") and .count("E") functions to gather the total amount of the letters.


<details>
           <summary>How To Run :</summary>
           <p>

Sample test.txt file:
#Hello! There should be 6 E's in this file!#
              
              
Command line:

```
λ python es.py test.txt
```

```
The total amount of e/E in test.txt is 6
```
There is validation included to check that user is passing a txt file using a simple .endswith(".txt") function on the filename.

```
λ python es.py test.pdf
```

```
Invalid file type, must be a .txt file
```
</p>
</details>

- - - -
