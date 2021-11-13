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

    mike "The FitnessGram™ Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues.
The 20 meter pacer test will begin in 30 seconds. Line up at the start.
The running speed starts slowly, but gets faster each minute after you hear this signal.
A single lap should be completed each time you hear this sound.
Remember to run in a straight line, and run as long as possible.
The second time you fail to complete a lap before the sound, your test is over.
The test will begin on the word start.
On your mark, get ready, start."

    jump intro


label afterPronouns:
    narrator "Howdy"
    mike "Nice to meet you [narrator.name]. I hear you use [narrator.pSingular]/[narrator.pPossesive] pronouns."

    # This ends the game.


return
