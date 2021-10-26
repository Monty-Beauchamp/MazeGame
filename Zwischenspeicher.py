


"""
def on_key_down():
    if grounded:
        if buttonLinks.is_pressed and background.left < WIDTH/2:
            if not walls_collide(40,0):
                animate(background, pos = (background.x+40, background.y), on_finished=bunnyLeftPic, duration = 0.25)
                animate(ball, pos = (ball.x+40, ball.y), duration = 0.25)
                walls_move(40, 0)
                bunny.image = "jleft"
                sounds.walk2.play()
        elif buttonRechts.is_pressed and background.right > WIDTH/2:
            if not walls_collide(-40,0):
                animate(background, pos = (background.x-40, background.y), on_finished=bunnyRightPic, duration = 0.25)
                animate(ball, pos = (ball.x-40, ball.y), duration = 0.25)
                walls_move(-40, 0)
                bunny.image = "jright"
                sounds.walk2.play()
        elif buttonVorne.is_pressed and background.top < HEIGHT/2:
            if not walls_collide(0, 40):
                animate(background, pos = (background.x, background.y+40), on_finished=bunnyUpPic, duration = 0.25)
                animate(ball, pos = (ball.x, ball.y+40), duration = 0.25)
                walls_move(0, 40)
                bunny.image = "jbunny"
                sounds.walk2.play()
        elif buttonHinten.is_pressed and background.bottom > HEIGHT/2:
            if not walls_collide(0, -40):
                animate(background, pos = (background.x, background.y-40), on_finished=bunnyDownPic, duration = 0.25)
                animate(ball, pos = (ball.x, ball.y-40), duration = 0.25)
                walls_move(0, -40)
                bunny.image = "jdown"
                sounds.walk2.play()
"""


"""
buttonVorne = Button(12)
buttonRechts = Button(18)
buttonLinks = Button(21)
buttonHinten = Button(20)
buttonKarteRechts = Button(4)
buttonKarteLinks = Button(22)
dreiLeben = PWMLED(6)
zweiLeben = PWMLED(19)
einLeben = PWMLED(26)
"""


"""
def leben():
    dreiLeben.off()
    zweiLeben.on()
    einLeben.on()
    sleep(2)
    dreiLeben.on()
    zweiLeben.off()
    sleep(2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.off()
    sleep(2)
    print("tot")
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(0.2)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(0.2)
    zweiLeben.on()
    dreiLeben.on()
    einLeben.off()
    sleep(2.5)
    dreiLeben.on()
    zweiLeben.on()
    einLeben.on()
    sleep(10)
"""

"""
.json Datei
{
    "DEBUG": false,
    "jump_sound": true,
    "background_music": true,
    "show_fps": false,
    "show_score": true,
    "high_scores": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
    ]
}
"""

