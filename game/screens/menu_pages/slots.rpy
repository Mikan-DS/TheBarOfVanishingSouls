screen save():

    tag menu

    use file_slots(_("Сохранить"))


screen load():

    tag menu

    use file_slots(_("Загрузить"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"), quick=_("Быстрые сохранения"))

    use game_menu(title):
        vbox:
            xalign .5
            
            spacing 200

            frame:
                xalign .5
                style "medium_frame"
                hbox:
                    align (0.5, 0.5)
                    spacing 40
                    
                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("Q") action FilePage("quick")

                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

            hbox:
                xalign .5
                box_wrap True
                spacing 30
                box_wrap_spacing 40

                for slot in range(1, 7):
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot, empty="gui/game_menu/slots/slot_background.png"):
                            xalign 0.5
                            xysize (config.thumbnail_width, config.thumbnail_height)

                        text FileTime(slot, format=_("%A, %B %d %Y, %H:%M")):
                            xalign .5

                        key "save_delete" action FileDelete(slot)
