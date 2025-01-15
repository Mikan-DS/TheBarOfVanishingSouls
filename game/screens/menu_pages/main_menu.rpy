
image main_menu_background face_1:
    matrixcolor SaturationMatrix(.1)
    contains:
        "gui/main_menu/backgrounds/face_1/light.png"
    contains:
        "gui/main_menu/backgrounds/face_1/idle.png"
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)
    "gui/main_menu/backgrounds/face_1/revert.png" with dissolve
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)

image main_menu_background face_2:
    matrixcolor SaturationMatrix(.1)
    contains:
        "gui/main_menu/backgrounds/face_2/light.png"
    contains:
        "gui/main_menu/backgrounds/face_2/idle.png"
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)
    "gui/main_menu/backgrounds/face_2/revert.png" with dissolve
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)
     

image main_menu_background face_3:
    matrixcolor SaturationMatrix(.1)
    contains:
        "gui/main_menu/backgrounds/face_3/light.png"
    contains:
        "gui/main_menu/backgrounds/face_3/idle.png"
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)
    "gui/main_menu/backgrounds/face_3/revert.png" with dissolve
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)
     

image main_menu_background face_4:
    matrixcolor SaturationMatrix(.1)
    contains:
        "gui/main_menu/backgrounds/face_4/light.png"
    contains:
        "gui/main_menu/backgrounds/face_4/idle.png"
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)
    "gui/main_menu/backgrounds/face_4/revert.png" with dissolve
    linear .4 matrixcolor SaturationMatrix(1.0)
    .3
    linear .4 matrixcolor SaturationMatrix(.1)
     


image main_menu_background:
    parallel:
        "main_menu_background face_1" with dissolve
        pause 2.2
        "main_menu_background face_2" with dissolve
        pause 2.2
        "main_menu_background face_3" with dissolve
        pause 2.2
        "main_menu_background face_4" with dissolve
        pause 2.2
        repeat



transform main_menu_bounce:
    parallel:
        zoom 1.05
        ease 8.8 zoom 1.12
        ease 8.3 zoom 1.05
        repeat
    parallel:
        xalign 0.0
        ease 7.3 xalign 1.0
        ease 6.4 xalign 0.0
        repeat
    parallel:
        yalign 0.0
        ease 10.2 yalign 1.0
        ease 11.2 yalign 0.0
        repeat


transform button_slide(invert=1):
    xpos -1100*invert
    on idle:
        ease .2 xpos -1100*invert
    on hover:
        ease .2 xpos 0

screen main_menu():

    tag menu
    
    add "main_menu_background":
        at transform:
            main_menu_bounce

    vbox:
        spacing 400
        ypos 200
        button:
            at button_slide
            ysize 356
            xsize 1875
            frame:  
                add "gui/main_menu/button_frame.png"
                add "gui/main_menu/buttons/start.png":
                    yalign .5
                    xalign .0
            action NullAction()

        button:
            at button_slide
            ysize 356
            xsize 1875
            frame:  
                add "gui/main_menu/button_frame.png"
                add "gui/main_menu/buttons/load.png":
                    yalign .5
                    xalign .0
            action NullAction()

        button:
            at button_slide
            ysize 356
            xsize 1875
            frame:  
                add "gui/main_menu/button_frame.png"
                add "gui/main_menu/buttons/quit.png":
                    yalign .5
                    xalign .0
            action NullAction()
    vbox:

        spacing 400
        ypos 200
        xalign 1.0

        button:
            at button_slide(-1)
            ysize 356
            xsize 1875
            frame:  
                add "gui/main_menu/button_frame.png":
                    xzoom -1.0
                add "gui/main_menu/buttons/help.png":
                    yalign .5
                    xalign 1.0
            action NullAction()

        button:
            at button_slide(-1)
            ysize 356
            xsize 1875
            frame:  
                add "gui/main_menu/button_frame.png":
                    xzoom -1.0
                add "gui/main_menu/buttons/preferences.png":
                    yalign .5
                    xalign 1.0
            action NullAction()


        button:
            at button_slide(-1)
            ysize 356
            xsize 1875
            frame:  
                add "gui/main_menu/button_frame.png":
                    xzoom -1.0
                add "gui/main_menu/buttons/about.png":
                    yalign .5
                    xalign 1.0
            action NullAction()

    # vbox:
    #     align (0.5, 0.5)

    #     textbutton "start" action Start()

