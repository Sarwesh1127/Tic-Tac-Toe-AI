from typing import Tuple
from .board import Board

class AI:
    def __init__(self, symbol: str, opponent: str):
        self.symbol = symbol
        self.opponent = opponent

    def best_move(self, board: Board) -> int:
        _, move = self._minimax(board, True, 0, float('-inf'), float('inf'))
        assert move is not None
        return move

    def _minimax(self, board: Board, maximizing: bool, depth: int, alpha: float, beta: float) -> Tuple[int, int]:
        winner = board.winner()
        if winner == self.symbol:
            return (10 - depth, -1)
        elif winner == self.opponent:
            return (-10 + depth, -1)
        elif board.is_full():
            return (0, -1)

        if maximizing:
            best_val = float('-inf')
            best_move = -1
            for mv in board.available_moves():
                board.make_move(mv, self.symbol)
                val, _ = self._minimax(board, False, depth + 1, alpha, beta)
                board.undo_move(mv)
                if val > best_val:
                    best_val = val
                    best_move = mv
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return best_val, best_move
        else:
            best_val = float('inf')
            best_move = -1
            for mv in board.available_moves():
                board.make_move(mv, self.opponent)
                val, _ = self._minimax(board, True, depth + 1, alpha, beta)
                board.undo_move(mv)
                if val < best_val:
                    best_val = val
                    best_move = mv
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return best_val, best_move
