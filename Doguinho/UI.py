# coding: utf-8
class UI:
    def __init__(self,cachorro):
        self.cachorro = cachorro
        self.comidas = [
                        {"nome": "Biscoito", "valor": 5},
                        {"nome": "Ração", "valor": 10},
                        {"nome": "Bife", "valor": 20},
                        {"nome": "Boi", "valor": 50}
                        ]
        self.elementos = []
        
        
        #botao de comida
        y = 100
        for comida in self.comidas:
            #self.botao(410,y,self.cachorro.comer, arg = comida["valor"])
            b = Botao(400,y)
            b.definirCallback(self.cachorro.comer, comida['valor'])
            if comida['nome'] == 'Biscoito':
                b.definirImagem('Biscoito.png')
            self.elementos.append(b)
            y += 60
            
            
        b = Botao(400, y + 40)
        b.definirCallback(self.cachorro.brincar)
        self.elementos.append(b)
                
    def update(self):
        #barrinha de felicidade
        self.barrinha(10,50,self.cachorro.felicidade)
        
        #barrinha de fome
        self.barrinha(10,70,self.cachorro.fome,color (0,255,0))
        
        for elemento in self.elementos:
            elemento.update()
        
    def mouseClicado(self):
        for elemento in self.elementos:
            dx = mouseX - elemento.x
            dy = mouseY - elemento.y
            if dx >= 0 and dx <= elemento.w:
                if dy >= 0 and dy <= elemento.h:
                    elemento.clicado()
        
    def barrinha(self, x, y, qtd, cor = color (255,0,0)):
        tamanho = 250
        grossura = 8
        pre = map(qtd,0,100,0,250)

        stroke(30)
        strokeWeight(1)
        fill(255)
        rect (x,y,tamanho,grossura)
        
        noStroke()
        fill(cor)
        rect (x,y,pre,grossura)

class Botao:
    w = 70
    h = 50
    cor = color(200,200,200)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def definirCallback(self, func, *args):
        self.callback = func
        self.callback_args = args
        
    def definirImagem(self, url):
        self.img = loadImage(url)
            
    def update(self):
        stroke(30)
        strokeWeight(1)
        fill(self.cor)
        rect(self.x, self.y, self.w, self.h)
        if hasattr (self, 'img'):
            image(self.img, self.x, self.y, self.w, self.h)
        
    def clicado(self):
        if hasattr(self, 'callback'):
            self.callback(*self.callback_args)