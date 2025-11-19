# Tic-Tac-Toe AI

A simple Tic-Tac-Toe game with an unbeatable AI using Minimax with Alpha-Beta pruning.

Run the CLI to play vs the AI.

Quick start (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate; pip install -r requirements.txt
python cli.py
```

Tests:

```powershell
pip install -r requirements.txt
pytest
```

Using the AI programmatically:

```python
from tictactoe.board import Board
from tictactoe.ai import AI

b = Board()
# set some moves...
b.make_move(0, 'X')
# instantiate AI
ai = AI('O','X')
# get best move
move = ai.best_move(b)
print(move)
```

AI: The AI uses a minimax search that optimizes for win/draw/loss and prunes branches with alpha-beta.
