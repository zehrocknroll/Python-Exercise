""" 
Data Structures

- Numbers: int, float, complex
- Strings: str
- Boolean (TRUE-FALSE): bool
- List
- Dictionary
- Tuple
- Set

"""


#integer 
x = 10
type(10)

#float
x = 6.5
type(6.5)

#complex
x = 2j + 8
type(x)

x = "Hello Python"
type(x)

#boolean (True-False)

6==7 #False
3==8 #False
1==1 #True
type(6 == 4)


#list 
x = ["python","r","julia"]
type(x)

#dictionary
x = {"name":"Chandler","Age":26}
type(x)

#tuple 
x = ("spyder","pycharm","vscode")
type(x)

#set
x = {"spyder","pycharm","vscode"}
type(x)

#Note: List, tuple, set, and dictionary data structures are also referred to as Python Collections (Arrays).


#Numbers: int, float, complex

a = 10
b = 20

a * 5
b / 4
a * b /18
a ** 2


#changing types

int(b)
float(a)
int(a * b /18)
c = a * b / 45
int(c)


#STRINGS


print("Zehra")
print('Zehra')

name = "Zehra"
name = 'Zehra'


#accessing elements of strings

name
name[0]
name[1]
name[2]
name[3]
name[-1]
name[-2]


#slice operation in character strings

name[0:3]


#querying a character in a string


string = "data","ml","nlp"


"data" in string
"Data" in string



#string methods

dir(str)


#len
name = "Machine"
type(name)
type(len)

len("Machine Learning")


#upper() & lower(): small-to-large conversions


"data".upper()
"MACHINE".lower()

type(upper)
type(upper())


#replace: replaces characters

data = "Data Preprocessing"
data.replace("r","l")


#split

"Hello Python".split()


#strip

" fogofoh".strip()
"fogofoh".strip("o")



#capitalize: capitalizes the first letter


"machine".capitalize()
dir(machine)

"machine".startswith("f")


#LIST

# - Changeable
# - It is sequential. Index operations can be done.
# - It is inclusive.


list = [1,2,3,4,5]
type(list)
letter = ["a","b","c","d"]
mixed = [1,2,3,4,"a","b",True,[1,2,3]]

mixed[0]
mixed[3]
mixed[6]
mixed[7][2]

type(mixed[6])
type(mixed[7])
type(mixed[7][0])

list[0] = 88
mixed[0:4]




#list methods

dir(list)


#len: size information
len(list)
len(mixed)


#append: adds element
list.append(6)


#pop: delete by index

list.pop(0)


#insert: inserts into index


list.insert(1,7)




#DICTIONARY


# - It can be changed.
# - Unordered.
# - Container.

#key-values

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]



dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["CART"][1]


#key query
"RFR" in dictionary


#accessing value by key
dictionary["REG"]
dictionary.get("REG")


#change value
dictionary["REG"] = ["YSA", 10]


#access all keys
dictionary.keys()

#access all values
dictionary.values()


#convert all pairs to list as tuples
dictionary.items()


#updating key-value
dictionary.update({"REG": 11})


#adding new key-value
dictionary.update({"RF": 10})



#TUPLE

# - Cannot be changed.
# - It is sequential.
# - It is inclusive.


t = ("Zehra","Hamza",1,2)
type(t)

t[0]
t[0:2]

t[0] = 30

t = list(t)
t[0] = 30
t = tuple(t)



#SET

# - Can be changed.
# - Unordered + Unique.
# - It is inclusive.


set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

#difference(): difference of two sets

#in set1 but not in set2.
set1.difference(set2)
set1 - set2

# in set2 but not in set1.
set2.difference(set1)
set2 - set1


#symmetric_difference(): not relative to each other in both sets
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)


#intersection(): the intersection of two sets
set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2


#union(): union of two sets
set1.union(set2)
set2.union(set1)


#isdisjoint(): is the intersection of two sets empty?
et1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


#issubset(): Is one set a subset of another set?
set1.issubset(set2)
set2.issubset(set1)


#issuperset(): does one set include another set?
set2.issuperset(set1)
set1.issuperset(set2)









