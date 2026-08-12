print('Hello world');
print('This is my first python code');

print('Hello world', end =' Hi world');
print ('I am', 25);
# multiline comment use....
"""
This is a comment
written in 
more than just one line
"""
print ('Hi world');

#Write a single-line comment
# This is comment
# Comment out this line so it does not run:
print("This should not run")

# Add a multiline comment
"""
a multiline 
comment
"""
# type conversion...
x = 5;
y = str(x);
print (type(x), type(y));

# Many values to multiple variables..
x, y, z = 'Bangladesh', 'Palestine', 'South Korea';
print(x, y, z);

x = y = z = 'All are countries';
print(x);

# Unpack a collection...
country = ['Bangladesh', 'Palestine', 'South Korea'];
x, y, z = country;
print (x, y, z);
#Global variable...
x = 'awesome';
def myFunction ():
    print('Python is ', x);
myFunction();

a = 'python world';
def globalVariable():
    a = 'fantastic';
    print('This is a ', a);
globalVariable();
print('This is ', a);
# Global variable keyword...
a = 'awesome';
def myFunc():
    global a
    a = 'fantastic';
myFunc();
print('Python is ', a);
# python data type..
#complex type.
x = 1+2j; 
print(type(x));

#list type..
x = ['Bangladesh', 'Palestine', 'Korea'];
print(type(x));

#tuple type..
x = ('Bangladesh', 'Palestine', 'Korea')
print(type(x));

#range type
x = range(10);
print(x);
print(list(x));

#dict type..
x = {'name: ' : 'Nazib', 'age': 23 };
print(type(x));

#set, frozenset type..
x = {'Bangladesh', 'Palestine', 'Korea'};
print(type(x));

x = frozenset({'apple', 'banana', 'orange'})
print(type(x));

#bytes, bytearray, memoryview type
x = bytes(range(10, 15)); 
x = bytes(5);
a = bytes();
print(a);
# here bytes always carry the ASCII value. 
#Here use 'b' before any str it convert str to bytes str
print(x);
print(type(x));

#NoneType
x = None;
print(type(x));
# number to complex number conversion..
x = 1;
a = complex(x);
print(x,a);

# python doesn't have random() function but built in have random module.
import random;
print(random.randrange(1,50));
# here randrange means random number range(start, end);

# python casting means just conversion like number to float, float to complex etc.
# multiline string in python..
a = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labor et dolor magna aliqua.
""";
print(a);

# looping through a string..
for x in 'Banana':
    print(x);

# check length..
x = 'Bangladesh';
print(len(x));

#check string..
txt = "The best things in life are free";
print("free" in txt, type(txt));
# here txt is a string type but when check str it returns the boolean type.
# use if statement..
txt = "The best things in life are free";
print(txt);
if "use" in txt:
    print("Yes, 'life' is present");
else:
    print('Not present');

# use if not statement..
txt = "The best things in life are free";
print(txt);
if "use" not in txt:
    print("Yes, 'use' is not present");
# Slicing string...
x = 'Hi python';
print(x[3:6]); # here range start 3 to 6 index value will be 3, 4, 5 not 6;

#slice from the start and end..
print(x[:5]);
print(x[3:]);

# Negative indexing...
a = 'Hello python';
print(a[-5:-3]); # it works in reverse....
# String Methods....
a = "Hello python";
print(a.upper());

a = 'Hello w3schools';
print(a.lower());

a = " Hi this is white-space ";
print(a.strip()); #returns Hi this is white-space.

a = 'Hello world';
print(a);
print(a.replace("ello", "i"));

a = "Hello world or universe";
print(a.split("!"));
sentence = "Python is a powerful programming language";
print(sentence.split());

csx_data = "Rahim,25,Dhaka,Bangladesh";
print(csx_data.split(","));

txt = "I love Python programming language very much";
print(txt.split(' ', 3)); # here 3 is represent the index where the total str are return. It's called maxsplit
# BMI calculate...
height = input("Enter your height: ");
weight = input("Enter your weight: ");
bmi = float(weight) / float(height)**2;
print(bmi);
print(type(bmi));
name = "Nazib"
age = 23;
# Argument by position..
print('Hello my name is {name} and I am {age} years old'.format(name = name, age = age));
# Using f-string...
print(f'Hello my name is {name} and I am {age} years old');
# string format..
# It shows an error.
age = 36
txt = "My name is Nazib, I am "+ age;
print(txt);
# put "f" in front of the str and add curly {} as placeholder of variable.
age = 36
txt = f"My name is Nazib, I am {age}"
print(txt);
price = 60
txt = f"The price is {price} dollars."
print(txt);
price = 80
txt = f"This price is {price:.3f} dollars"
print(txt);
# here :.3f means show after dot how many numbers.
# String Methods...
# title-- every 1st word will be capital
text = "Hello python world"
print(text.title());
# swapcase-- convert every word big to small and small to big
text = "Hello pyhtHon World";
print(text.swapcase());
#casefold-- it's will be the lower case.

# Searching and finding string methods...
#find-- find the substring if present return start index number, if not return -1.
text = "Hello python learner"
print(text.find("Nazib"));
print(text.find("learner"));
#index(sub)-- most like find() but if not find then return the value error..
text = "Hello javascript learner"
print(text.index("python"));
print(text.index("learner"));
#count-- how many times are present subs string
text = "python python python"
print(text.count("python"));
#startswith(prefix)-- start fixed string?? return true or false
text = "Let's learn python from w3schools."
print(text.startswith("python"));
print(text.startswith("Let's"));
#endswith(suffix)-- same as the startswith..
# Assignment Operator...
# here "//" is the complete number of division.
x = 10
x//=8
print(x);
y = 10
y = y //9
print(y)
#&=
x = 5
x&=3
print(x);
# |= bit wise OR operation means binary addition.
x = 10
x |= 5
print(x);
# Ternary Operator..
# means one-line condition apply
num = 6;
x = "Weekend!" if num > 5 else "Workday";
print(x);

age = input("Enter your age: ")
result = "Adult" if int(age) >= 18 else "Child Baby";
print(result);
# Logical Operator..
x = 5
print(x > 0 and x < 10); # must be both condition will true

x = 5
print(x < 5 or x >10) # if any one false then both are false

x = 5
print(not(x > 5 and x < 10)); # reverse the and answer..
# answer is false but when use not it will be true.
# List in python
thisList = ["Apple", "Banana", "Cherry"];
print(thisList);
thisList = ["Apple", "Banana", "Cherry", "Banana", "Apple", "Cherry"];
print(thisList);
# allow duplicate values..
print(len(thisList));
list1 = ["Apple", "Banana", "Cherry"]
list2 = [1,2,3,4,5]
list3 = [True, False, False];
print(list1, list2, list3);
listV = ["Bangladesh", 25, True]
print(listV); # contain different data types..
# using list constructor..
thisList = list(("Apple", "Banana", "Cherry"));
print(thisList);
#Add item in the list..
fruits.append("Cherry")
print(fruits);
# remove items from the list..
fruits.remove("Apple");
print(fruits);
# insert item in specific position..
fruits.insert(1, "Strawberries");
print(fruits);
# remove item from the list to specific position
fruits.pop(0);
print(fruits);
# reverse the list...
fruits.reverse();
print(fruits);
# sort Alphabetically..
fruits.append("Apple")
print(fruits)
fruits.sort();
print(fruits);
# reverse sort..
fruits.sort(reverse=True);
print(fruits);
# tuples..
# fruits = ("Apples", "Orange", "Grapes");
# fruit2 = tuple(("Apples", "Orange", "Grapes"));
# print(fruit2);
# fruits[0] = "Banana";
# print(fruits)
# del fruit2;
# print(fruit2)
# create set
fruit = {"Apple", "Orange", "Mango"};
print("Apple" in fruit); # return the boolean value..
# add item to the set
fruit.add('Banana');
print(fruit)
# remove the set
fruit.remove('Mango');
print(fruit);
# Clear the set
fruit.clear();
print(fruit);
# Map---Dictionary
# create Dic..
person = {
    'first_name': 'Nazib',
    'last_name': 'Ul Alam',
    'age': 25
}
print(person);

# dictionary constructor...
person = dict(first_name = 'Nazib', last_name = 'Ul Alam', age = 25);
print(person);

# get value..
get_value = person['first_name'], person['last_name'], person['age'];
print(get_value);

# use get method..
value = person.get('first_name');
print(value);

# add key/value in person object..
person['course'] = "Python Course"
person['department'] = "ICT"
print(person);
print(person.get('course'));
print(person.get('department'));

# get all key and items..
print(person.keys());
print(person.items());

# Copy dict..
person2 = person.copy();
person2['Section'] = 'A';
print(person2);

# remove the item..
del(person2['Section']);
print(person2);
person2.pop('department');
print(person2);

# list of dict...
people = [
    {'name': 'Marce', 'age':25},
    {'name': 'Nazib', 'age': 22}
]
print(people);
print(people[0]['name']);

# if else loop
a = 33
b = 200
if b>a :
    print("b is greater than a");

number = 15
if number > 0 :
    print("The number is positive");

age = int(input("Enter your age: "))
if age >= 18 :
    print("You are an adult")
elif age <18 and age >0:
    print("You are not adult")
else:
    print("You are not exists in the world")
is_logged_in = True
if is_logged_in:
    print("Welcome back!");

# elif loop...
a = 33
b = 33
if b > a:
    print("b is greater then a");
elif a==b:
    print("a and b are equal");

# multiple elif loop..
score = 75
if score >=90:
    print("Grade: A");
elif score >=80:
    print("Grade: A-");
elif score >=70:
    print("Grade: B");
elif score >=50:
    print("Grade: C");
else :
    print("Fail in the exam");
#turnarry operator
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is: ", bigger);

age = int(input("Enter your age: "));
adult = age if age > 18 else "You are under 18"
print("Age is: ", adult);
a = 330
b = 330
print("A") if a!=b else print("=") if a==b else print("B");
# A print korbe na when a!=b hobe, = print korbe when a==b hobe , onnthai print korbe "B"
x = 15
y = 20
max_value = x if x>y else y
print ("Max value: ", max_value);
# logical operator
a = int(input("Enter value a: "));
b = int(input("Enter value b: "));
c = int(input("Enter value c: "));
if a>b and c>a:
    print("Both conditions are True");
else:
    print("Both are not True");
# not operator..
a = 33
b = 200
if not a>b:
    print("a is not greater than b");
else:
    print("b is greater than a");
# combining multiple operator
age = 22
is_student = False
has_discount = True

if (age<18 or age > 65) and not is_student or has_discount:
    print("Discount applied");
else:
    print("Discount not applied");
temp = 25
is_raining = False
is_weekend = True

if (temp < 20 and is_raining) and not is_weekend:
    print("Great day for outdoor activities");
else:
    print("Stay at home");
# nested if..
x = 1
if x>10:
    print("Above ten")
    if x>20:
        print("and also above 20")
    else:
        print("but not above 20");
else:
    print("Less 20");
# multilevel nested if-else
username = "Email" # ""
password = "python123" # ""
is_active = True #False

if username:
    if password:
        if is_active:
            print("Login successful");
        else:
            print("Account is not active");
    else:
        print("Password required");
else:
    print("Username required");

# identity operators...
x = ['apple', 'banana']
y = ['apple', 'banana']
z = x
print(x is z)
print(x is y)
print(x==y);

x = ['apple', 'banana']
y = ['apple', 'banana']
print(x is not y);

x = [1,2,3,4]
y = [1,2,3,4]
x = y # if use this then return the true
print(x==y)
print(x is y);

# Membership operators...
fruits = ["apple", "mango", "orange"]
print("banana" in fruits); # this "is" operator retrun the boolean type

fruits = ["apple", "mango", "orange"]
print("banana" not in fruits);

# this operator also work in string...
txt = "Hello python coder"
print("p" in txt);
print("Python" in txt)
print("r" not in txt);
# Create variables
a = 15
b = 4
# Print modulus
print( a%b);
# Print floor division
print( a // b)
# Print power
print( a** b);
# Add 10 to a
a  = a+10;

# list 
thislist = ["apple", "banana", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# looping using List comprehension...
thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist];
for x in thislist:
    print(x);
thislist = ["Apple", "Banana", "Cherry"]
for i in range(len(thislist)):
    print(thislist[i]);

# While loop..
thislist = ["Bangladesh", "China", "Japan", "Korea"]
while i < len(thislist):
    print(thislist[i])
    i +=1;
# list comprehension
fruit = ["Apple", "Banana", "CHerry", "Kiwi"]
newList = []
for i in fruit:
    if "a" in i or "A" in i:
        newList.append(i)
print(newList);
car = ["Tayota", "BMW", "Akij", "ODDDY"]
newList = [i for i in car if 'a' in i or 'A' in i]
print(newList);
# Create a list
colors = ["red", "green", "blue"]
# Print the first item
print(colors[0]);
# Change the second item to "yellow"
colors[1] = "yellow"
# Add "purple" to the end
colors.append("purple")
# Remove "red"
colors.remove("red")
# Print the list
print(colors)
# Tuple...
thistuple = ("apple", "banana", "cherry");
print(thistuple);
print(len(thistuple))

thisTuple = ("apple", )
print(type(thisTuple))
#NOT a tuple
thisTuple = ("apple")
print(type(thisTuple))

# Tuple consturctor..
thisTuple = tuple(("apple", "banana", "orange"));
print(thisTuple);

# Unpacking Tuple
fruits = ("apple", "banana", "orange")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red);

# Using Asterisk*...
fruits = ("apple", "banana", "cherry", "strawberry", "orange")
(green, blue, *black) = fruits
print(green)
print(blue)
print(black)
# Tuple methods "count & index"....
thisTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 5)
x = thisTuple.count(5);
# count = how many times 5 are present in this tuple.
print(x)
# Create the tuple
fruits = ("apple", "banana", "cherry");
# Print the second item
print(fruits[1]);
# Print the number of items
print(len(fruits));
# Unpack the tuple
(a,b,c) = fruits;
# Print b
print(b);

# python set...
thisSet = {"apple", "banana", "cherry"}
print(thisSet);
# Unchanged 
unChange = {"apple", "banana", "apple", "cherry"}
print(unChange)

# python set use update method...
thisSet = {"Mango", "Orange", "Cherry"}
color = {"Green", "Red", "Blue"}
thisSet.update(color)
print(thisSet)

thisSet.discard("Mango")
print(thisSet)

thisSet.pop()
print(thisSet)

# python join sets
# union, update = add both variable elements...
car = {"BMW", "ODDY", "Tesla"}
japCar = {"Tayota", "Neesan"}
print(car.union(japCar))

#intersection = common element are present in both variable....
fruit = {"Apple", "Mango", "Orange"}
food = {"Burgger", "Pizza", "Chicken fry", "Mango"}
print(fruit.intersection(food))

# difference = it's same as the math subtruction...
set1 = {"apple", "mango", "orange"}
set2 = {"google", "microsoft", "apple"}
print(set1.difference(set2))

# symmetric difference = remove the same element of both variables....
tech1 = {"google", "samsung", "sony"}
tech2 = {"microsoft", "apple", "android", "sony"}
print(tech1.symmetric_difference(tech2))

#python frozenset...
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x));

# python Dictionaries.. it's like a js object..
thisDictionary = {
    "band" : "Ford",
    "model": "Mustang",
    "year" : 1964 
}
print(thisDictionary)
print(thisDictionary["model"])
print(len(thisDictionary))

# dict constructor...
thisDict = dict(name = "BMW", id = 5658, model = "Mustang")
print(thisDict);
print(type(thisDict["id"]));
thisDict["car"] = "Four  wheel";
print(thisDict)
x = thisDict.values();
print(x);
thisDict["name"] = "Tayota"
print(thisDict);
# python Dictionaries.. it's like a js object..
thisDictionary = {
    "band" : "Ford",
    "model": "Mustang",
    "year" : 1964 
}
# pop() items from the dictionary...
thisDictionary.popitem();
print(thisDictionary)
# practise..
for i in range(1, 21):
    if i%2!=0:
        continue
    print(i)
number_input = int(input("Enter a number: "))
first_number = 1
for i in range(1, number_input+1):
    first_number *=i
print(first_number);

# Get input from user
start = int(input())
end = int(input())
step = int(input())

# Write your for loop here
for i in range(start, end, step):
    print(i);
num1 = int(input()) # Don't change this line
num2 = int(input()) # Don't change this line
product = num1 * num2
print("product =", product) # Don't change this line
#Python Function...
def myFunction ():
    print("Hello from a function")
myFunction();
def student(firstName, lastName):# here firstName and lastName is perameter..
    print(f"Name of student is {firstName} {lastName}");
student("Nazib", "Ul Alam") #here inside function thats  are arguments...

def increment(number, by):
    return number + by;
print(increment(2, by=1))

def temperature (temp):
    return (temp-32)*5 / 9;
print(temperature(77));
def my_function(animal, name):
    print(f"I have a {animal}")
    print(f"My {animal}'s name is {name}");
my_function(animal="Cat", name="Joro");

def my_function (person):
    print("Name", person["name"])
    print("Age:", person["age"]);
# dictionary as an argument....
my_person = {"name": "Email", "age": 25}
my_function(my_person)
# Get input for rows and columns
rows = int(input())
cols = int(input())

# Write your nested loops here
# Outer loop for rows
# Inner loop for columns
for i in range(rows):
    rows = ""
    for j in range(cols):
        rows += "*"
    print(rows)

first_input = int(input())
res = 0
for i in range(first_input):
    inputs = int(input())
    res += inputs
print(res);

# Declare the function print_large_number below
def print_large_number():
    print(50005000)
n = int(input())
for i in range(n):
    # Call the function here
    print_large_number();

# Declare your function here
def product(a1, b1):
    return print(a1 * b1);
# # print the result of a*b inside the function
a = int(input())
b = int(input())
# # Call your function here with the arguments a and b
product(a, b);

def square_number (n):
    return n*n
input_num = int(input())
result = square_number(input_num)
print(result);

yearInput = int(input("Enter the year: "))
if (yearInput % 4 == 0 and yearInput % 100 !=0) or (yearInput % 400 == 0):
    print("Leap Year");
else:
    print("Not Leap Year");

def is_leap(year):
    leap = False
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True;
    else:
        return False;
    return leap;

year = int(input())
print(is_leap(year))

n = int(input());
for i in range(n):
    i +=1
    print(i, end="");

# List problem...
n = int(input())
new_list = []
for i in range (n):
    userInput = input()
    if(userInput[0] == 'insert'):
        i = int(userInput[1])
        e = int(userInput[2])
        new_list(i,e);
    elif (userInput[0]=="print"):
        print(new_list)
    elif (userInput[0]=="remove"):
        e = int(userInput[1])
        new_list.remove(e)
    elif (userInput[0]=="append"):
        e = int(userInput[1])
        new_list.append(e)
    elif (userInput[0]=="sort"):
        new_list.sort()
    elif (userInput[0]=="pop"):
        new_list.pop()
    elif (userInput[0]=="reverse"):
        new_list.reverse()
def fizzbuzz(number):
    # Check for "Almost Fizz" first (contains '3')
    if "3" in str(number):
        if number % 3 != 0 and number % 7 != 0:
            return "Almost Fizz"
        # If divisible by 3 or 7, fall through to normal rules
    
    # Original FizzBuzz rules
    if number % 3 == 0 and number % 7 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 7 == 0:
        return "Buzz"
    else:
        return str(number)

def myfunc():
    x = 300
    print(x);
myfunc();


def values(lst):
    # Write code here
    for i in range(len(lst)):
        print(lst[i]);

values([5,9,2,10,2])

data = [1,2,3,4]
data.clear()
