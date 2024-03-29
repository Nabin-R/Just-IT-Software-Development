# print(1+1)
# print(9-2)
# print(14*2)
# print(10^3)
print(2 * 3, "\n", 2 + 3, "\n", 2 / 3, "\n", 21 - 3)

print('Nabin', '\n', 'London', '\n', 'Coding')


# ~string comments
"This is a comment"

"""
This is a multiline comment 
This is a multiline comment 
This is a multiline comment 
"""

# Boolean data types
# Boolean is yes/no or true or false (0 = off and 1 = on)
bVal1 = True # declare and assign a boolean type variable with value True
bVal2 = False # declare and assign a boolean type variable with value False


# Numeric data types
num1 = 20.5 # float(decimal) variable declaration and assigment 
num2 = 20 # integer variable declaration and assigment


"To DO: type() function is used to ?"
print(type(bVal1)) # bool
print(type(bVal2))

s1 = 'String 1'
s2 = 'String 2'
s3 = 'String 3'

print(type(s1)) # str
print(type(s2))
print(type(s3))

print(type(num1)) #float
print(type(num2)) #int

"Modify:"
"To DO:"
# Modify the data structures above by changing their values or oject names

num1 + 1

print(num1)


"Make:"
"To DO:"
# Produce five examples of numeric datatypes

number1 = 10
number2 = 1j
number3 = 30.3
number4 = 0o10
number5 = 5.80

print(type(number1)) #int
print(type(number2)) #complex
print(type(number3)) #float/double
print(type(number4)) #floating point
print(type(number5)) #float

# Produce five examples of string datatypes

"Objectives"
"" '' #Variables and Variable naming convention
"" '' #Use meaningful identifiers
"" '' #Determine the need for variables
"" '' #Distinguish between declaration, initialisation, and assignment of variables 
"" '' #Demonstrate appropriate use of naming conventions
"" '' #Output data (e.g. print (myVvar))


"Research"
# What is variable in python
#Answer: A variable ........ ​

"Characteristics or features of variables"
# A variable .........

"Object references 1"
var_num = "an_object"  #  var_num is now a name referencing the object "an_object"
num1 = 10  # static object/value
num2 = 20  # static object/value
num3 = 30  # static object/value


"Predict, then Run, and Investigate"
"What is the function the object's type when used in as shown below?"
print(type(num1))

"This is what happens when you create a variable in python?"
# 1. Creates and int/float/string object (variable)
# 2. Assign the object the value
# 3. use or print the object


answer1 = num1 + num2
print(answer1)
answer2 = num3 * num2
print(answer2)
answer3 = answer1 + answer2
print(answer3)


"Assign multiple values(objects) to multiple variables in a single line"
#To DO: Complete the code below to assign values to the respective variables
name, address, interest = "your name", "your fake address", "your interest"
print(name, address, interest)


"Chained assignment"
first_child = second_child = third_child = "your name"
print(
    "I am the first child",
    first_child,
    "\nI am the second child",
    second_child,
    "\nI am the third child",
    third_child,
)

"You have now seen the how to assign multiple values(objects) to multiple variables and chained assignment."
"In your own words, can you explain the difference between the two?"
#The differences 


"Object references 2"
# Rather than creating a new object when num4 = num1 code is executed,
# it creates a symbolic name/reference, and num4 now point to the object with a value of 10
# same as num1
num4 = num1  # multiple references to the same object
print(id(num1))  # id returns the identify of an object
print(id(num4))

"Will the identity of the two objects referenced below be the same ?"
num1 = 10
num4 = "10"
print(id(num1))
print(id(num4))


# num1 = "10"
# print(type(num1))
# num1 = 10.0
# print(type(num1))

"What is the evivalent of python type in JavaScript?"
#The equivalent of 


"Knowledge Check"
#To DO: Write one thing you remember from what we covered so far?


"Read, Run and investigate the lines of code below"

# Variable naming convention
username = "user1"  # meaningful name

# use of camel notation when the variable is a combination of two words
userName = "user2"

 # use snake case/underscore when the variable is a combination of two words
user_name = "user3" 

user4 = "paul0045"  # meaningful name

userAge = 23  # meaningful name

firstname = "Anna"  # meaningful name and use of single quotes in value

"DON'T DO THIS"
AGE = 12  # Unless it is a constant!!
# £cash or $cash
User = "muser"  # dont start variable with upper case
# user name = # no spaces between two words in variable assignment
# 1user = "jam"# no number at start of variable name

# Avoid doing the following:
# £errr = "money"  don't use a symbol
# AGE = 12 variable name should not be in all upper cases
# Username = "toby345" # don't start variable names with upper case character
# 2username = "Coder112345" #dont start variable names with number
# user name = "test user" # no spaces between variable name/s



"Research:" 
"To DO: Is there a difference in using dollar or any other currency symbol to declare variable in JS vs python?"


"Further reading on variables naming convention and independent learning, see link(s) below"
# https://peps.python.org/pep-0008/#function-and-variable-names
# https://namingconvention.org/python/


# Python constant
AGE = 12  # AGE is constant do not re-assign with a different object
print("\nOriginal age is", AGE)

AGE = 15
print("\nAge is now", AGE)

"Research:" 
"To DO: Investigate how python use make use of constants to answer if there is any similarity with constant use in JavaScript?"

mySet = [1, 2, 3, 4]
print('Example: ', mySet[0])

#Modifying
newSet = mySet[:3], 5, mySet[3:]
print(newSet) 

mySet2 = {'Apple', 'Banana', "Orange", True, 1, 2}
print("Example 2: ", mySet2)


# List - List are Ordered

my_List = [1, True, 'Hi', [1,2,3]]

# Dictionary

Person = {
    "Name": "Nabin",
    "Age": 23,
    "Gender": "M"
}

print (Person["Name"])

# Change Value
Person["Name"] = "Nabin Raj"
print (Person["Name"])

#Updating Keys/Values
Person.update({"Name": "Md Nabin Raj"})
Person.update({"DOB": "11-02-01"}) #Adding new Value
print(Person)