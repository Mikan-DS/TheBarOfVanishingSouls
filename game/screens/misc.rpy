screen confirm(message, yes_action, no_action):

    modal True
    zorder 200

    frame:
        align (0.5, 0.5)
        background Solid("#000D")
        padding (60, 60, 60, 60)
        vbox:
            xalign .5
            yalign .5
            spacing 45
            label _(message):
                xalign 0.5
                text_textalign .5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Пропуск")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        background Solid("#0008")
        text "[message!tq]"

    timer 3.25 action Hide('notify')
