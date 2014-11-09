## Rock, Paper, Scissors!!!

Let’s make some mother fucking objects. Your goal is to create an interactive game of rock, paper, scissors using object oriented programming.

#### Description

First, the game should prompt the user for the “best out of” number (e.g. 5). Throughout this challenge, you should account for invalid inputs, and if one is entered you should reprompt the user until a valid one is entered.

Once the user inputs a valid number, the game should repeatedly prompt for the user’s hand. Again, account for invalid inputs in case the user does not enter one of rock, paper, or scissors (or r/p/s if you’d like). Once a valid input is entered, the game should output a single line stating the outcome of the round (something to the effect of your rock beats my scissors or your scissors loses to my rock where “your” is the user and “my” is the computer). This will continue until either the user or the computer wins, in which case a single line will be output beneath the last round’s outcome that declares the winner.

Finally, you should ask the user if they want to play again. Once again, make sure the input is a valid yes/no (or y/n). If they chose to play again, start from the beginning asking for the new “best out of” number. If they chose not to play again, exit the program.

#### Details

- You should define a minimum of 2 classes: one for the hands (rock, paper, and scissors), and one for the game itself (it will handle parsing the user’s input, scoring, determining a winner, etc). You are more than welcome to make either of those into multiple classes, and to make any other classes you’d like.
- There are no rules about how you should generate the computer’s hand. You may make it as smart or as dumb as you’d like. Note that if your game plays rock every round, you’ll probably score more poorly than if it reacts based on the user’s habits. I would consider random generation to be somewhere in the middle. Honestly, random should be your goal, unless you’re an overachiever.Artificial intelligence not required.
- To make sure everything is fair, you should already know what the computer’s hand is going to be BEFORE prompting the user to enter theirs. We’re not cheaters.
