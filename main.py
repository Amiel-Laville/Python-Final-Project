from chess_board import ChessBoard
from player import Player, AIPlayer

def play_game(mode):
    board = ChessBoard()

    if mode == "1":
        white = Player("white")
        black = AIPlayer("black")
    elif mode == "2":
        white = Player("white")
        black = Player("black")
    else:
        white = AIPlayer("white")
        black = AIPlayer("black")

    turn = "white"
    move_count = 0
    max_moves = 200

    while move_count < max_moves:
        board.display_board()

        player = white if turn == "white" else black

        if isinstance(player, Player):
            move = input("Enter move (r c r c) or 'quit': ")

            if move.lower() == "quit":
                print("Returning to menu...\n")
                return

            try:
                r1, c1, r2, c2 = map(int, move.split())
                if board.move_piece((r1, c1), (r2, c2)):
                    turn = "black" if turn == "white" else "white"
                    move_count += 1
                else:
                    print("Invalid move")
            except:
                print("Bad input")

        else:
            player.get_move(board)
            turn = "black" if turn == "white" else "white"
            move_count += 1

    print("Game ended.\n")


def main():
    while True:
        print("\n=== CHESS MENU ===")
        print("1. Human vs AI")
        print("2. Human vs Human")
        print("3. AI vs AI")
        print("4. Exit")

        choice = input("Choose: ")

        if choice in ["1", "2", "3"]:
            play_game(choice)
        elif choice == "4":
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    main()
