---

Python Tkinter Racing Game

A simple car racing game built with Python Tkinter and Pillow (PIL) where the player controls a car to dodge enemy cars and score points. The game also keeps track of the highest score using a CSV file.


---

🎮 Features

Player Movement: Move your car left and right using arrow keys.

Enemy Cars: Multiple enemy cars appear and move down the screen.

Collision Detection: Game ends when the player collides with an enemy car.

Scoring System: Score increases every time an enemy car passes.

High Score Tracking: Highest score is saved in highscore.csv.

Game Over Screen: Background turns white and displays Game Over.



---

📂 Project Structure

.
├── main.py               # Main game file (your code)
├── highscore.csv         # Stores the highest score
├── assets/
│   ├── Racetrack.png      # Background image
│   ├── player_car.png     # Player car image
│   └── enemy_car.png      # Enemy car image
└── README.md

> Note: Replace player_car.png and enemy_car.png with your actual image paths.




---

⌨️ Controls

Key	Action

←	Move car left
→	Move car right



---

📦 Requirements

Python 3.x

Tkinter (comes pre-installed with Python)

Pillow (pip install pillow)



---

▶️ How to Run

1. Clone or download the project.


2. Place the required images in the correct paths.


3. Install Pillow if not installed:

pip install pillow


4. Run the Python file:

python main.py




---

🏆 Scoring & High Score

Your score increases each time an enemy car crosses the screen.

The highest score is stored in highscore.csv and updated automatically.



---

⚡ Future Improvements

Add difficulty increase with time (faster enemies).

Add background music or sound effects.

Add a restart option without closing the program.

Display the final score in the game-over screen.



---
