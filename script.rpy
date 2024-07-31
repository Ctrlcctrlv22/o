define a = Character('ktoto', color="#ff0000", image = 'ktoto')

define b = Character('bunny', color="#ffa200ad", image = 'bunny')

init:
    $ left2 = Position(xlign = 90, yalign = 1.0)

define gui.text_color = "#000000"

#define gui.text_font = "minecraft.ttf"

label start:
    scene bg bigcity

    show ktoto smile at left
    
    show bunni main at right

    a"..........."

    b"net"

    a angry "grrrrrrrrrrrrrrrrrrrrrrr"
    
    b black "ne bey"

    a villiansmile "hihiha"

    return

