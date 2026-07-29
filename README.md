# Classic Snake Game

## Description
A fully functional replica of the classic Nokia Snake game built with Python's Turtle graphics library. The player controls a snake that grows longer as it consumes food, with the goal of surviving as long as possible without hitting the walls or its own tail.

## Features
- Smooth snake movement and keyboard controls.
- Dynamic food generation and collision detection.
- Real-time score tracking.
- High score persistence: Reads and writes the all-time high score to a local text file.

## Technologies
- Python 3.x
- 	urtle module for rendering graphics and handling inputs.
- Object-Oriented Programming (OOP) architecture.

## Installation
1. Clone the repository:
   `ash
   git clone https://github.com/yourusername/snake-game.git
   cd snake-game
   `
2. No external dependencies are required.

## Usage
Run the game script to start playing:
`ash
python main.py
`

## Project Structure
- main.py: Game loop and screen configuration.
- snake.py: Snake object logic and movement.
- ood.py: Food generation logic.
- scoreboard.py: Score tracking and high score saving logic.
- data.txt: Stores the persistent high score.

## Requirements
- Python 3.9+

## Future Improvements
- Add difficulty levels to adjust the speed of the snake.
- Implement an overarching menu system.
- Add sound effects.

## License
This project is licensed under the MIT License.