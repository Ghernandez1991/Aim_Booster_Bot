
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# http://www.aimbooster.com/

# gives us time to load the game
time.sleep(2)
# function to click


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # sometimes the click will not registered if you click to fast
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)


# press s to stop the bot- when it is not pressed, the bot will continue
while keyboard.is_pressed('s') == False:
    # store game area as variable pic using region--this looks for the game area on screen
    pic = pyautogui.screenshot(region=(661, 334, 600, 450))
    # store the width and height
    width, height = pic.size
    # RGB value of the center of the circle is 255,219,195
    for x in range(0, width, 5):#starting at 0,to the width of the screen. loop every 5 pixels
        for y in range(0, height, 5):#starting at 0,to the height of the screen. loop every 5 pixels

            r, g, b = pic.getpixel((x, y))#scan the screen shot and get the RGB values 
        # if the blue value = blue value of the circle, we want to click
            if b == 195:
                # our screen shot starts at pizel 661 and 334, so we add the pixel value of x and y to them to start where the screen shot is
                click(x+661, y+334)
                time.sleep(0.05)
                break
