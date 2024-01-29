"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Roan Somers Mason
ID:      169072187
Email:   maso2187@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze

# Constants

maze1 = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
            'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}

maze2 = {'Start': ['X']}

maze3 = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
    'D':[], 'E': ['X', 'F'], 'F':['G'], 'G':['C']} 

# maze4 = {'Start': ['A'], 'A':[]}


mazes = [maze1, maze2, maze3]

for maze in mazes:
    result = stack_maze(maze)
    if not result == None:
        string = ""
        for element in result:
            string += f"{element}, "
    else:
        string = "None"
    
    print(f"Result: {string}")
