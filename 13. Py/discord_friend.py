#!/usr/bin/env python
# coding: utf-8

from pynput.mouse import Button, Controller
from time import sleep
import keyboard

mouse = Controller()
# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

Search_pos = (2430, 248)
BTN_pos = (3250, 233)

def click_to_input():
    mouse.position = Search_pos
    mouse.press(Button.left)
    mouse.release(Button.left)
    
def click_to_add():
    mouse.position = BTN_pos
    mouse.press(Button.left)
    mouse.release(Button.left)

#Clear input
def clear_input():
    for _ in range(10):
        click_to_input()
        keyboard.press_and_release("backspace")
        sleep(0.1)

def do_input(arr):
    for i in arr:
        keyboard.write(i)
        sleep(0.1)

for i in range(200,1000):
    clear_input()
    sleep(0.25)
    click_to_input()
    sleep(0.4)
    do_input(["F","l","y","n","n","#","0",str(i)])
    sleep(0.5)
    click_to_add()
    sleep(1.5)
    keyboard.press_and_release("enter")
    sleep(7)