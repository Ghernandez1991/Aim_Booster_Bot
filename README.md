# Aim_Booster_Bot
Create a bot for Aimbooster Flash game.

URL TO GAME = http://www.aimbooster.com/

Bot uses pyautogui to automatically click the center of the bullseye on the Flash game. 

---------------------------------------------Line 27
Users will need to screenshot the game region(see savedimage.png) on their monitor in order for pyautogui to recoginze what it is searching for , and what to click.
The region (region=(661, 334, 600, 450)) is specific to my monitor(1920 x 1080) and will change on a different sized monitor. 


---------------------------------------------Line 31-40
We are using a nested for loop to go through each pixel(starting at 0) for both the width of the picture(width) and the height(height) and we are doing it in increments of 5. We are essentially
scanning each 5x5 area and looking for the RGB value we need to click. 

---------------------------------------------- Line 34
We capture the rgb values by using the .getpixel method of x,y from the for loops. 

----------------------------------------------Line 36
THe RGB(Red , Green , Blue) value we are looking for is 195. Use an if statement to tell the program if it sees an value of 195 for the b value, to click . My screen shot starts at pizel 661 and 334, so we add the pixel value of x and y to them to start where the screen shot is. 
This will differ from user to user so make sure to double check this. 


Check out youtube to see the bot in action. 
https://youtu.be/ZYXHzoSaUuQ
