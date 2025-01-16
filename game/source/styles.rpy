style default:
    properties gui.text_properties()


style gui_text:
    properties gui.text_properties("interface")

style button_text is gui_text:
    properties gui.text_properties("button")

style label_text is gui_text:
    size 36


style medium_frame:
    background Frame("gui/game_menu/misc/medium_frame.png")
    ysize 112
    padding (20, 20, 20, 20)


style bar:
    base_bar Frame("gui/game_menu/misc/medium_frame.png", 20, 20)
    thumb "gui/game_menu/preferences/thumb.png"
    thumb_offset 8
    ysize 112

style slider is bar