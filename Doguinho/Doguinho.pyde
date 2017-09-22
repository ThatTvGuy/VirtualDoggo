#--------------------------------------
#Cria a classe cachorro
#--------------------------------------
class Cachorro:
    def __init__(self, nome, idade, cor, secsu, patas = 4):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.secsu = secsu
        self.patas = patas
        self.fome = 0
        self.sono = 0
        self.felicidade = 100
        self.saude = 100
#--------------------------------------
#define algumas funcoes do cachorro
#--------------------------------------
    def comer(self):
        if self.fome > 10:
            self.fome -=20
            self.fome = constrain(self.fome, 0, 100) 
            print (self.nome + ' esta mais feliz')
        else:
            print (self.nome + ' não está com fome')
    
    def uptade(self):
        global height, width
        x = width/2
        y = height/2
        w = 10 * self.idade
        h = w
        fill (self.cor)
        ellipse(x,y,w,h)
        
#--------------------------------------
#Barrinha da fome e felicidade
#--------------------------------------
        rectMode(CENTER)
        
        self.felicidade -= 0.01        
        rect (x, y-h-20,self.felicidade,15)
        
        self.fome += 0.02
        rect (x,y-h,self.fome,15)    
#--------------------------------------
#Define as variaçoes de cada cachorro
#--------------------------------------
preto = color(0)
dog = Cachorro('Toninho', 6, preto, 'Macho')

def setup():
    background (136,227,232)
    size (500,500)
def draw():
    background (136,227,232)
    dog.uptade()

def keyPressed():
    if key == ' ':
        dog.comer()
    if key == 'b':
        dog.brincar