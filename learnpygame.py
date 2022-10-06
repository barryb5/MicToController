# importing pygame module
from tkinter import N
import pygame
from pygame.locals import *
import time
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Controller Emulation Test')
pygame.mouse.set_visible(0)
controller = pygame.joystick.Joystick(0)
controller.init()

print("Controllers: {0}".format(pygame.joystick.get_count()))
print("Power: {0}".format(controller.get_power_level()))

for i in range(controller.get_numbuttons()):
    button = controller.get_button(i)
    print("Button {0} Value: {1}".format(i, button))

for i in range (controller.get_numaxes()):
    print("Number of axes: {0}".format(controller.get_numaxes()))


# creating a running loop

# Green Red Yellow Blue Orange
buttonHoldings = [False, False, False, False, False]

while True:
    time.sleep(1)
    # Checks Holdings
    if (buttonHoldings[0] == True):
        print("Holding Green")
    if (buttonHoldings[1] == True):
        print("Holding Red")
    if (buttonHoldings[2] == True):
        print("Holding Yellow")
    if (buttonHoldings[3] == True):
        print("Holding Blue")
    if (buttonHoldings[4] == True):
        print("Holding Orange")

    # creating a loop to check events that
    # are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                print("You pressed 'a'.")
            if event.key == K_d:
                print("You pressed 'd'.")
            if event.key == K_w:
                print("You pressed 'w'.")
            if event.key == K_s:
                print("You pressed 's'.")
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")
        
        if event.type == pygame.JOYBUTTONDOWN:
            # Green
            if event.button == 1:
                buttonHoldings[0] = True
                print("Pressed green")
            # Red
            if event.button == 2:
                buttonHoldings[1] = True
            # Yellow
            if event.button == 3:
                buttonHoldings[2] = True
            # Blue
            if event.button == 0:
                buttonHoldings[3] = True
            # Orange
            if event.button == 4:
                buttonHoldings[4] = True
            
        if event.type == pygame.JOYBUTTONUP:
            # Green
            if event.button == 1:
                buttonHoldings[0] = False
                print("Released green")
            # Red
            if event.button == 2:
                buttonHoldings[1] = False
            # Yellow
            if event.button == 3:
                buttonHoldings[2] = False
            # Blue
            if event.button == 0:
                buttonHoldings[3] = False
            # Orange
            if event.button == 4:
                buttonHoldings[4] = False
            
        if event.type == pygame.JOYAXISMOTION:
            if event.axis == 2:
                print("You pressed the long thing")

            # if event.axis == 2:
                # print("You pressed the long thing")
            # if event.axis == 3:
                # print("You pressed the something else")
            
            print("Axis Motion")
        if event.type == pygame.JOYHATMOTION:
            if event.hat == 0:
                print("You pressed the strummer")

            print("Hat motion")
            