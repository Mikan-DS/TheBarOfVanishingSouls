screen preferences():
    tag menu

    use game_menu(_("НАСТРОЙКИ")):


        hbox:
            spacing -90
            vbox:
                ypos 100
                spacing 600
                
                hbox:
                    spacing 30
                    vbox:
                        xsize 500
                        spacing 10
                        frame:
                            text _("Отображение")  align (0.5, 0.8)
                            style "medium_frame"
                            xfill True

                        frame:
                            background Frame("gui/game_menu/slots/slot_background.png")
                            padding (20, 20, 20, 20)
                            xfill True
                            vbox:
                                xalign 0.5
                                textbutton _("Окно") action Preference("display", "window")
                                textbutton _("Полный") action Preference("display", "fullscreen")

                    vbox:
                        xsize 500
                        spacing 10
                        frame:
                            text _("Пропуски") align (0.5, 0.8)
                            style "medium_frame"
                            xfill True

                        frame:
                            background Frame("gui/game_menu/slots/slot_background.png")
                            padding (20, 20, 20, 20)
                            xfill True
                            vbox:
                                xalign 0.5
                                textbutton _("Весь текст") action Preference("skip", "toggle")
                                textbutton _("После выборов") action Preference("after choices", "toggle")

                vbox:
                    spacing 30
                    hbox:
                        xsize 550
                        spacing 30
                        frame:
                            text _("Скорость текста") align (0.5, 0.8)
                            style "medium_frame"
                            xfill True
                            yalign .5
                        bar value Preference("text speed")
                    hbox:
                        xsize 550
                        spacing 30
                        frame:
                            text _("Автопереход") align (0.5, 0.8)
                            style "medium_frame"
                            xfill True
                            yalign .5
                        bar value Preference("auto-forward time")

            vbox:
                yalign .34
                xsize 1250
                frame:
                    text _("Громкость") align (0.5, 0.8)
                    style "medium_frame"
                    xfill True
                    yalign .5

                hbox:
                    xsize 550
                    spacing 30
                    frame:
                        text _("Музыка") align (0.5, 0.8)
                        style "medium_frame"
                        xfill True
                        yalign .5
                    bar value Preference("music volume")

                hbox:
                    xsize 550
                    spacing 30
                    frame:
                        text _("Звуки") align (0.5, 0.8)
                        style "medium_frame"
                        xfill True
                        yalign .5
                    bar value Preference("sound volume")

                hbox:
                    xsize 550
                    spacing 30
                    frame:
                        text _("Голос") align (0.5, 0.8)
                        style "medium_frame"
                        xfill True
                        yalign .5
                    bar value Preference("voice volume")

