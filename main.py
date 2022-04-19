 #exercice1
    from configparser import BasicInterpolation
    from decimal import BasicContext
    from tkinter import Button


    var1 = 0

    def on_button_pressed_b():
        global var1
        if True:
            BasicInterpolation.show_string("" + str((input.temperature())))
        else:
            var1 = input.sound_level()
    input.on_button_pressed(Button.B, on_button_pressed_b)

    def on_forever():
        pass
    BasicContext.forever(on_forever)

    #exercice2
is_logo_pressed = False
def on_forever():
    global is_logo_pressed
    is_logo_pressed = True
    if input.logo_is_pressed():
        is_logo_pressed = False
    if is_logo_pressed == True:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)
#exercice3
def on_sound_loud():
    basic.show_icon(IconNames.SMALL_HEART)
input.on_sound(DetectedSound.LOUD, on_sound_loud)