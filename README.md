# rock-paper-scissors

Milestone 1 -
The model was trained using the website Teachable Machine to recognise weather a rock, paper or scissors sigh is being made. This model was then downloaded for later use in the project, to provide the users input to the game.

Milestone 2 - As part of this milestone the rock paper scissors program was made without the Machine vision model. This was done in order to test the programming used for running the game, for this to work the input from the machine vision model was replaced by a user input function.

Milestone 2.1 - The first subsection of this milestone was setting up the environment. The enviroment was set up using python 3.8 to assure compatibility with tensorflow. Next opencv-python, tensorflow and ipykernel were installed into the environment.

Milestone 2.2 - The next few subsections are related to writing the python code that simulated the rock paper scissors game. The first section that was added was an input for the player and the computer. The players input is made up of an input function and a while loop to ask them again if they input something incorrect. The computers input was made up of a random number generator to create numbers between 0 and 2 that were then turned into a string.

Milestone 2.3 - The next milestone was making a system to decide the winner. First i created a new variable called results, this was made up of the combined strings of the computer and player input. This would mean the results variable was made up of a number from the computer and a word from the player. The results variable is then looked up in a dictionary that gives either won, lost or drew.

Milestone 2.4 - the next step was making the game have multiple rounds then have a player win after a certain amount of victories. This was achieved by setting up a counter variable for the computer and player. Most of the code for the game that would then be used for playing the game was placed inside a while loop that would carry on going until one of the players got the the required number of points. A system that added a value to the players counters if they won was then added.
