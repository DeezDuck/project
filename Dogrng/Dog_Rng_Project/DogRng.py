#importing libraries
import pygame
import sys
import time
pygame.init()
import random
rolldir = ""
import tkinter
from tkinter import *
from tkinter import messagebox
specialevent = False
rolls = 0
def msgbox(msg):
    window = tkinter.Tk()
    window.wm_withdraw()
    tkinter.messagebox.showinfo(title="...", message=msg)
    window.destroy()
    return None


programIcon = pygame.image.load('icon.png')

pygame.display.set_icon(programIcon)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def roll():
    fifty = 0
    whatyougot = ""
    currentroll = random.randint(1, 10000)
    specialroll = random.randint(1, 100000)
    onemill = 0

    if specialroll == 50000:
        msgbox("...")
        time.sleep(0.5)
        msgbox("...")
        time.sleep(1)
        print(specialroll)
        print(whatyougot)
        whatyougot = "HARLEY, AN AUSSIE 1 IN 100,000"
        return whatyougot
    else:
        fifty = random.randint(1, 50000)
    if fifty == 25000:
        msgbox("...")
        time.sleep(0.5)
        msgbox("...")
        time.sleep(1)
        whatyougot = "KALI, A GOLDEN RETRIVER 1 IN 50K"
        print(onemill)
        print(whatyougot)
        return whatyougot
    else:
        onemill = random.randint(1, 1000000)
    if onemill ==500000:
        msgbox("...")
        time.sleep(0.5)
        msgbox("...")
        time.sleep(1)
        whatyougot = "WILLOW, AN AUSSIE 1 IN 1,000,000"
        print(onemill)
        print(whatyougot)
        return whatyougot
    print(currentroll)


    if specialroll != 50000 and onemill != 500000 and fifty != 50000:
             if currentroll <= 5000:
                     whatyougot = "Common golden retriver 1 in 2"
                     rolldir = "dog images/golden.png"
                     return whatyougot
             elif currentroll >5000 and currentroll < 7500:
                 whatyougot = "uncommon weiner dog 1 in 4"
                 rolldir = "dog images/wienerdog.png"
                 return whatyougot
             elif currentroll > 7500 and currentroll < 8750:
                 whatyougot = "rare german shepherd 1 in 8"
                 rolldir = "dog images/german"
                 return whatyougot
             elif currentroll > 8750 and currentroll < 9375:
                 whatyougot = "ultra rare pomeranian 1 in 16 "
                 rolldir = "dog images/pomeranian"
                 return whatyougot
             elif currentroll > 9375 and currentroll < 9500:
                 whatyougot = "legendary chiwawa >:) 1 in 80 "
                 rolldir = "dog images/chiwawa.jfif"
                 return whatyougot
             elif currentroll > 9500 and currentroll < 9550:
                 whatyougot = "ultra legendary poodle 1 in 200 "
                 rolldir = "dog images/poodle.jpg"
                 return whatyougot
             elif currentroll > 9550 and currentroll < 9575:
                 specialevent=True


                 whatyougot = "mythical pug  1 in 400 "
                 rolldir = "dog images/pug.jpg"
                 return whatyougot
             elif currentroll > 9575 and currentroll < 9600:
                 specialevent=True


                 whatyougot = "mythical french bull dog  1 in 400 "
                 rolldir = "dog images/french bull dog.jpg"
                 return whatyougot
             elif currentroll > 9600 and currentroll < 9700:
                 whatyougot = "glitch doog 1 in 100"
                 rolldir = "dog images/shiba inu.png"
                 return whatyougot
             elif currentroll > 9700 and currentroll < 9710:
                 specialevent=True
                 msgbox("...")
                 time.sleep(1)
                 whatyougot = "doge 1 in 1000"
                 rolldir = "dog images/doge.png"
                 return whatyougot
             elif currentroll > 9710 and currentroll < 9800:
                 whatyougot = "sephora dog  1 in 110"

                 return whatyougot
             elif currentroll > 9800 and currentroll < 9900:
                 whatyougot = "american dog  1 in 100"
                 return whatyougot
             elif currentroll == 9901:


                 msgbox("...")
                 time.sleep(1)
                 whatyougot ="chicken nugget dog 1 in 10,000"
                 return whatyougot
             elif currentroll == 9902:

                 msgbox("...")
                 time.sleep(1)
                 whatyougot = "AUSTRALIAN SHEPHERD 1 IN 10,000"

                 return whatyougot
             elif currentroll > 9903 and currentroll <= 9913:

                 msgbox("...")
                 time.sleep(1)
                 whatyougot = "AUSSIE BABY DOG 1 IN 1000"
                 return whatyougot
             else:
                 whatyougot = "?? NULL DOOG ??"
                 return whatyougot





#functions/classes


# setting screen size and background color
screen = pygame.display.set_mode((600,500))
screen_width = 640
screen_height = 480
screen.fill([255, 255, 255])
pygame.display.set_caption('Dog Rng')
BackGround = Background('Dog_Rng_Project/background.png', [0, 0])
player_x = 240
player_y = 200
#player image
font = pygame.font.Font('freesansbold.ttf', 32)
button_surface = pygame.Surface((150, 50))
text = font.render("Roll", True, (244, 244, 244))
text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
rollevent = ""
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
currentdawgtxt = "Current dawg: None"
X = 640
Y = 480

# create a rectangular object for the
# text surface object



# Create a pygame.Rect object that represents the button's boundaries
button_rect = pygame.Rect(240, 400, 150, 50)  # Adjust the position as needed
textRect2 = text.get_rect()
textRect3 = text.get_rect()
textRect4 = text.get_rect()
font = pygame.font.Font('freesansbold.ttf', 24)

# create a text surface object,
# on which text is drawn on it.
text2 = font.render(currentdawgtxt, True, black, white)

text3 = font.render("Space to toggle autoclicker: off", True, black, white)
text4 = font.render("Rolls: " + str(rolls), True, black)
# create a rectangular object for the
# text surface object
textRect2 = text.get_rect()
textRect3.center = (150, 30)
textRect4.center = (100, 300)


# set the center of the rectangular object.
textRect2.center = (27, 80)
# set the center of the rectangular object.
bgt = False
cooldowntrue = False
cooldown = 0.2
autocooldown = 0.35
autoclicker = False
kos = False
screen = pygame.display.set_mode((screen_width, screen_height))
#the main loop for the game
while True:

    #the code to close when you call the function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                autoclicker = not autoclicker
    #coloring the screen
    #flipping the display
    screen.blit(BackGround.image, BackGround.rect)
    checking = False

    if autoclicker == True and checking == False and cooldowntrue == False:
        rollevent = roll()
        rolls = rolls + 1
        time.sleep(autocooldown)
        print(rollevent)
        if rollevent == "mythical french bull dog  1 in 400 ":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True
        if rollevent == "mythical pug  1 in 400 ":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True
        if rollevent == "doge 1 in 1000":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True

        if rollevent == "chicken nugget dog 1 in 10,000":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True
        if rollevent == "AUSTRALIAN SHEPHERD 1 IN 10,000":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True
        if rollevent == "AUSSIE BABY DOG 1 IN 1000":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True
        if rollevent == "HARLEY, AN AUSSIE 1 IN 100,000":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True
        if rollevent == "WILLOW, AN AUSSIE 1 IN 1,000,000":
            autoclicker = False
            kos = messagebox.askyesno("Would you like to keep: " + rollevent, "Would you like to keep: " + rollevent)
            if kos == True:
                currentdawgtxt = "Current dawg: " + rollevent
            autoclicker = True



    # Check for the mouse button down event


    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and cooldowntrue == False and autoclicker == False:
        # Call the on_mouse_button_down() function
        rollevent = roll()
        rolls = rolls + 1
        print(rollevent)
        kos = messagebox.askyesno("Would you like to keep: " +rollevent, "Would you like to keep: " +rollevent)
        if kos == True:
         currentdawgtxt = "Current dawg: " + rollevent
        print(kos)
        cooldowntrue == True
        time.sleep(cooldown)
        cooldowntrue == False

    text2 = font.render(currentdawgtxt, True, black, white)
    text4 = font.render("Rolls: " + str(rolls), True, black)
    if autoclicker == False:
        text3 = font.render("Space to toggle autoclicker: off", True, black )
    else:
        text3 = font.render("Space to toggle autoclicker: on", True, black)

    # Check if the mouse is over the button. This will create the button hover effect
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, (50, 50, 50), (1, 1, 148, 48))

    else:
        pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
        pygame.draw.rect(button_surface, (100, 100, 100), (1, 1, 148, 48))

        # Show the button text
    button_surface.blit(text, text_rect)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    # Draw the button on the screen
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    pygame.display.flip()
