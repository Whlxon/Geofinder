import pygame as pg 
from import_script import *        

def europe_d():
    
    pg.init()
    
    ef = pg.display.set_mode((1082, 1000))
    
    Clock = pg.time.Clock()

    running = True
    
    bad = 0
    
    follow_mouse = False
    
    while running:
        click = False
        s_p_rect.x, s_p_rect.y = pg.mouse.get_pos()
        ef.fill((255, 255, 255))
        
        ef.blit(europe, (0, 0))
        
        #on passe en revue tout les evenements de pygame et si on click sur la croix on ferme la fenêtre
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        #on fait une boucle for pour affiché les différente images dans la variable pays
        for i in range(len(pays)):
            if pays_l[i] == True:
                ef.blit(validation, (pays_rect[i].x, pays_rect[i].y))
            else:
                ef.blit(pays[i], (pays_rect[i].x, pays_rect[i].y))
        
        for i in range(len(pays)):
            if s_p_rect.colliderect(pays_rect[i]):
                if click:
                    if follow_mouse:
                        follow_mouse = False
                        bad += 1
                        for i in range(len(pays_d_x)):
                            x, x2 = pays_d_x[i]
                            y, y2 = pays_d_y[i]
                            if pays_l[i] == False:
                                if pays_rect[i].x > x and pays_rect[i].x < x2:
                                    if pays_rect[i].y > y and pays_rect[i].y < y2:
                                        if follow_mouse == False:
                                            bad -= 1
                                            pays_l[i] = True
                            
                    elif follow_mouse == False and pays_l[i] == False:
                        follow_mouse = True
                    n = i
        
        #on compte le nombre de pays qui sont bien placé
        count = 0
        for i in pays_l:
            if i == True:
                count += 1
            else:
                pass
        
        #si tout les pays sont bien placé on arrête le jeux
        if count == 43:
            pg.QUIT()
        
        #si le drapeau est en suivis de la souris alors on donne les coordonné de la souris au drapeau
        if follow_mouse:
            pays_rect[n].x, pays_rect[n].y = pg.mouse.get_pos()
                
        
        ef.blit(s_point, (s_p_rect.x, s_p_rect.y))
        
        police = pg.font.SysFont("monospace" ,25)
        image_texte = police.render ( f"{count}/43", 1 , (0, 0, 0) )
        ef.blit(image_texte, (0, 0))
        
        image_texte = police.render ( f"You miss: {bad} times", 1 , (0, 0, 0) )
        ef.blit(image_texte, (0, 20))
        
        Clock.tick(120)
        pg.display.flip()
