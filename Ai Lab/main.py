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
    
