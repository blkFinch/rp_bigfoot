screen hello_world():
    text "Hello World"

screen day_count(day):
    frame:
        xpos 50
        ypos 50

        hbox:
            text "Day "
            text str(day)

screen input_name():
    window:
        vbox: 
            text "Enter your name"
            input default "Sam"