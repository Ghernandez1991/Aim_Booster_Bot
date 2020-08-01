import pyautogui

#return the current xy coordinate of the mounse
pyautogui.position()
#take sceenshot of region of your computer monitor. This is the screenshot of the playing board.
iml = pyautogui.screenshot(region=(661, 334, 600, 450))
#save ot as an image
iml.save(r"C:\Users\Gabriel Hernandez\Desktop\Aim_Booster\savedimage.png")


#650, 275
