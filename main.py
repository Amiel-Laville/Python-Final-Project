from chess_board import ChessBoard
from player import Player, AIPlayer

def main():
    print("Welcome to Chess!")
    print("1. Human vs AI")
    print("2. Human vs Human")
    print("3. AI vs AI")
    
    while True:
        mode = input("Select mode (1/2/3): ")
        if mode in ['1', '2', '3']:
            break
        print("Invalid selection.")
    
    board = ChessBoard()
    
    if mode == '1':
        white_player = Player('white')
        black_player = AIPlayer('black')
        print("You are White.")
    elif mode == '2':
        white_player = Player('white')
        black_player = Player('black')
    else:
        white_player = AIPlayer('white')
        black_player = AIPlayer('black')
    
    current_color = 'white'

    move_count = 0
    max_moves = 100  # stops infinite games

    while move_count < max_moves:
        board.display_board()
        
        player = white_player if current_color == 'white' else black_player
        
        try:
            player.get_move(board)
            current_color = 'black' if current_color == 'white' else 'white'
            move_count += 1

        except KeyboardInterrupt:
            print("\nGame ended.")
            break

    print("Game ended (move limit reached).")

if __name__ == "__main__":
    main()
