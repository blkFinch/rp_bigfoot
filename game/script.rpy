# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sass")
define me = Character(_("Me"), color="#2ff5c7")
define dad = Character(_("Dad"), color="#cc941d")

default day = 1


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_bedroom

    "Boxes filled my new bedroom and the air still stank of fresh paint and carpet cleaner. We had gotten in to town two
        days ago and I still hadn't started unpacking."

    "I had fallen asleep fully clothed and woke up staring at the lumpy popcorn plaster on the ceiling"

    me "Oh shoot- I'm going to be late.. I gotta get to school"

    menu:
        "What should I do"

        "Go to school":
            "I decided to head to my first day at the new school"
            jump school
        
        "Stay home":
            "I continued to do nothing and go nowhere"

label school:

    scene bg_schoolroom
    with fade

    if day == 1:
        me "wow its the first day of school!"
        $ day = day + 1

        show sass
        with dissolve 

        s "Hello friend! I am sas o quatch"

        jump start
    else:
        me "its another day"


label end:

    # This ends the game.

    return
