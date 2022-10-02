from subprocess import call
import sounddevice as sd
import numpy as np
# import vgamepad as vg
import pygame, time
from pygame.locals import *
import keyboard

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(0)

save_values = [0] * 10
# gamepad = vg.VX360Gamepad()

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    save_values.insert(len(save_values), int(volume_norm))
    save_values.pop(0)
    print(int(volume_norm))
    averaged_of_100 = sum(save_values) / len(save_values)
    print("Sofened list value: {0}".format(averaged_of_100))

def controller_output(strength):
    # gamepad.left_joystick_float(x_value_float=-0.5, y_value_float=0.0)
    #left right up down
    direction = [0, 0, 0, 0]
    if keyboard.read_key() == "a":
        print("You pressed 'a'.")
        direction[0] = 1
    if keyboard.read_key() == "d":
        print("You pressed 'd'.")
        direction[1] = 1
    if keyboard.read_key() == "w":
        print("You pressed 'w'.")
        direction[2] = 1
    if keyboard.read_key() == "s":
        print("You pressed 's'.")
        direction[3] = 1

    


# with sd.Stream(callback=controller_output):
    # sd.sleep(10000)