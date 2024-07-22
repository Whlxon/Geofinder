import pygame as pg
from tkinter import *
import tkinter as tk 
from import_script import *


def america_n_D ():
    pg.init()
    
    ef = pg.display.set_mode((713, 810))
    
    Clock = pg.time.Clock()
    
    bad = 0
    
    running = True
    
    follow_mouse = False
    
    while running:
        click = False
        s_p_rect.x, s_p_rect.y = pg.mouse.get_pos()
        ef.fill((255, 255, 255))
        ef.blit(amerique_n, (0, 0))
        #on fait le tour de tout les évement dan pygame
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        #on affiche tout nos drapeaux et si l'emplacement est bon on affiche un v
        for i in range(len(amerique)):
            if amerique_l[i] == True:
                ef.blit(validation, (amerique_rect[i].x, amerique_rect[i].y))
            else:
                ef.blit(amerique[i], (amerique_rect[i].x, amerique_rect[i].y))
        
        #on verifie si la souris est en collision avec un drapeau si c'est le cas on verifie si on click dessus si c'est le cas on mets sur True le suivis de la souris
        for i in range(len(amerique)):
            if s_p_rect.colliderect(amerique_rect[i]):
                if click:
                    if follow_mouse:
                        follow_mouse = False
                        bad += 1
                        
                        #on récupère les coordoné du bon emplacement du pays et on verifie si il y est, si il y est on mets sur true la variable de verfication
                        for i in range(len(amerique_d_x)):
                            x, x2 = amerique_d_x[i]
                            y, y2 = amerique_d_y[i]
                            
                            if amerique_l[i] == False:
                                if amerique_rect[i].x > x and amerique_rect[i].x < x2:
                                    if amerique_rect[i].y > y and amerique_rect[i].y < y2:
                                        if follow_mouse == False:
                                            amerique_l[i] = True
                                            bad -= 1
                        
                    elif follow_mouse == False and amerique_l[i] == False:
                        follow_mouse = True
                    n = i
        
        #on compte le nombre de pays qui sont bien placé
        count = 0
        for i in amerique_l:
            if i == True:
                count += 1
            else:
                pass
        
        #si tout les pays sont bien placé on arrête le jeux
        if count == 16:
            pg.QUIT()
        
        if follow_mouse:
            amerique_rect[n].x, amerique_rect[n].y = pg.mouse.get_pos()
        
        ef.blit(s_point, (s_p_rect.x, s_p_rect.y))
        
        police = pg.font.SysFont("monospace" ,25)
        image_texte = police.render ( f"{count}/16", 1 , (0, 0, 0) )
        ef.blit(image_texte, (0, 0))
        
        image_texte = police.render ( f"You miss: {bad} times", 1 , (0, 0, 0) )
        ef.blit(image_texte, (0, 20))
        
        Clock.tick(120)
        pg.display.flip()