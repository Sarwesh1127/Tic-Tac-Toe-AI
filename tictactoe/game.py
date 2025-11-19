from .board import Board
from typing import Optional

class Game:
    def __init__(self, human: str = 'X', ai: str = 'O'):
        if human == ai:
            raise ValueError("Human and AI must have different symbols")
        self.board = Board()
        self.human = human
        self.ai = ai
        self.current = 'X'  # X always starts

    def make_human_move(self, pos: int) -> bool:
        if self.current != self.human:
            return False
        ok = self.board.make_move(pos, self.human)
        if ok:
            self.current = self.ai
        return ok

    def make_ai_move(self, pos: int) -> bool:
        if self.current != self.ai:
            return False
        ok = self.board.make_move(pos, self.ai)
        if ok:
            self.current = self.human
        return ok

    def winner(self) -> Optional[str]:
        return self.board.winner()

    def is_over(self) -> bool:
        return self.board.game_over()

    def __str__(self):
        return str(self.board)
