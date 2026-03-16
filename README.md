# Python Mini Projects

A collection of two beginner-friendly Python programs: a number guessing game and a simple calculator.

---

## 1. Number Guessing Game (`number_guess.py`)

### Overview

A terminal-based game where the player tries to guess a randomly chosen number between 1 and 100. The game gives temperature-style hints to guide the player and allows replaying after each round.


### How It Works

1. The program picks a secret random number between 1 and 100.
2. The player is given **10 attempts** to guess correctly.
3. After each guess, a hint is shown based on how close the guess is:

   | Difference from Secret Number | Hint     |
   |-------------------------------|----------|
   | Exactly 0                     | Correct! |
   | 1 – 5                         | Warmer!  |
   | 6 – 20                        | Warm     |
   | 21 – 40                       | Cold     |
   | 41+                           | Colder   |

4. If the player guesses correctly, the game ends with a congratulations message.
5. If all 10 attempts are used up without a correct guess, the secret number is revealed.
6. After each round, the player is asked if they'd like to play again.

### Input Validation

- Guesses outside the 1–100 range are rejected (the attempt is not counted).
- Non-numeric input is caught and prompts the player to try again (the attempt is not counted).

### Example Gameplay

```
Welcome to the Number Guessing Game!
You have 10 attempts to guess the number
I'm thinking of a number between 1 and 100.
Enter your guess (10 attempt(s) left): 50
Cold

Enter your guess (9 attempt(s) left): 80
Warmer!

Enter your guess (8 attempt(s) left): 83
Correct! You guessed the right number with 8 attempts remaining.

Do you want to play again? (y/n):
```

---

## 2. Simple Calculator (`simple_calc.py`)

### Overview

A terminal-based calculator that supports six arithmetic operations. The user selects an operation from a menu and enters the required numbers to get a result.

### How It Works

On launch, a menu is displayed:

```
==== SIMPLE CALCULATOR ====

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor Division
6. Exponentiation
0. Exit
```

The user enters a number (0–6) to choose an operation. The calculator then prompts for the necessary inputs and displays the result. The menu loops until the user selects `0` to exit.

### Operations

| Option | Operation       | Description                                              | Output Format        |
|--------|-----------------|----------------------------------------------------------|----------------------|
| 1      | Addition        | Adds two numbers                                         | `a + b = result`     |
| 2      | Subtraction     | Subtracts second number from first                       | `a - b = result`     |
| 3      | Multiplication  | Multiplies two numbers                                   | `a x b = result`     |
| 4      | Division        | Divides first number by second (4 decimal places)        | `a ÷ b = result`     |
| 5      | Floor Division  | Integer division with remainder shown if applicable      | `a ÷ b = q r r`      |
| 6      | Exponentiation  | Raises a base to a given power                           | `base power exp = result` |

### Input Validation

- **Division (option 4):** If the second number is 0, the user is re-prompted until a valid non-zero number is entered.
- **Floor Division (option 5):** Same zero-check applies. Inputs are treated as integers.
- **Invalid menu choice:** Displays an error message and re-shows the menu.

### Example Usage

```
Choose an operation (0-6): 5
Enter first integer: 17
Enter second integer: 5
17 ÷ 5 = 3 r 2

==== SIMPLE CALCULATOR ====
Choose an operation (0-6): 0
Exiting calculator. Goodbye!
```

---

## Requirements

- Python 3.10 or higher (required for the `match` statement used in `simple_calc.py`)
- No external libraries needed — both scripts use the Python standard library only.
