from re import A
from tkinter import N
from subprocess import call
import numpy as np
import vgamepad as vg
import pygame, time
import sounddevice as sd
from pygame.locals import *
import sys

# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Controller Emulation Test')
pygame.mouse.set_visible(0)
controller = pygame.joystick.Joystick(0)
controller.init()

save_values = [0] * 10
recent_strength = 0
gamepad = vg.VX360Gamepad()
gamepad.reset()

button_holdings = [False, False, False, False, False]

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    save_values.insert(len(save_values), int(volume_norm))
    save_values.pop(0)
    # print(int(volume_norm))
    averaged_of_10 = sum(save_values) / len(save_values)
    print("Sofened list value: {0}".format(averaged_of_10))
    recent_strength = averaged_of_10

    # controller_output(averaged_of_10)
    # controller_output(50)

def controller_output(strength):
    #left right, up down
    direction = [0, 0]
    # Trust me on these numbers I tested them
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Controller inputs
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 1:
                button_holdings[0] = True
                print("You pressed green.")
            if event.button == 2:
                button_holdings[1] = True
                print("You pressed red.")
            if event.button == 3:
                button_holdings[2] = True
                print("You pressed yellow.")
            if event.button == 0:
                button_holdings[3] = True
                print("You pressed blue.")
            if event.button == 4:
                button_holdings[4] = True
                print("You pressed orange.")

        if event.type == pygame.JOYBUTTONUP:
            # Green
            if event.button == 1:
                button_holdings[0] = False
                print("Released green")
            # Red
            if event.button == 2:
                button_holdings[1] = False
                print("Released red")
                
            # Yellow
            if event.button == 3:
                button_holdings[2] = False
                print("Released Yellow")
            # Blue
            if event.button == 0:
                button_holdings[3] = False
                print("Released Blue")
            # Orange
            if event.button == 4:
                button_holdings[4] = False
                print("Released orange")

    if (button_holdings[0]):
        direction[0] += -1
    if (button_holdings[1]):
        direction[0] += 1
    if (button_holdings[2]):
        direction[1] += 1
    if (button_holdings[3]):
        direction[1] += -1
    

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
    # print("Power: {0}".format(input_strength))
    print("X Direction: {0}".format(x_direction))
    print("Y Direction: {0}".format(y_direction))
    # print("Calculated Power: {0}".format(np.sqrt(np.square(x_direction) + np.square(y_direction))))
    


with sd.Stream(callback=print_sound):
    while (True):
        # time.sleep(1)
        controller_output(recent_strength)

