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
    
    def update(self):
        #barrinha de felicidade
        self.barrinha(10,50,self.cachorro.felicidade)
        
        #barrinha de fome
        self.barrinha(10,70,self.cachorro.fome,color (0,255,0))
        
        #botao de comida
        y = 100
        for comida in self.comidas:
            self.botao(410,y,self.cachorro.comer, arg = comida.valor)
            y += 60        
        
        
        
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
        
    def botao(self, x, y, callback, arg, cor = color(200,200,255)):
        stroke(30)
        strokeWeight(1)
        fill(cor)
        w = 70
        h = 50
        rect(x, y, w, h)
        dx = mouseX - x
        dy = mouseY - y
        
        if mousePressed:
            if dx >= 0 and dx <= w:
                if dy >= 0 and dy <= h:
                    callback(arg)