screen preferences():
    tag menu

    use game_menu(_("НАСТРОЙКИ")):

        vbox:
            ypos 100
            spacing 30
            hbox:
                xsize 900
                frame:
                    text _("Отображение") align (0.5, 0.5)
                    style "medium_frame"

            
                frame:
                    text _("Пропуски") align (0.5, 0.5)
                    style "medium_frame"

            frame:
                background Frame("gui/game_menu/slots/slot_background.png")
                xysize (800, 200)

                hbox:
                    vbox:
                        textbutton _("Окно") action Preference("display", "window")
                        textbutton _("Полный") action Preference("display", "fullscreen")


            vbox:
                label _("Text Speed")
                bar value Preference("text speed")

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

            vbox:
                label _("Music Volume")

                bar value Preference("music volume")


                label _("Sound Volume")

                bar value Preference("sound volume")

        # hbox:
        #     style_prefix "preferences_boxes"

        #     align (.5, .5)
        #     box_wrap True
        #     spacing 60
        #     box_wrap_spacing 30

        #     frame:
        #         vbox:
        #             label _("Display")
        #             textbutton _("Window") action Preference("display", "window")
        #             textbutton _("Fullscreen") action Preference("display", "fullscreen")

        #     frame:
        #         vbox:
        #             label _("Skip")
        #             textbutton _("Unseen Text") action Preference("skip", "toggle")
        #             textbutton _("After Choices") action Preference("after choices", "toggle")

        #     frame:
        #         vbox:
        #             label _("Text Speed")
        #             bar value Preference("text speed")

        #             label _("Auto-Forward Time")
        #             bar value Preference("auto-forward time")

        #     frame:
        #         vbox:
        #             label _("Music Volume")

        #             bar value Preference("music volume")


        #             label _("Sound Volume")

        #             bar value Preference("sound volume")