import sys
from checkmate import checkmate

files = sys.argv[1:]
for file in files:
    with open(file, 'r') as f:
        board = f.read()
        checkmate(board)