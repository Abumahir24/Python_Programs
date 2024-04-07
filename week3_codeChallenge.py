#Large Power........01
"""Create a method that tests whether the result of taking the power of one number 
to another number provides an answer which is greater than 5000. 
We will use a conditional statement to return True if the result is greater than 5000 or 
return False if it is not"""

def large_power(base, exponent):
    result = base ** exponent
    if result>5000: 
        print("True")
    else:
        print("False")

#calling the function
large_power(550, 60)

#Division by Ten.........02
"""Create a function that determines whether or not a number is divisible by ten. 
A number is divisible by ten if the remainder of the number divided by 10 is 0
"""
def divisible_by_ten(num):
    result=num%10
    if result==0:
        print('True')
    else:
        print('False')
divisible_by_ten(20)
