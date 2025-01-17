style default:
    properties gui.text_properties()


style gui_text:
    properties gui.text_properties("interface")

style button_text is gui_text:
    properties gui.text_properties("button")

style label_text is gui_text:
    size 90


style medium_frame:
    background Frame("gui/game_menu/misc/medium_frame.png")
    ysize 112
    padding (20, 20, 20, 20)


style bar:
    base_bar Frame("gui/game_menu/preferences/bar.png")
    thumb "gui/game_menu/preferences/thumb.png"
    thumb_offset 8
    ysize 253
    xsize 1200

style slider is bar