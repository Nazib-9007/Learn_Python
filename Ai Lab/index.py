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
