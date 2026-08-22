# Math function...
import math
f = 5
print(f'Factorial of {f}! = {math.factorial(f)}')

a = 15
b = 5
print(f'The gcd of {b} and {a} is: {math.gcd(b,a)}');

x = -10
print(f'The absolute value of {x} is: {math.fabs(x)}')
# Logical operator...
has_high_income = False
has_good_credit = True
has_criminal_record = False

#And operator...
if has_high_income and has_good_credit:
    print('Eligible for loan')
else:
    print('Sorry! you are not eligible for loan')

# OR operator...
if has_high_income or has_good_credit:
    print('Eligible for loan');
else:
    print('Not eligible for loan');

if has_good_credit and not has_criminal_record:
    print('Eligible for loan');
    
name = input('Enter your name: ')

if len(name) < 3:
    print('Name must be at least 3 characters');
elif len(name) > 20:
    print('Name can be a maximum of 10 characters');
else:
    print('Name looks good')
    
# weight conversion project...
weight = float(input('Enter your weight: '))
ask_kg_lb = input('(L) bs or (K) kg: ')

if ask_kg_lb == 'k':
    result = weight * 0.4535
    print(f'You are {result:.2f} kg')

elif ask_kg_lb == 'l':
    result = weight/0.4535
    print(f'You are {result:.2f} lbs')

else:
    print('Invalid Choice');
    
# while loop using make a guess game...
secret_num = 9
i = 0
while i<3:
    guess = int(input('Guess: '))
    i += 1
    if guess == secret_num:
        print('You succeded!')
        break;
else:
    print('Timed out!');

# car game...
user_input = ''
started = False
while True:
    user_mess = input('>> ')
    if user_mess == 'start':
        if started:
            print('Car is already started..')
        else:
            started = True
            print('Car started...Ready to go!')

    elif user_mess == 'stop':
        if not started:
            print('Car is already stopped..')
        else:
            started = False
            print('Car is stopped!')

    elif user_input == 'help':
        print('Start - To start the car')
        print('Stop - To stop the car')
        print('Quit - To exit')
        print('Note: must be use loewr case...')

    elif user_mess == 'quit':
        print('The game is Quit!')
        break;
    
    else:
        print("I don't understand!")
# for loop in python..
for item in range(5, 10, 2): # here 3rd index where 2 is represent to the difference between two numbers
    print(item);
