transform hover_brightness(initial=0.0, hovered=.4, time_to_change=.3):
    matrixcolor BrightnessMatrix(initial)
    on idle:
        ease time_to_change matrixcolor BrightnessMatrix(initial)
    on hover:
        ease time_to_change matrixcolor BrightnessMatrix(hovered)


transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


    