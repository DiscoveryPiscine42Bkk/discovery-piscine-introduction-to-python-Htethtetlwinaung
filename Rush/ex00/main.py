import sys
from checkmate import checkmate


def main():
    board = """
    ....
    .K..
    .K..
    ...B
    """
    checkmate(board)
    
if __name__ == "__main__":
    main()
