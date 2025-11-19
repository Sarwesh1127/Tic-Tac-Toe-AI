from typing import List, Optional

class Board:
    def __init__(self):
        # 9 cells, positions 0..8
        self.cells: List[Optional[str]] = [None] * 9

    def make_move(self, pos: int, player: str) -> bool:
        if pos < 0 or pos > 8: 
            raise ValueError("Position must be between 0 and 8")
        if self.cells[pos] is not None:
            return False
        self.cells[pos] = player
        return True

    def undo_move(self, pos: int) -> None:
        self.cells[pos] = None

    def available_moves(self) -> List[int]:
        return [i for i, c in enumerate(self.cells) if c is None]

    def is_full(self) -> bool:
        return all(c is not None for c in self.cells)

    def _lines(self):
        # rows, columns, diagonals
        return [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]

    def winner(self) -> Optional[str]:
        for a,b,c in self._lines():
            if self.cells[a] is not None and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def game_over(self) -> bool:
        return self.winner() is not None or self.is_full()

    def __str__(self):
        def ch(x):
            return x if x is not None else ' '
        rows = [' | '.join(ch(self.cells[r*3 + c]) for c in range(3)) for r in range(3)]
        return "\n---------\n".join(rows) + "\n"
