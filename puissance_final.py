import sys
import tkinter as tk
import tkinter.messagebox
import pygame
import grille

grille_g=grille.Grille(6,7)
               #### la palette des couleurs utilisés####
arriereplan=(230,230,250)
couleurgrille="#ce4848"
joueur_1="#313347"
joueur_2="#b50427"
white="white"

                           #### Classe GAME ####
class Fenetre:

    def __init__(self,taille):
        self.taille=taille
        self.radius=taille//2-6
        self.width=7*taille
        self.height = 7 * taille
        self.offset=taille
        self.cercle_off=taille//2
        self.display = pygame.display.set_mode((self.width, self.height+100))
    def arr_plan(self):
        for i in range (grille_g.nbligne):
            for j in range(grille_g.nbcolonne):
                left=j*self.taille
                top=i*self.taille+self.offset
                pygame.draw.rect(self.display,couleurgrille,(left,top,self.taille,self.taille))
                pygame.draw.circle(self.display, arriereplan, (left+self.cercle_off, top+ self.cercle_off), self.radius)

        pygame.display.update()
    def coloring_pos(self):
        for i in range (grille_g.nbligne):
            for j in range(grille_g.nbcolonne):
                if grille_g.matrice[i,j]==1:
                    couleur_j_c=joueur_1
                elif grille_g.matrice[i,j]==2:
                    couleur_j_c = joueur_2
                else:
                    couleur_j_c = arriereplan
                x=j*self.taille+self.cercle_off
                y=self.height-(i*self.taille+self.cercle_off)
                pygame.draw.circle(self.display, couleur_j_c, (x,y), self.radius)
        pygame.display.update()
    def mouse(self,x,couleur_j_c):
        pygame.draw.rect(self.display, arriereplan, (0,0, self.width, self.taille))
        pygame.draw.rect(self.display, arriereplan, (0, 630, self.width, self.taille+20))
        pygame.draw.circle(self.display, joueur_1, (52, 700),20)
        pygame.draw.circle(self.display, joueur_2, (52, 655), 20)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Joueur 2', white, joueur_2)
        text2 = font.render('Joueur 1', white, joueur_1)
        textRect2 = text2.get_rect()
        textRect1 = text.get_rect()
        textRect1.center = (250//2, 655)
        textRect2.center = (250 // 2, 701)
        self.display.blit(text, textRect1)

        self.display.blit(text2, textRect2)
        pygame.draw.circle(self.display, couleur_j_c, (x , self.cercle_off), self.radius)
        pygame.display.update()
    def mettre_piece(self,x,tour):
        column=x//self.taille
        if grille_g.position_v(column):
            row=grille_g.position_val_suiv(column)
            grille_g.mettre_p(row,column,tour)
            return True
        return False
    def repeter(self):
        self.display = pygame.display.set_mode((self.width, self.heigh))
        grille_g.repeter()
        self.arr_plan()
        self.coloring_pos()
def results(gagnant=0):
    title='GAME OVER'
    if gagnant!=1 or gagnant!=2:
        message=f'le joueur {gagnant} a gagné ! souhaitez-vous recommencer ?'
    else:
        message = 'le match était null ! souhaitez-vous recommencer ?'
    return tkinter.messagebox.askyesno(title=title,message=message)
def main():
    pygame.init()
    pygame.display.set_caption('Puissance 4 BY ECHRAK CHALGHAMI')
    fenetre=Fenetre(90)
    fenetre.arr_plan()
    continuer=True
    tour=1
    tkinter.messagebox.showinfo(title="Information", message="le joueur 1 va commencer le jeu ")
    couleur_j_c=joueur_1
    while continuer:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.MOUSEMOTION:
                fenetre.mouse(event.pos[0],couleur_j_c)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if fenetre.mettre_piece(event.pos[0],tour):
                    fenetre.coloring_pos()
                    if grille_g.ganant(tour):
                        continuer=results(tour)
                        grille_g.repeter()
                    elif grille_g.pleine():
                        continuer = results()
                        grille_g.repeter()
                    else:
                        if tour==1:
                            tour=2
                        else:
                            tour==2
                            tour=1
                        if tour==1:
                            couleur_j_c=joueur_1
                        else:
                            couleur_j_c=joueur_2

                        fenetre.mouse(event.pos[0],couleur_j_c)

if __name__=="__main__":
    main()
