***
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes

***
def is_factorial_number(n):
    if n < 1:
        return False
    
    factorial = 1
    i = 1
    while factorial < n:
        i += 1
        factorial *= i
        
    return factorial == n

# Input reading
number = int(input().strip())

# Check if the number is a factorial number
if is_factorial_number(number):
    print("Yes")
else:
    print("No")
