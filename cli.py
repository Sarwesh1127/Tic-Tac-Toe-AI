from tictactoe.board import Board
from tictactoe.ai import AI


def get_int(prompt: str, choices=None):
    while True:
        try:
            v = int(input(prompt))
            if choices and v not in choices:
                print(f"Choose one of: {choices}")
                continue
            return v
        except ValueError:
            print("Enter a number.")


def print_board(b: Board):
    def ch(x):
        return x if x is not None else ' '
    print('\n')
    for r in range(3):
        print(' | '.join(ch(b.cells[r*3 + c]) for c in range(3)))
        if r < 2:
            print('---------')
    print('\n')


def main():
    print('\nUser VS Tic-Tac-Toe Unbeatable AI')
    print('---------------------------------\n')
    human = None
    while human not in ('X','O'):
        human = input('Pick your symbol (X or O) [X goes first]: ').upper().strip()
    ai_symbol = 'O' if human == 'X' else 'X'

    board = Board()
    ai = AI(ai_symbol, human)
    current = 'X'  # X starts

    while True:
        print_board(board)
        if board.winner():
            print(f"Winner: {board.winner()}")
            break
        if board.is_full():
            print('Draw!')
            break

        if current == human:
            print('Your turn')
            available = board.available_moves()
            print('Available moves: ', available)
            pos = get_int('Enter position (0..8): ', choices=available)
            board.make_move(pos, human)
            current = ai_symbol
        else:
            print("AI thinking...")
            pos = ai.best_move(board)
            print(f"AI chooses {pos}")
            board.make_move(pos, ai_symbol)
            current = human

    print_board(board)
    print('Game over.\n')


if __name__ == '__main__':
    main()
