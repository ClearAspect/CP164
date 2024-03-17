"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total

# Constants


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

for v in DATA1:
    bst1.insert(Letter(v))

for v in DATA2:
    bst2.insert(Letter(v))

for v in DATA3:
    bst3.insert(Letter(v))
    
big_fh = open("miserables.txt", "r", encoding = "utf-8")
do_comparisons(big_fh, bst1)
total1 = comparison_total(bst1)

big_fh = open("miserables.txt", "r", encoding = "utf-8")
do_comparisons(big_fh, bst2)
total2 = comparison_total(bst2)

big_fh = open("miserables.txt", "r", encoding = "utf-8")
do_comparisons(big_fh, bst3)
total3 = comparison_total(bst3)

print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(f"{total1:,d}")
print("------------------------------------------------------------")
print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print(f"{total2:,d}")
print("------------------------------------------------------------")
print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print(f"{total3:,d}")



