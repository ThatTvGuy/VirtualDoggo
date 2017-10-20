#coding: utf-8

#--------------------------------------
#Cria a classe cachorro
#--------------------------------------
class Cachorro:
    def __init__(self, nome, idade, cor, sexo, notif, patas = 4):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.sexo = sexo
        self.patas = patas
        self.fome = 0
        self.felicidade = 100
        self.sono = 0
        self.notif = notif
#--------------------------------------
#define algumas funcoes do cachorro
#--------------------------------------
    def __repr__(self):
        return "este eh o " + ". ele tem " + str(self.idade) + " anos, e ele é um(a) " + self.sexo + "."
    
    
    def comer(self):
        if self.fome > 10:
            self.fome -=20
            self.notif.novaMsg (self.nome + ' esta mais feliz')
        else:
            self.notif.novaMsg (self.nome + ' não está com fome')
    
    def update(self):
        global height, width
        x = width/2
        y = height * 3/4
        w = 10 * self.idade
        h = w * 2/3
        stroke
        fill (self.cor)
        ellipse(x,y + 33,w,h)
        rectMode(CENTER)
        
#--------------------------------------
#Barrinha da fome e felicidade
#--------------------------------------
        
        self.felicidade -= 0.01        
        self.felicidade = constrain(self.felicidade, 0, 100)
        rect (x, y-h-100,self.felicidade,8)
        
        
        
        self.fome += 0.02
        self.fome = constrain(self.fome,0,100)
        rect (x,y-h-15,self.fome,15)