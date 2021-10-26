import pgzero
import pgzrun
import pygame
import tkinter as tk
import maze
import random
import tkinter
import tkinter.font as font
from tkinter import *
from tkinter import Tk, Canvas, Button
from time import sleep
from time import time
from random import randint
from tkinter import messagebox
#from win32api import GetSystemMetrics


#bildschirmbreite = GetSystemMetrics(0)
#bildschirmhoehe = GetSystemMetrics(1)
#breitenPositionierung = bildschirmbreite // 2 - 400
#hoehenPositionierung = bildschirmhoehe // 2 - 400
breitenPositionierung = 600
hoehenPositionierung = 200
pygame.display.set_mode((100, 300))
master = tkinter.Tk()

pygame.init()
einfach = True


def startButtonClick():
    master.destroy()
    sounds.gameclicksound.play()
    #print("Spiel startet!")


def optionsButtonClick():
    sounds.gameclicksound.play()
    #print("Optionen")


def easyButtonClick():
    global einfach
    sounds.gameclicksound.play()
    einfach = True
    #print("Easy Mode")


def hardButtonClick():
    global einfach
    sounds.gameclicksound.play()
    einfach = False
    #print("Hard Mode")


def quitButtonClick():
    #print("Spiel wurde beendet!")
    quit()


def playAgainButtonClick():
    #print("Spiel wird neu gestartet!")
    # root.destroy()
    # startButtonClick()
    # mainMenu()
    erstelleLabyrinth()
    root.destroy()
    master.destroy
    master.mainloop()
    draw()


def quit_after_winClick():
    #print("Spiel wurde beendet!")
    quit()


def onLeaveStart(event):
    startButton.config(bg="#1874CD")


def onEnterStart(event):
    startButton.config(bg="#1E90FF")


def onLeaveOptions(event):
    optionsButton.config(bg="#1874CD")


def onEnterOptions(event):
    optionsButton.config(bg="#1E90FF")


def onLeaveQuit(event):
    quitButton.config(bg="#1874CD")


def onEnterQuit(event):
    quitButton.config(bg="#1E90FF")


def onLeaveQuitEasy(event):
    easyButton.config(bg="#1874CD")


def onEnterQuitEasy(event):
    easyButton.config(bg="#1E90FF")


def onLeaveQuitHard(event):
    hardButton.config(bg="#1874CD")


def onEnterQuitHard(event):
    hardButton.config(bg="#1E90FF")


playAgainButton = tkinter.Button
playAgainButton = tkinter.Button
quit_after_winButton = tkinter.Button


def erstelleMain_Menu():
    global playAgainButton
    global optionsButton
    global quit_after_winButton
    global MainMenuText
    global createdBy

    global root
    root = tkinter.Tk()
    root.title("Labyrinth Finish")
    root.geometry("800x800")

    root.geometry("+%d+%d" % (breitenPositionierung, hoehenPositionierung))
    buttonFont = font.Font(family="Impact", size=30)
    MainMenuTextFont = font.Font(family="Arial", size=60)

    MainMenuText = Label(root, text="F I N I S H", font=MainMenuTextFont)
    MainMenuText.pack(pady=50)

    createdBy = Label(
        root, text="Created By: Emilio, Monty & Rico", font=MainMenuTextFont
    )
    createdBy.pack(pady=500)

    playAgainButton = tkinter.Button(
        root,
        text="P L A Y   A G A I N",
        width=400,
        height=100,
        command=playAgainButtonClick,
        bg="#1874CD",
        fg="white",
        activebackground="#1E90FF",
        activeforeground="white",
        bd=15,
        font=buttonFont,
    )

    optionsButton = tkinter.Button(
        root,
        text="O P T I O N S",
        width=400,
        height=100,
        command=optionsButtonClick,
        bg="#1874CD",
        fg="white",
        activebackground="#1E90FF",
        activeforeground="white",
        bd=15,
        font=buttonFont,
    )

    quit_after_winButton = tkinter.Button(
        root,
        text="Q U I T   G A M E",
        width=400,
        height=100,
        command=quit_after_winClick,
        bg="#1874CD",
        fg="white",
        activebackground="#1E90FF",
        activeforeground="white",
        bd=15,
        font=buttonFont,
    )

    playAgainButton.pack()
    # playAgainButton.bind('<Leave>', onLeaveStart)
    # playAgainButton.bind('<Enter>', onEnterStart)
    playAgainButton.place(x=200, y=200, width=400, height=100)

    optionsButton.pack()
    # optionsButton.bind('<Leave>', onLeaveOptions)
    # optionsButton.bind('<Enter>', onEnterOptions)
    optionsButton.place(x=200, y=400, width=400, height=100)

    quit_after_winButton.pack()
    # quit_after_winButton.bind('<Leave>', onLeaveQuit)
    # quit_after_winButton.bind('<Enter>', onEnterQuit)
    quit_after_winButton.place(x=200, y=600, width=400, height=100)

    root.mainloop()

startButton = tkinter.Button()
optionsButton = tkinter.Button()
quitButton = tkinter.Button()
easeyButton = tkinter.Button()
hardButton = tkinter.Button()

def mainMenu():

    master.title("Labyrinth Main_Menu")
    master.geometry("800x800")

    master.geometry("+%d+%d" % (breitenPositionierung, hoehenPositionierung))
    buttonFont = font.Font(family="Impact", size=30)
    MainMenuTextFont = font.Font(family="Arial", size=60)
    createdByFont = font.Font(family="Arial", size=20)

    MainMenuText = Label(master, text="L A B Y R I N T H", font=MainMenuTextFont)
    MainMenuText.pack(pady=50)

    createdBy = Label(
        master, text="Created By: Emilio, Monty & Rico", font=createdByFont
    )
    createdBy.place(y=600, x=193)

    global startButton
    startButton = tkinter.Button(
        master,
        text="S T A R T   G A M E",
        width=400,
        height=100,
        command=startButtonClick,
        bg="#1874CD",
        fg="white",
        activebackground="#1E90FF",
        activeforeground="white",
        bd=15,
        font=buttonFont,
    )

    global easyButton
    easyButton = tkinter.Button(
        master,
        text="E A S Y",
        width=180,
        height=80,
        command=easyButtonClick,
        bg="#1874CD",
        fg="white",
        activebackground="#1E90FF",
        activeforeground="white",
        bd=15,
        font=buttonFont,
    )
    global hardButton
    hardButton = tkinter.Button(
        master,
        text="H A R D",
        width=180,
        height=80,
        command=hardButtonClick,
        bg="#1874CD",
        fg="white",
        activebackground="#1E90FF",
        activeforeground="white",
        bd=15,
        font=buttonFont,
    )
    global quitButton
    quitButton = tkinter.Button(
        master,
        text="Q U I T   G A M E",
        width=400,
        height=100,
        command=quitButtonClick,
        bg="#1874CD",
        fg="white",
        activebackground="#1E90FF",
        activeforeground="white",
        bd=15,
        font=buttonFont,
    )

    startButton.pack()
    startButton.bind("<Leave>", onLeaveStart)
    startButton.bind("<Enter>", onEnterStart)
    startButton.place(x=200, y=200, width=400, height=100)

    quitButton.pack()
    quitButton.bind("<Leave>", onLeaveQuit)
    quitButton.bind("<Enter>", onEnterQuit)
    quitButton.place(x=200, y=480, width=400, height=100)

    easyButton.pack()
    easyButton.bind("<Leave>", onLeaveQuitEasy)
    easyButton.bind("<Enter>", onEnterQuitEasy)
    easyButton.place(x=200, y=350, width=180, height=80)

    hardButton.pack()
    hardButton.bind("<Leave>", onLeaveQuitHard)
    hardButton.bind("<Enter>", onEnterQuitHard)
    hardButton.place(x=420, y=350, width=180, height=80)

    master.mainloop()

mainMenu()

WIDTH = 800
HEIGHT = 800
STEP = 40  # Schrittweite
schluessel = False
geschafft = False
grounded = True
laufen = True

TITLE = "Labyrinth"
CENTER = (WIDTH / 2, HEIGHT / 2)

bunny = Actor("bunny")
background = Actor("backgroundgross", (400, 400))
vignette = Actor("vignette")
aufgabe = "Aufgabe: Schluessel finden"
ball = Actor("schluesselklein")
ausgang = Actor("ball")

walls = []
labyrinth = maze.Maze(width=12, height=12)
labyrinth.randomize()
playerx = random.randrange(0, labyrinth.width)
playery = random.randrange(0, labyrinth.height)
ausgabe_array = labyrinth._to_str_matrix()

def erstelleLabyrinth():

    global ausgabe_array
    global ball
    global ausgang
    for i in range(len(ausgabe_array)):
        for j in range(len(ausgabe_array[i])):
            if ausgabe_array[i][j] == "O":
                walls.append(Actor("wand01", (i * STEP - 80, j * STEP - 80)))

    targetx = random.randrange(0, labyrinth.width)
    targety = random.randrange(0, labyrinth.height)

    exitx = random.randrange(0, labyrinth.width)
    exity = random.randrange(0, labyrinth.height)

    ausgabe_array = labyrinth._to_str_matrix()
    ausgabe_array[2 * playerx + 1][2 * playery + 1] = "@"

    bunny.x = WIDTH // 2 + STEP
    bunny.y = HEIGHT // 2 + STEP
    ausgabe_array[2 * targetx + 1][2 * targety + 1] = "$"
    ausgabe_array[2 * exitx + 1][2 * exity + 1] = "e"
    ball = Actor(
        "schluesselklein", (STEP * (2 * targetx - 1), STEP * (2 * targety - 1))
    )
    ausgang = Actor("ball", (STEP * (2 * exitx - 1), STEP * (2 * exity - 1)))

erstelleLabyrinth()

def walls_move(dx, dy):
    for w in walls:
        animate(w, pos=(w.x + dx, w.y + dy), duration=0.25)

def walls_collide(dx, dy):
    collision = False
    for w in walls:
        if (
            abs(w.x + dx - (WIDTH // 2 + STEP)) < 20
            and abs(w.y + dy - (HEIGHT // 2 + STEP)) < 20
        ):
            collision = True
    return collision

def on_key_down(key):
    if grounded:
        if keyboard.left and background.left < WIDTH / 2:
            if not walls_collide(40, 0):
                animate(
                    background,
                    pos=(background.x + 40, background.y),
                    on_finished=bunnyLeftPic,
                    duration=0.25,
                )
                animate(ball, pos=(ball.x + 40, ball.y), duration=0.25)
                animate(ausgang, pos=(ausgang.x + 40, ausgang.y), duration=0.25)
                walls_move(40, 0)
                bunny.image = "jleft"
                sounds.walk2.play()

        elif keyboard.right and background.right > WIDTH / 2:
            if not walls_collide(-40, 0):
                animate(
                    background,
                    pos=(background.x - 40, background.y),
                    on_finished=bunnyRightPic,
                    duration=0.25,
                )
                animate(ball, pos=(ball.x - 40, ball.y), duration=0.25)
                animate(ausgang, pos=(ausgang.x - 40, ausgang.y), duration=0.25)
                walls_move(-40, 0)
                bunny.image = "jright"
                sounds.walk2.play()
        elif keyboard.up and background.top < HEIGHT / 2:
            if not walls_collide(0, 40):
                animate(
                    background,
                    pos=(background.x, background.y + 40),
                    on_finished=bunnyUpPic,
                    duration=0.25,
                )
                animate(ball, pos=(ball.x, ball.y + 40), duration=0.25)
                animate(ausgang, pos=(ausgang.x, ausgang.y + 40), duration=0.25)
                walls_move(0, 40)
                bunny.image = "jbunny"
                sounds.walk2.play()
        elif keyboard.down and background.bottom > HEIGHT / 2:
            if not walls_collide(0, -40):
                animate(
                    background,
                    pos=(background.x, background.y - 40),
                    on_finished=bunnyDownPic,
                    duration=0.25,
                )
                animate(ball, pos=(ball.x, ball.y - 40), duration=0.25)
                animate(ausgang, pos=(ausgang.x, ausgang.y - 40), duration=0.25)
                walls_move(0, -40)
                bunny.image = "jdown"
                sounds.walk2.play()


def bunnyLeftPic():
    bunny.image = "left"


def bunnyRightPic():
    bunny.image = "right"


def bunnyDownPic():
    bunny.image = "down"


def bunnyUpPic():
    bunny.image = "bunny"


def schluesselEinsammeln():
    global schluessel, aufgabe
    if bunny.colliderect(ball):
        schluessel = True
        ball.x = 2000
        sounds.key.play()

    if schluessel == True:
        ball.image = "empty"
        aufgabe = "Aufgabe: Tuer suchen"



def ausgangGefunden():
    global aufgabe
    global geschafft
    global schluessel
    if bunny.colliderect(ausgang) and schluessel == True:
        sounds.gameover.play()
        geschafft = True
        ausgang.x = 2040
        erstelleMain_Menu()
        pygame.display.set_mode((800, 800))



def update():
    global grounded
    global schluessel
    global geschafft
    global aufgabe
    grounded = False
    if (
        bunny.image == "left"
        or bunny.image == "right"
        or bunny.image == "down"
        or bunny.image == "bunny"
    ):
        grounded = True
    schluesselEinsammeln()
    ausgangGefunden()
    # leben()
    if geschafft == True and schluessel == True:
        aufgabe = "Sie haben das Ziel erreicht"


def draw():
    screen.clear()
    background.draw()
    bunny.draw()
    ball.draw()
    ausgang.draw()

    for w in walls:
        w.draw()
    if einfach == False:
        vignette.draw()
    screen.draw.text(
        str(aufgabe),
        color="white",
        midtop=(400, 10),
        fontsize=50,
        shadow=(1, 1),
        scolor="#808080",
    )

pgzrun.go()