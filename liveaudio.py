from subprocess import call
import numpy as np
import vgamepad as vg
import pygame, time
import sounddevice as sd
from pygame.locals import *
import keyboard

# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption('Pygame Keyboard Test')
# pygame.mouse.set_visible(0)

save_values = [0] * 10
gamepad = vg.VX360Gamepad()
gamepad.reset()

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    save_values.insert(len(save_values), int(volume_norm))
    save_values.pop(0)
    print(int(volume_norm))
    averaged_of_10 = sum(save_values) / len(save_values)
    print("Sofened list value: {0}".format(averaged_of_10))

    controller_output(averaged_of_10)

def controller_output(strength):
    #left right, up down
    direction = [0, 0]
    # Trust me on these numbers I tested them
    if keyboard.is_pressed('a'):
        print("You pressed 'a'.")
        direction[0] = -1
    if keyboard.is_pressed('d'):
        print("You pressed 'd'.")
        direction[0] = 1
    if keyboard.is_pressed('w'):
        print("You pressed 'w'.")
        direction[1] = 1
    if keyboard.is_pressed('s'):
        print("You pressed 's'.")
        direction[1] = -1

    input_strength = 0

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
    
    gamepad.left_joystick_float(x_direction, y_direction)
    gamepad.update()
    # gamepad.left_joystick(x_value=-10000, y_value=0)  # values between -32768 and 32767
    # gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button
    # gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button
    print("Power: {0}".format(input_strength))
    print("X Direction: {0}".format(x_direction))
    print("Y Direction: {0}".format(y_direction))
    print("Calculated Power: {0}".format(np.sqrt(np.square(x_direction) + np.square(y_direction))))
    


with sd.Stream(callback=print_sound):
    sd.sleep(100000)