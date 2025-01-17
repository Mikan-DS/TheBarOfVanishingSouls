screen say(who, what):


    frame:
        yalign 1.0
        xfill True
        ysize 789
        background "gui/textbox/colored.png"
        id "window"

        if who is not None:
            text who id "who":
                xalign .1
                yalign .17
                size 65

        frame:
            xsize .8
            ysize .5
            align (.5, .76)
            text what:
                id "what"


