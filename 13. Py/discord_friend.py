#!/usr/bin/env python
# coding: utf-8

# In[19]:


from pynput.mouse import Button, Controller
from time import sleep
import keyboard


# In[20]:


mouse = Controller()


# In[54]:


# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))


# In[55]:


Search_pos = (2430, 248)
BTN_pos = (3250, 233)


# In[48]:


def click_to_input():
    mouse.position = Search_pos
    mouse.press(Button.left)
    mouse.release(Button.left)
    
def click_to_add():
    mouse.position = BTN_pos
    mouse.press(Button.left)
    mouse.release(Button.left)


# In[49]:


#Clear input
def clear_input():
    for _ in range(10):
        click_to_input()
        keyboard.press_and_release("backspace")
        sleep(0.1)


# In[57]:


def do_input(arr):
    for i in arr:
        keyboard.write(i)
        sleep(0.1)


# In[58]:


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


# In[ ]:




