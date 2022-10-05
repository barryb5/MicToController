import time
import keyboard
import numpy as np
import vgamepad as vg

gamepad = vg.VX360Gamepad()

while True:
    time.sleep(1)
    direction = [0, 0]
    if keyboard.is_pressed('a'):
        print("You pressed 'a'.")
        direction[0] = 1
    if keyboard.is_pressed('d'):
        print("You pressed 'd'.")
        direction[0] = -1
    if keyboard.is_pressed('w'):
        print("You pressed 'w'.")
        direction[1] = 1
    if keyboard.is_pressed('s'):
        print("You pressed 's'.")
        direction[1] = -1
    if keyboard.read_key() == "p":
        print("Exiting")
        break

    strength = 50

    input_strength = 0.5

    if strength >= 100:
        input_strength = 1
    elif strength >= 0:
        input_strength = strength/100


    if direction[0] == 0:
        angle = np.pi/2
    elif direction[1] == 0:
        angle = 0
    else:
        angle = np.pi/4

    x_direction = direction[0] * abs(np.cos(angle)*input_strength)
    y_direction = direction[1] * abs(np.sin(angle)*input_strength)
    print("Power: {0}".format(input_strength))
    print("X Direction: {0}".format(x_direction))
    print("Y Direction: {0}".format(y_direction))
    print("Calculated Power: {0}".format(np.sqrt(np.square(x_direction) + np.square(y_direction))))
    
    # gamepad.left_joystick_float(x_value_float=x_direction, y_value_float=y_direction)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button
    gamepad.update()
    # time.sleep(1)
    # gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button
    # gamepad.left_joystick_float(x_value_float=.9, y_value_float=0)
