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
