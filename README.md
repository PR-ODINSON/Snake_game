# Enhanced Snake Game

## Overview
The **Enhanced Snake Game** is a modern twist on the classic snake game, developed using Python and Pygame. It features customizable difficulty levels, a toggleable wall-collision mode, and dynamic speed adjustments as the game progresses.

## Features
- **Difficulty Levels**: Choose between Easy, Medium, and Hard modes.
- **Wall Collision**: Toggle walls ON/OFF for a different gameplay experience.
- **Dynamic Speed**: The snake's speed increases after every 50 points.
- **Customizable Colors**: Alternating tail colors for a vibrant visual.
- **Background Music and Sound Effects**: Background music and eating sound effects enhance the gaming experience.
- **Home Screen**: A welcoming UI to select settings and start the game.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/enhanced-snake-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd enhanced-snake-game
   ```
3. Install the required dependencies:
   ```bash
   pip install pygame
   ```
4. Place the audio files `Snake_bite.mp3` and `BG_snake_sound.mp3` in the project directory.

## How to Play
1. Run the game:
   ```bash
   python snake_game.py
   ```
2. On the home screen:
   - Select difficulty by pressing `1`, `2`, or `3`.
   - Toggle walls ON/OFF by pressing `W`.
   - Press `SPACE` to start the game.
3. Use the arrow keys to control the snake:
   - `UP`, `DOWN`, `LEFT`, `RIGHT`.
4. Collect the red food squares to grow the snake and increase your score.
5. Avoid colliding with yourself (or walls if they are ON) to prevent losing.
6. If you lose:
   - Press `C` to play again.
   - Press `Q` to quit.

## Controls
| Key        | Action                      |
|------------|-----------------------------|
| `1`        | Select Easy mode            |
| `2`        | Select Medium mode          |
| `3`        | Select Hard mode            |
| `W`        | Toggle walls ON/OFF         |
| `SPACE`    | Start the game              |
| `UP`       | Move snake up               |
| `DOWN`     | Move snake down             |
| `LEFT`     | Move snake left             |
| `RIGHT`    | Move snake right            |
| `C`        | Play again after losing     |
| `Q`        | Quit the game               |

## Game Logic
- The snake starts with a length of 1 and grows longer as it eats food.
- The game speed increases after every 50 points scored.
- If walls are enabled, colliding with the screen edges results in a game over.
- If walls are disabled, the snake wraps around the screen edges!

## File Structure
```
.
├── snake_game.py          # Main game script
├── Snake_bite.mp3         # Sound effect for eating food
├── BG_snake_sound.mp3     # Background music
├── README.md              # Documentation
```

## Requirements
- Python 3.7+
- Pygame library

## Future Enhancements
- Add new power-ups and obstacles.
- Implement multiplayer mode.
- Save and display high scores.
- Add themes and customizable snake skins.

## Contributing
Contributions are welcome! If you'd like to improve this project:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details!

## Acknowledgments
- Thanks to the developers of [Pygame](https://www.pygame.org/) for providing a fantastic library for game development.
- Inspired by the classic snake game and modern gaming elements.

