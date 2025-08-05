# blackjack-game
A simply Blackjack game built with python that runs in terminal.

# Blackjack: Python Console Game

A simple console-based Blackjack game, made as part of my **100 Days of Python** journey with Angela Yu. This project is a hands-on way to practice Python basics while creating a fun and playable mini-game.

## Features

- 🎴 Standard Blackjack rules
- 🤖 Play against a computer dealer
- 🃏 Random card dealing and smart Ace handling (1 or 11)
- 📝 Score calculation and game result feedback
- 🔁 Unlimited rounds—play as many games as you want!
- 🎨 ASCII art game logo (via `art` module)

## Getting Started

1. **Clone or Download** this repository.
2. **Install Dependencies**
   - The only non-standard module is `art`. Install it with:
     ```
     pip install art
     ```
3. **Run the Game**
   ```
   python blackjack.py
   ```

## What I Practiced and Revised

This project helped me revise and strengthen these core Python concepts:

- **Functions:** Defined clear, modular functions for each piece of logic.
- **Lists:** Used lists to manage each player's cards, applying methods like `.append()` and `.remove()`.
- **Control Flow:** Implemented decision-making with `if`/`elif`/`else` and repeated actions with `while` loops.
- **Randomization:** Used the `random` module for shuffling and dealing cards.
- **User Interaction:** Managed input/output for smooth game flow.
- **Game Logic:** Applied Blackjack rules—like Ace value changes, dealer drawing logic, win/lose conditions.

## Sample Gameplay

```
Do you want to play a game of Blackjack? Type 'y' or 'n'.
y

 _________
|A        |
|         |
|    ♠    |
|         |
|_______ A|

Your cards: [11, 7] and Current Score = 18
Computer card: 10
Do you want to draw another card? Type 'y' or 'n'.n
Game over.
Your final hand: [11, 7], final score: 18
Computer's final hand: [10, 8], final score: 18
draw.
```

## Ideas for Future Improvements

- Input validation for user choices
- Betting/chips system and tracking win streaks
- GUI version with Tkinter or a web-based interface
- Multiplayer support
- Saving and displaying game statistics or leaderboards
- More visual card representations

## Acknowledgements

Made as part of the **100 Days of Python** course by Angela Yu.  
Thanks to the course, I could put my Python knowledge into practice while building something fun!

Happy coding and enjoy playing Blackjack! 🖤🃏

Feel free to adjust the text and formatting to match your personal preferences or project details!
