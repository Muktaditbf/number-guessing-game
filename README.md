# 🎯 Number Guessing Game

A command-line game in Python: the computer picks a secret number from 1 to 100, and you guess until you find it.

## Example

```
Guess a number between 1 and 100 (or type 'exit' to quit): 50
Too high! Try again.
Guess a number between 1 and 100 (or type 'exit' to quit): 25
Too low! Try again.
Guess a number between 1 and 100 (or type 'exit' to quit): 37
Congratulations! You've guessed the correct number!
```

## Features

- "Too high" and "too low" hints after every guess
- Rejects text and numbers outside 1–100 without crashing
- Type `exit` to quit at any time

## Run it

```bash
python NumberGuessingGame.py
```

## Tip

Always guess the middle of the remaining range and you'll win in at most 7 guesses. That's **binary search**, since log₂(100) ≈ 7.
