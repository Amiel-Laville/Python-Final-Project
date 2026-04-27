from chess_board import ChessBoard
from player import Player, AIPlayer

def play_game(mode):
    board = ChessBoard()

    if mode == '1':
        white_player = Player('white')
        black_player = AIPlayer('black')
    elif mode == '2':
        white_player = Player('white')
        black_player = Player('black')
    else:
        white_player = AIPlayer('white')
        black_player = AIPlayer('black')

    current_color = 'white'
    move_count = 0
    max_moves = 200

    while move_count < max_moves:
        board.display_board()

        print("Type 'quit' to end game and return to menu")

        player = white_player if current_color == 'white' else black_player

        # ---- END GAME COMMAND CHECK ----
        if isinstance(player, Player):
            move = input(f"{current_color} move (r c r c): ")

            if move.lower() == "quit":
                print("Returning to main menu...\n")
                return

            try:
                r1, c1, r2, c2 = map(int, move.split())
                if board.move_piece((r1, c1), (r2, c2)):
                    current_color = 'black' if current_color == 'white' else 'white'
                    move_count += 1
                else:
                    print("Invalid move")
            except:
                print("Invalid input")

        else:
            # AI move
            player.get_move(board)
            current_color = 'black' if current_color == 'white' else 'white'
            move_count += 1

    print("Game ended (move limit reached). Returning to menu...\n")


def main():
    while True:
        print("=== CHESS GAME MENU ===")
        print("1. Human vs AI")
        print("2. Human vs Human")
        print("3. AI vs AI")
        print("4. Exit")

        choice = input("Select option: ")

        if choice in ['1', '2', '3']:
            play_game(choice)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()
