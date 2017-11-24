from cachorro import Cachorro
from mensagem import Mensageiro
from UI import UI
#--------------------------------------------------------------
#Define as variaçoes de cada cachorro, cenarios e outras coisas
#--------------------------------------------------------------
preto = color(0)

notif = Mensageiro(0,0)
dog = Cachorro('Toninho', 6, preto, 'Macho', notif)
interface = UI(dog)


def setup():
    global img
    background (136,227,232)
    size (500,500)
    img = loadImage('CenarioMelhor.png')
    
    

def draw():
    #background (136,227,234)
    image(img,0, 0, width, height)
    dog.update()
    notif.update()
    interface.update()


def keyPressed():
    if key == ' ':
      dog.comer( )
      
def mouseClicked():
    if dog.mouseover():
        dog.carinho()