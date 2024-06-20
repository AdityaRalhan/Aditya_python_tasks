# take an input from the user the factorial of a number if the user enters a string print not a valid input

fact = 1
number = input('Enter a number : ')

if number.isdigit():
    number = int(number)
    for i in range(1,number+1):
        fact *= i
   
    print(f'Factorial is : {fact}')

else: 

    print('Invalid input ')
    

    