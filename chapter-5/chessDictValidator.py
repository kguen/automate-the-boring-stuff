def isValidChessBoard(board):
    pieces = ('king', 'queen', 'rook', 'bishop', 'knight', 'pawn')
    for key, value in board.items():
        # Validate key
        if len(key) != 2:
            print('Invalid key: ' + key)
            return False
        elif key[0] < '1' or key[0] > '8':
            print('Invalid key: ' + key)
            return False
        elif key[1] < 'a' or key[1] > 'h':
            print('Invalid key: ' + key)
            return False
        
        # Validate value
        if value[0] != 'b' and value[0] != 'w':
            print('Invalid value: ' + value)
            return False
        elif value[1:] not in pieces:
            print('Invalid value: ' + value)
            return False

    # Validate number of pieces
    pieceCnt = {
        'b': {'total': 0, 'pawn': 0, 'king': 0},
        'w': {'total': 0, 'pawn': 0, 'king': 0}
    }
    for value in board.values():
        color = value[0]
        pieceName = value[1:]
        pieceCnt[color]['total'] += 1
        if pieceName in pieceCnt[color].keys(): # Not counting pieces other than pawn and king
            pieceCnt[color][pieceName] += 1

    for color in pieceCnt.keys():
        if pieceCnt[color]['total'] > 16:
            print('Too many ' + (color == 'b' and 'black' or 'white') + ' pieces!')
            return False
        if pieceCnt[color]['king'] != 1:
            print('Each side has exactly 1 king!')
            return False
        if pieceCnt[color]['pawn'] > 8:
            print('Too many ' + (color == 'b' and 'black' or 'white') + ' pawns!')
            return False
    return True

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
if isValidChessBoard(board):
    print('This board is valid.')