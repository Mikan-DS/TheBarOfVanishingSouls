screen game_menu(title):

    frame:
        align (0.5, 0.5)
        xysize (3689, 2017)
        add "gui/game_menu/misc/game_menu_background.png"


        frame:
            xysize (1708, 324)
            yalign .05
            add "gui/game_menu/misc/label_frame.png"
            label title:
                yalign .5
                xpos 100

        vbox:
            spacing 80
            align (.05, .8)
            frame:
                xalign .5
                xysize (608, 1314)
                add "gui/game_menu/misc/navigation_frame.png"

                vbox:
                    align (0.5, 0.5)
                    spacing 40


                    if main_menu:
                        textbutton _("НАЧАТЬ ИГРУ") action Start()
                    else:
                        textbutton _("СОХРАНИТЬ") action ShowMenu("save")

                    textbutton _("ЗАГРУЗИТЬ") action ShowMenu("load")
                    textbutton _("НАСТРОЙКИ") action ShowMenu("preferences")
                    textbutton _("ОБ ИГРЕ") action ShowMenu("about")
                    textbutton _("ПОМОЩЬ") action ShowMenu("help")

                    if _in_replay:
                        textbutton _("ЗАКОНЧИТЬ КАТСЦЕНУ") action EndReplay(confirm=True)

                    elif not main_menu:
                        textbutton _("ГЛАВНОЕ МЕНЮ") action MainMenu()

                    if renpy.variant("pc"):
                        textbutton _("ВЫХОД") action Quit(confirm=not main_menu)
    

            button:
                xysize (424, 112)
                xalign .5
                
                frame:
                    add "gui/game_menu/misc/back_frame.png"
                    text _("Назад"):
                        align (0.5, 0.5)

                action Return()

        frame:
            xysize (2372, 1414)
            align (0.82, 0.62)

            transclude

screen game_menu_framed(title):
    use game_menu(title):
        frame:
            background "gui/game_menu/misc/large_frame.png"
            xysize (2372, 1314)
            padding (50, 50)
            align (0.5, 0.5)

            transclude