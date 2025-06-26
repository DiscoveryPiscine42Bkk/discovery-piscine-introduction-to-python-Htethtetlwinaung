def checkmate(board_input):
    board = parse_board(board_input)
    
    size = len(board)
    for row in board:
        if len(row) != size:
            print("Error")
            return None
    
    
    for i, row in enumerate(board):
        for j, pos in enumerate(row):
            # get all possible attack positions for a piece
            attack_positions = []
            if pos == 'P':
                attack_positions = get_pawn_attack_positions(i, j, board)
            elif pos == 'B':
               attack_positions = get_bishop_attack_positions(i, j, board)
            elif pos == 'R':
                attack_positions = get_rook_attack_positions(i, j, board)
            elif pos == 'Q':
                attack_positions = get_queen_attack_positions(i, j, board)
                
            # check for king in attack positions for check mate
            for x, y in attack_positions:
                if board[x][y] == 'K':
                    print("Success")
                    return None
    print("Error")
                
    
    
def parse_board(board_input: str):
    board = []
    for row_input in board_input.strip().split('\n'):
        row = []
        for place in row_input.strip():
            if place == '.':
                row.append(None)
            else:
                row.append(place)
        board.append(row)
    return board

def get_pawn_attack_positions(i, j, board):
    attacks = []
    col_size = len(board[0])
    row_size = len(board)
    forward_row = i-1
    if forward_row < 0:
        return []
    if j-1 >0:
        attacks.append((forward_row, j-1))
    if j+1 < col_size:
        attacks.append((forward_row, j+1))
    return attacks

def get_bishop_attack_positions(i, j, board):
    row_len = len(board)
    col_len = len(board[0])
    directions = [
        (-1, -1),  # Up-Left
        (-1, 1),   # Up-Right
        (1, -1),   # Down-Left
        (1, 1)     # Down-Right
    ]
    
    attack = []
    for dx, dy in directions:
        x, y = i, j
        while 0 <= x < row_len and 0 <= y < col_len:
            x += dx
            y += dy
            if 0 <= x < row_len and 0 <= y < col_len:
                attack.append((x, y))
    return attack

def get_rook_attack_positions(i, j, board):
    row_len = len(board)
    col_len = len(board[0])
    attack = []
    
    # Check vertical and horizontal lines
    for x in range(row_len):
        if x != i:
            attack.append((x, j))
    
    for y in range(col_len):
        if y != j:
            attack.append((i, y))
    
    return attack

def get_queen_attack_positions(i, j, board):
    attack = []
    
    # Get rook-like attack positions
    attack.extend(get_rook_attack_positions(i, j, board))
    
    # Get bishop-like attack positions
    attack.extend(get_bishop_attack_positions(i, j, board))
    
    return attack


    
              
