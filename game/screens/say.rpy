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
                font gui.name_text_font

        frame:
            xsize .8
            ysize .5
            align (.5, .76)
            text what:
                id "what"


screen choice(items):
    style_prefix "choice"

    vbox:
        spacing 30
        xsize 900
        align (0.5, 0.5)
        for i in items:
            button:
                at hover_brightness(0,.1)
                xfill True
                background Frame("gui/game_menu/misc/medium_frame.png", 20, 20, 20, 20)
                text i.caption xalign .5
                padding (20, 50, 20, 20)
                action i.action
            # textbutton i.caption:
            #     background Frame("gui/game_menu/misc/medium_frame.png", 20, 20)
            #     action i.action
            #     xfill True
            #     text_textalign .5
            #     align (0.5, 0.5)