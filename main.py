"""Main chess game entry point"""
from chess_board import ChessBoard
from player import Player, AIPlayer

def main():
    print("Welcome to Chess!")
    print("Game mode selection:")
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
        print("You are White. AI is Black.")
    elif mode == '2':
        white_player = Player('white')
        black_player = Player('black')
    else:
        white_player = AIPlayer('white')
        black_player = AIPlayer('black')
    
    current_color = 'white'
    
    while True:
        board.display_board()
        
        player = white_player if current_color == 'white' else black_player
        
        try:
            player.get_move(board)
            current_color = 'black' if current_color == 'white' else 'white'
        except KeyboardInterrupt:
            print("\nGame ended by player.")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()