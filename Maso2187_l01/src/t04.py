"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-11"
-------------------------------------------------------
"""
# Imports
import Food_utilities

# Constants

fh = open('foods.txt', 'r', encoding='utf-8')

food = Food_utilities.read_food(fh.readline())