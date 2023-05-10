#!/usr/bin/env python
# coding: utf-8

# In[4]:


# blibliotecas para fazer funcionar os codigos de automação
import pyautogui as pg
import time as T
pg.PAUSE = 2

# entrar no youtube.

pg.hotkey("ctrl", "t")
T.sleep(10)
pg.write(r"https://www.youtube.com")
Time.sleep(2)
pg.press("enter")

# estas são as variaveis que vai fazer o loop funcionar.
determinante = 209
i = 0


# loop para desinscrever dos canais.
while i <= determinante:
    #entrando no canal
    T.sleep(5)
    pg.click(x=142, y=628) #se caso mudar, adaptar pra sua tela.
    T.sleep(9)
    #aqui vai selecionar o botão de inscrito.
    screenshot = pg.screenshot()
    T.sleep(2)
    img = pg.locateOnScreen("insscritp.png") #adicionar imagem do primeiro botão
    if img is not None:
        x, y = pg.center(img)
        pg.click(x, y)
    else:
        print("não encontrado a img1")
    T.sleep(2)
    
    #aqui vai selecionar o botão de inscrito 2.
    screenshot = pg.screenshot
    img2 = pg.locateOnScreen("inscrito_dif.png") #adicionar imagem do segundo botão
    if img2 is not None:
        x, y =pg.center(img2)
        pg.click(x, y)
    else:
        print("nao encontrado a img2")
    
    T.sleep(2)
    #aqui vai selecionar o botão de inscrito 3.
    screenshot = pg.screenshot
    img3 = pg.locateOnScreen("inscrito_deff.png") #adicionar imagem do terceiro botão
    if img3 is not None:
        x, y =pg.center(img3)
        pg.click(x, y)
    else:
        print("nao encontrado a img3")

    T.sleep(2)
    #aqui vai selecionar o botão de cancelar. 
    screenshot = pg.screenshot
    img4 = pg.locateOnScreen("cancelrp.png") #adicionar imagem de cancelar inscrição
    if img4 is not None:
        x, y =pg.center(img4)
        pg.click(x, y)
    else:
        print("nao encontrado a img4")
    T.sleep(2)
    #aqui vai selecionar o botão de cancelar o ultimo.
    pg.click(x=893, y=518) #se caso mudar, adaptar pra sua tela.


# 

# In[11]:


T.sleep(5)
pg.position()


# In[1]:





# In[ ]:


import pygame as py
from pygame.locals import *
from sys import exit
py.init()
tela = py.display.set_mode((640, 480))
while True:
    for event in py.event.get():
        if event.type == QUIT:
            exit()
    py.display.update()

