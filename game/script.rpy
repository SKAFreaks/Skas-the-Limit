# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jess = Character("Jess")
define mitch = Character("Mitch")
define mike = Character("Mike")
define zoe = Character("Zoe")
define danny = Character("Danny")
define rj = Character("RJ")
define damon = Character("Damon")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    mike "Shadow the Hedgehog is a bitchass motherfucker"

    mike "He pissed on my wife!"

    # This ends the game.

    return
