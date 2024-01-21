"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import food_search

# Constants

foods = [
    Food("BBQ Pork", 1, False, 920),
    Food("Beef with Green Pepper", 1, False, 251),
    Food("Vegetable Curry", 2, True, 350),
    Food("Sushi", 6, False, 180),
    Food("Margarita Pizza", 7, True, 800),
]

searched_foods = food_search(foods, 1, 0, None)
for food in searched_foods:
    print(f"Origin: Chinese, Food: {food.name}")