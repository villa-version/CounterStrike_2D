from main import Main

main = None

def setup():
    size(1280, 720)
    rectMode(CENTER)
    ellipseMode(CENTER)
    imageMode(CENTER)
    textSize(24)

    global main
    main = Main()

def draw():
    background(126,224,232)
    global main
    main.run()

    # move player
    if keyPressed:
        if key == 'a':
            main.dir_player('LEFT')
        elif key == 'd':
            main.dir_player('RIGHT')
        elif key == ' ':
            main.dir_player('UP')
    # move player


#def keyPressed():
#    global main
#    if key == 'r':
#        main.reload()


def mousePressed():
    main.build_box()
    #main.shoot()

    if mouseButton == RIGHT:
        main.delete_box()
