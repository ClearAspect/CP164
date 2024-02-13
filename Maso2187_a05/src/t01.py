"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""

# Imports
from List_array import List
from Food import Food
from Food_utilities import read_food

# Constants

foodsList = List()
emptyList = List()
number1List = List()
number2List = List()
number3List = List()

for i in range(20):
    number1List.append(i)
    number2List.append(i)

fh = open("foods.txt", "r", encoding="utf-8")
for line in fh:
    food = read_food(line)
    foodsList.append(food)

fh.close()

if number1List == number2List:
    print("Lists are equal")
else:
    print("Lists are not equal")

if number1List == emptyList:
    print("Lists are equal")
else:
    print("Lists are not equal")


number3List.intersection(number1List, number2List)
print("Intersected List")
for e in number3List:
    print(f"{e} ", end="")
print("")


number3List = List()
number3List.combine(number1List, number2List)
print("Combine List")
for e in number3List:
    print(f"{e} ", end="")
print()

number3List.clean()
print("Cleaned List")
for e in number3List:
    print(f"{e} ", end="")
print()


number3List.prepend(100)
number3List.prepend(8)
number3List.prepend(8)
number3List.prepend(8)
print("Prepended List")
for e in number3List:
    print(f"{e} ", end="")
print()

number3List.remove_front()
number3List.remove_many(8)
print("Removed Front List and all 8s")
for e in number3List:
    print(f"{e} ", end="")
print()

number4list = List()
number4list = number3List.copy()

target1 = List()
target2 = List()

target1, target2 = number3List.split()
print("Split List")
for e in target1:
    print(f"{e} ", end="")
print()
for e in target2:
    print(f"{e} ", end="")
print()


target1, target2 = number4list.split_alt()
print("Split Alt List")
for e in target1:
    print(f"{e} ", end="")
print()
for e in target2:
    print(f"{e} ", end="")
print()

target1.append(2)
target1.append(4)

number4list = List()
number4list.union(target1, target2)
print("Union List")
for e in number4list:
    print(f"{e} ", end="")
print()
