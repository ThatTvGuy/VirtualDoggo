# coding: utf-8
from random import randint
#--------------------------------------
# Cria a classe cachorro
#--------------------------------------
class Cachorro:

    def __init__(self, nome, idade, cor, sexo, notif, patas=4):
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
# define algumas funcoes do cachorro
#--------------------------------------

    def __repr__(self):
        return "este eh o " + ". ele tem " + str(self.idade) + " anos, e ele é um(a) " + self.sexo + "."

    def comer(self, valor):
        if self.fome > valor:
            self.fome -= valor
            self.notif.novaMsg(self.nome + ' Amou essa comida')
        else:
            self.notif.novaMsg(self.nome + ' não está com fome')

    def carinho(self):
        chance = randint(0,1)
        if chance == 1:
            self.felicidade += 10
            self.notif.novaMsg(self.nome + ' esta mais feliz')
        else:
            self.felicidade -= 2
            self.notif.novaMsg(self.nome + ' Ta de mal humor')

    def mouseover(self):
        x = width / 2
        y = height * 3 / 4
        d = ((mouseX - x) ** 2 + (mouseY - y) ** 2) ** 0.5
        r = 60
        if d < r:
            return True
        else:
            return False

    def update(self):
        global height, width
        x = width / 2
        y = height * 3 / 4
        w = 10 * self.idade
        h = w
        stroke
        fill(self.cor)
        ellipse(x, y + 33, w, h)


#--------------------------------------
# Barrinha da fome e felicidade
#--------------------------------------

        self.felicidade -= 0.01
        self.felicidade = constrain(self.felicidade, 0, 100)

        self.fome += 0.02
        self.fome = constrain(self.fome, 0, 100)