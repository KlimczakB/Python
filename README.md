# Python
To be able to play you need an "images" folder along with the pictures and the script project.py.

In this project, I wanted to create the Rock/Paper/Scissors game in Python with a Tkinter GUI. 
It's a single-player game(player vs computer). In this game you have three choices: rock, paper, and scissors. The computer has the same choice, it randomly selects one of the options. Then the player's and computer's choices are compared with each other. As a result of the comparison: you win, you lose or there is a draw. Every time someone wins they get a point, for a draw and a loss there are no points.

Game rules:
- Rock wins against scissors 
- Paper wins against rock
- Scissors wins against paper

This game has no end, you can play as long as you like. The game result is saved to file: result.txt. 
If you start a new game, the result of the previous game will remain saved in the file.

The tkinter module was used to prepare the graphical interface. 
In the project I used widgets such as:
- Label
- Button
- Text
- Frame 

Also geometry managers (.pack, .grid) and multiple windows(Toplevel).

ATTENTION! The buttons for selecting one of the 3 options by the player have pictures instead of text. The pictures are saved in the "images" folder. You need this folder!
