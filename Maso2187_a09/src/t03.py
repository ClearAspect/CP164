"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-03-24"
-------------------------------------------------------
"""
# Imports
from Hash_Set_BST import Hash_Set
from functions import insert_words, comparison_total

# Constants

fh = open("otoos610.txt", "r", encoding="utf-8")
hash_set = Hash_Set(20)

insert_words(fh, hash_set)
total, max_word = comparison_total(hash_set)


print("Using linked BST Hash_Set\n")
print(f"Total Comparisons: {total:,}")
print(f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")