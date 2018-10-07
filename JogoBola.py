from tkinter import *
from time import sleep
from random import randint

XB = 350
YB = 225
bolaYcontrole = 3
bolaXcontrole = 3

ptsI = 0
ptsE = 0

up = True
direita = False
vez_inimiga = False

YI = 225
YE = 225

def pontos():
    global XB
    global YB
    global YI
    global YE
    global ptsI
    global ptsE
    global pers
    global bola
    global inimigo
    global bolaXcontrole
    global bolaYcontrole
    global ponto

    if XB < 0:
        ptsE += 1
        YI = 225
        YE = 225
        XB = 350
        YB = 225
        ponto.destroy()
        bola.destroy()
        ponto = Label(tela, font='Times 150 bold', text='{}      {}'.format(ptsI, ptsE))
        ponto['bg'] = 'black'
        ponto['fg'] = 'white'
        ponto.place(x=90, y=95)
        pers.place(x=2, y=YI)
        bola = Label(tela, text=[[]])
        bola['bg'] = 'red'
        bola['fg'] = 'red'
        bola.place(x=XB, y=YB)
        inimigo.place(x=687, y=YE)
        bolaYcontrole = 2
        bolaXcontrole = 2
        tela.update()
        sleep(2)
    if XB > 685:
        ptsI += 1
        YI = 225
        YE = 225
        XB = 350
        YB = 225
        ponto.destroy()
        bola.destroy()
        ponto = Label(tela, font='Times 150 bold', text='{}      {}'.format(ptsI, ptsE))
        ponto['bg'] = 'black'
        ponto['fg'] = 'white'
        ponto.place(x=90, y=95)
        pers.place(x=2, y=YI)
        bola = Label(tela, text=[[]])
        bola['bg'] = 'red'
        bola['fg'] = 'red'
        bola.place(x=XB, y=YB)
        inimigo.place(x=687, y=YE)
        bolaYcontrole = 2
        bolaXcontrole = 2
        tela.update()
        sleep(2)
        
def ir_up(Key):
    global YI
    global pers
    YI -= 4
    if YI < 0:
        YI = 0
    pers.place(x=2, y=YI)
    tela.update()


def ir_down(Key):
    global YI
    global pers
    YI += 4
    if YI > 391:
        YI = 391
    pers.place(x=2, y=YI)
    tela.update()

def inimigo_mover():
    global YB
    global YE
    global inimigo
    global vez_inimiga

    if vez_inimiga == True:
        if YB > YE + 30:
            YE += randint(1, 3)
        if YB < YE + 30:
            YE -= randint(1, 3)
        if YE < 0:
            YE = 0
        if YE > 391:
            YE = 391
        inimigo.place(x=687, y=YE)
        
    tela.update()
        
def bola_mover():
    global XB
    global YB
    global YI
    global YE
    global bolaXcontrole
    global bolaYcontrole
    global bola
    global up
    global direita
    global vez_inimiga

    bola.place(x=XB, y=YB)

    if up == True:
        YB -= bolaYcontrole
    if up == False:
        YB += bolaYcontrole

    if direita == True:
        XB += bolaXcontrole
    if direita == False:
        XB -= bolaXcontrole
        
    if YB <= 0:
        up = False
    if YB >= 431:
       up = True

    if 12 > XB > 0  and (YI + 65) > YB > (YI - 20):
        direita = True
        vez_inimiga = True
        bolaYcontrole = randint(2, 7)
        bolaXcontrole = randint(3, 5)
    if 700 > XB > 671 and (YE + 65) > YB > (YE - 20):
        direita = False
        vez_inimiga = False
        bolaYcontrole = randint(2, 7)
        bolaXcontrole = randint(3, 5)
    tela.update()

def main():
    global XB
    global YB
    global YI
    global YE
    global pers
    global bola
    global inimigo
    global ptsI
    global ptsE
    global ponto

    ponto = Label(tela, font='Times 150 bold', text='{}      {}'.format(ptsI, ptsE))
    ponto['bg'] = 'black'
    ponto['fg'] = 'white'
    ponto.place(x=90, y=95)

    pers = Label(tela, text=['\n\n\n'])
    pers['bg'] = 'blue'
    pers['fg'] = 'blue'
    pers.place(x=2, y=YI)

    inimigo = Label(tela, text=['\n\n\n'])
    inimigo['bg'] = 'cyan'
    inimigo['fg'] = 'cyan'
    inimigo.place(x=687, y=YE)

    bola = Label(tela, text=[[]])
    bola['bg'] = 'red'
    bola['fg'] = 'red'
    bola.place(x=XB, y=YB)

    frame = Frame(tela)
    frame.bind('<w>', ir_up)
    frame.bind('<s>', ir_down)
    frame.focus_set()
    frame.place(x=-30, y=-30)
    
    tela.update()

tela = Tk()
tela.title('JogoBolaRebater')
tela.geometry('700x450+200+150')
tela['bg'] = 'Black'

if __name__=="__main__":
    main()
while __name__=="__main__":
    bola_mover()
    inimigo_mover()
    pontos()
    sleep(0.03)
    tela.update()
    


tela.mainloop()
