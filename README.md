For this assignment you will be creating an interface for two humans to play a simple game of "Pick Up Sticks". Here's how the game is played in the "real world":
  - The game begins with a number of sticks on a table (between 10 and 100)
  - Each player, in turn, takes between 1-3 sticks off the table.
  - The player to take the last stick loses.
Your job is to build a virtual version of the game using Python.

Part 1: Single Player Game

Begin by asking the user for a number of sticks to be used in the game. Only accept numbers between 10 and 100 - if the user supplies a number outside of this range you should re-prompt them.

Next, continually announce to the user how many sticks are on the table and ask the user to enter in a number of sticks to take away. Only accept choices of 1,2 or 3 sticks - anything else should cause an error message to be displayed. Once a valid number of sticks has been entered you should deduct that # of sticks from the total number of sticks in the game. When you reach 0 sticks left the game is over.

Program 1b: Two Player Game

As you can see, the single player version of this game isn't very fun. To make things more interesting we are now going to add in an element of competition. For this part you will be implementing a two player game where players take turns taking sticks from the table. The same rules apply - each player can only take 1, 2 or 3 sticks per turn. The player who takes the last stick off of the table is the loser.
