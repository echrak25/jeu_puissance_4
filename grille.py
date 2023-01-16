import numpy as np

class Grille:
    def __init__(self,nbligne,nbcolonne):
        self.nbligne=nbligne
        self.nbcolonne=nbcolonne
        self.matrice=np.zeros((nbligne,nbcolonne))
    def position_v(self,column):
        return self.matrice[self.nbligne-1,column]==0
    def position_val_suiv(self,column):
        for row in range(self.nbligne):
            if self.matrice[row,column]==0:
                return row
    def mettre_p(self,row,column,tour):
        self.matrice[row,column]=tour
    def ganant(self,tour):
        for i in range(self.nbligne):
            for j in range(self.nbcolonne-3):
                if self.matrice[i,j]==tour and self.matrice[i,j+1]==tour and self.matrice[i,j+2]==tour and self.matrice[i,j+3]==tour:
                    return True
        for i in range(self.nbligne-3):
            for j in range(self.nbcolonne ):
                if self.matrice[i, j] == tour and self.matrice[i+1, j ] == tour and self.matrice[i+2, j ] == tour and self.matrice[i+3, j ] == tour:
                    return True
        for i in range(self.nbligne):
            for j in range(self.nbcolonne - 3):
                if self.matrice[i, j] == tour and self.matrice[i-1, j + 1] == tour and self.matrice[i-2, j + 2] == tour and self.matrice[i-3, j + 3] == tour:
                    return True
        for i in range(self.nbligne -3 ):
            for j in range(self.nbcolonne - 3):
                if self.matrice[i, j] == tour and self.matrice[i+1, j + 1] == tour and self.matrice[i+2, j + 2] == tour and self.matrice[i+3, j + 3] == tour:
                    return True

    def pleine(self):
        return self.matrice.all() #cette fonction va verifier si la matrice est pleine
    def repeter(self):
        self.matrice=np.zeros((self.nbligne,self.nbcolonne))
    def affichage_matrice(self):
        print(np.flip(self.matrice,0))





