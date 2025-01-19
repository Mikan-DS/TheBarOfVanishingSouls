init offset = -4

init python:
    # gui.init(1920, 1080)
    gui.init(3840, 2160)

define config.check_conflicting_properties = True

define config.name = _("The Bar of Vanishing Souls")


define config.version = "0.2025.01.17.0"



define build.name = "The_Bar_of_Vanishing_Souls"


define config.enter_transition = dissolve
define config.exit_transition = dissolve



define config.intra_transition = dissolve



define config.after_load_transition = None

define config.window_icon = "gui/window_icon.png"

define config.end_game_transition = None


define config.thumbnail_width = 768
define config.thumbnail_height = 432

define config.window = "show"


define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# default preferences.volume.voice = 0.0

define config.main_menu_music = music_Kevin_MacLeod_Faster_Does_It