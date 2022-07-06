
"""

FUNCTIONS, CONDITIONS, LOOPS, COMPREHENSIONS

"""

#FUNCTIONS


#function definition
def multiplication(x):
    print(x * 2)
    
multiplication(8)


#define a function with two arguments/parameters
def summer(arg1, arg2):
    print(arg1 + arg2)
    
summer(9, 3)

summer(3, 9)

summer(arg2=6, arg1=2)



#docstring
def summer(arg1, arg2):
    print(arg1 + arg2)


def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    """

    print(arg1 + arg2)


summer(10, 8)


#statement/body section of functions

# def function_name(parameters/arguments):
#     statements (function body)



def say_hi():
    print("Hello")
    print("Hi")
    print("Hallo")


say_hi()


def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("data")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(6, 5)


#function to store the entered values ​​in a list.


list_l = []


def add_element(a, b):
    c = a * b
    list_l.append(c)
    print(list_l)


add_element(16, 32)
add_element(18, 28)
add_element(90, 50)


#default parameters/arguments
def divide(a, b):
    print(a / b)


divide(5, 1)


def say_hi(string="Hello"):
    print(string)
    print("Hi")
    print("Hallo")


say_hi("Welcome")




# varm, moisture, charge
(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80



def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(100, 15, 72)
calculate(95, 14, 65)


#return: using function outputs as input
def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)



# calculate(100, 15, 72) * 10
def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(100, 15, 72) * 10

a = calculate(100, 15, 72)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


type(calculate(98, 12, 78))

varma, moisturea, chargea, output = calculate(98, 12, 78)



#calling a function from within a function
def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(96, 20, 20) * 10


def standardization(d, p):
    return d * 10 / 100 * p * p


standardization(16, 1)


def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(2, 6, 9, 17)


def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(5, 9, 18, 19, 26)


#local global variables
list_l = [1, 2]

def add_element(a, b):
    c = a * b
    list_l.append(c)
    print(list_l)

add_element(4, 10)




#CONDITIONS


1 == 1
1 == 2

if 1 == 1:
    print("python")
    
if 1 == 5:
    print("python")
    
    
    
def number(number):
    if number == 10:
        print("number is 10")

number(19)


#else
def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("number is not 10")

number_check(12)


#elif
def number(number):
    if number > 10:
        print("greater than 10")
    elif number < 10:
        print("less than 10")
    else:
        print("equal to 10")

number(6)



#LOOPS


#for loop

languages = ["python","java","c","julia"]

languages[0]
languages[1]
languages[2]


for lan in languages:
    print(languages)
    
for lan in languages:
    print(lan.upper())
    

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)
    
    

for salary in salaries:
    print(int(salary*20/100 + salary))

for salary in salaries:
    print(int(salary*30/100 + salary))

for salary in salaries:
    print(int(salary*50/100 + salary))

def new_salary(salary, rate):
    return int(salary*rate/100 + salary)

new_salary(1500, 10)
new_salary(2000, 20)

for salary in salaries:
    print(new_salary(salary, 20))


salaries2 = [10700, 25000, 30400, 40300, 50200]

for salary in salaries2:
    print(new_salary(salary, 15))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))
        
        
#purpose: we want to write a string-changing function as follows.

#before: "hi my name is john and i am learning python"
#after: "Hi mY NaMe iS JoHn and i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string = ""
    #browse the indexes of the entered string.
    for string_index in range(len(string)):
       #capitalize if index is even.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        #convert to lowercase if index is odd.

        else:
            new_string += string[string_index].lower()
    print(new_string)

alternating("hi my name is john and i am learning python")




#break & continue & while



salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    if salary == 3000:
        break
    print(salary)


for salary in salaries:
    if salary == 3000:
        continue
    print(salary)
    
    
#while
num = 1
while num < 10:
    print(num)
    num += 1
    
    
#enumerate: for loop with automatic counter/indexer


name = ["Zehra", "Hamza", "Mark", "Jordan"]

for n in name:
    print(n)

for index, n in enumerate(name):
    print(index, n)

A = []
B = []

for index, n in enumerate(name):
    if index % 2 == 0:
        A.append(n)
    else:
        B.append(n)

    
#purpose     
#write a divide_students function.
#put the students in the double index into a list.
#take the students in one index to another list.
#but let these two lists return as a single list.
    
    
students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]




#writing the alternating function with enumerate
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learning python")



#zip
students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))


#lambda, map, filter, reduce


def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b

new_sum(4, 5)



#map
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))


#del new_sum
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2 , salaries))

#filter
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

#reduce
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)



#COMPREHENSIONS



#list comprehension
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))

null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))

[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]
[salary * 2 for salary in salaries]
[salary * 2 for salary in salaries if salary < 3000]
[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]
[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries]
students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]


[student.lower() if student in students_no else student.upper() for student in students]
[student.upper() if student not in students_no else student.lower() for student in students]




#dict comprehension
dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}

{k.upper(): v for (k, v) in dictionary.items()}

{k.upper(): v*2 for (k, v) in dictionary.items()}




#purpose: want to add even numbers to a dictionary by squaring them
#keys will be original values ​​and values ​​will be modified values.
numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n: n ** 2 for n in numbers if n % 2 == 0}


#list & dict comprehension applications


#changing variable names in a dataset

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())


A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]


#requests NO_FLAG to others of what happened to those with "INS" in their name


# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
#  'NO_FLAG_SPEEDING',
#  'NO_FLAG_ALCOHOL',
#  'NO_FLAG_NOT_DISTRACTED',
#  'NO_FLAG_NO_PREVIOUS',
#  'FLAG_INS_PREMIUM',
#  'FLAG_INS_LOSSES',
#  'NO_FLAG_ABBREV']

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]




#purpose is to create a dictionary with a string key and a list as the value below.
#we want to do it for numeric variables only.


# Output:
# {'total': ['mean', 'min', 'max', 'var'],
#  'speeding': ['mean', 'min', 'max', 'var'],
#  'alcohol': ['mean', 'min', 'max', 'var'],
#  'not_distracted': ['mean', 'min', 'max', 'var'],
#  'no_previous': ['mean', 'min', 'max', 'var'],
#  'ins_premium': ['mean', 'min', 'max', 'var'],
#  'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

#short blond
new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)    
    













