from main import Main

main = None

def setup():
    size(800,600)
    rectMode(CENTER)
    ellipseMode(CENTER)
    imageMode(CENTER)

    box_img = loadImage('images/box.jpg')

    global main
    main = Main(box_img)

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
