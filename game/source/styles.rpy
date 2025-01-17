style default:
    properties gui.text_properties()


style gui_text:
    properties gui.text_properties("interface")

style button_text is gui_text:
    properties gui.text_properties("button")

style label_text is gui_text:
    size 90


style medium_frame:
    background Frame("gui/game_menu/misc/medium_frame.png", 20, 20)
    ysize 112
    # padding (30, 30, 30, 30)



style bar:
    base_bar Frame("gui/game_menu/preferences/bar.png")
    thumb "gui/game_menu/preferences/thumb.png"
    thumb_offset 8
    ysize 253
    xsize 700

style slider is bar

# EXTRA

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos 30
    background Solid("#000D")
    padding (10, 10, 10, 10)

style skip_text:
    size 70

style skip_triangle:

    font "DejaVuSans.ttf"
