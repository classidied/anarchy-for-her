'''
check:
getch()
try pynput thing again

from pynput import keyboard

print('Press s or n to continue:')

with keyboard.Events() as events:
    # Block for as much as possible
    event = events.get(1e6)
    if event.key == keyboard.KeyCode.from_char('s'):
        print("YES")


goal is to simulate what a webserver button would do 
if key is pressed, take that one char as input and then simulate an enter key being pressed??? 
or like if getch does that for you just loop it forever
and whichever key is pressed call a function ez
just move it clockwise/counterclockwise for like 0.2s until the next instruction
this means there will always be a 0.2s delay in the instructions but oh well????

forward/backward/left/right | .py
call with os module in main 

firstly
check if it can even handle input
if key is pressed echo the key that was pressed 

use os
- login with ssh to rasppi
- use pynput maybe


alt caveman brain plan
- on key press from mac, open a terminal and ssh into the pi


'''