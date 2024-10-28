from pile import Pile
from file import File
import matplotlib.pyplot as plt
class Graphe:
    def __init__(self):
        self.dictionnaire = {}

    def ajouterNoeud(self, noeud):
        if noeud not in self.dictionnaire:
            self.dictionnaire[noeud] = {}

    def ajouterArc(self, noeud1, noeud2, porte):
        if noeud1 not in self.dictionnaire:
            self.ajouterNoeud(noeud1)
        if noeud2 not in self.dictionnaire:
            self.ajouterNoeud(noeud2)
        self.dictionnaire[noeud1][noeud2] = porte
        self.dictionnaire[noeud2][noeud1] = porte

    def listerNoeuds(self):
        return list(self.dictionnaire.keys())

    def listerArcs(self):
        arcs = []
        for noeud1, murs in self.dictionnaire.items():
            for noeud2, porte in murs.items():
                arcs.append((noeud1, noeud2, porte))
        return arcs

    def adjacenceNoeud(self, noeud):
        return list(self.dictionnaire[noeud].keys())

    def AfficherGraphe(self):
        for noeud, murs in self.dictionnaire.items():
            print(f"Noeud {noeud}:")
            for noeud2, porte in murs.items():
                print(f"\t- {noeud2} ({'porte' if porte else 'mur'})")
class SearchLabyrinthe:

    def __init__(self, graphe, etat_initial):
        self.graphe = graphe
        self.etat_initial = etat_initial
        self.explores = {}  
        self.accessibles = {}  

    def successeurs(self, etat):
  
        
        voisins = self.graphe.adjacenceNoeud(etat)

        successeurs_valides = []
        for voisin in voisins:
            
            if self.graphe.dictionnaire[etat].get(voisin, False):
                successeurs_valides.append(voisin)

        return successeurs_valides

    def VerifEtat(self, etat, explores, accessibles):
        
        return explores.get(etat, False) or accessibles.get(etat, False)
    def dfs(self,graphe,etat_initiale,etat_final):
        p=Pile()
        etat_explorer=[]
        etat_explorer.append(etat_initiale)
        p.empiler(etat_initiale)
        while not (p.pile_vide()) or etat_courant!=etat_final:
            etat_courant=p.depiler()
            if etat_courant==etat_final:
                return True
            else:
                etats_voisins = self.successeurs(etat_courant)  
                for voisin in etats_voisins:
                    if voisin not in etat_explorer:  
                        etat_explorer.append(voisin)  
                        p.empiler(voisin)  
        return False
    def bfs(self,graphe,etat_initiale,etat_final):
        f=File()
        etat_explorer=[]
        etat_explorer.append(etat_initiale)
        p.emfiler(etat_initiale)
        while not (p.File_vide()) or etat_courant!=etat_final:
            etat_courant=p.defiler()
            if etat_courant==etat_final:
                return True
            else:
                etats_voisins = self.successeurs(etat_courant)  
                for voisin in etats_voisins:
                    if voisin not in etat_explorer:  
                        etat_explorer.append(voisin)  
                        p.emfiler(voisin)  
        return False
    def dls(self, etat_actuel, etat_final, profondeur_limite):
        if etat_actuel == etat_final:
            return True
        if profondeur_limite <= 0:
            return False
        self.explores[etat_actuel] = True
        successeurs = self.successeurs(etat_actuel)
        for successeur in successeurs:
            if successeur not in self.explores:
                if self.dls(successeur, etat_final, profondeur_limite - 1):
                    return True
        return False
    def dls_incrementation(self, etat_initial, etat_final):
        depth_limit = 0
        while True:
            if self.dls(etat_initial, etat_final, depth_limit):
                return True, depth_limit
                break 
            depth_limit += 1
        
    
        

g= Graphe()
L=3
C=3
for i in range(L):
    for j in range(C):
        g.ajouterNoeud((i, j))


g.ajouterArc((0, 0), (0, 1), True)
g.ajouterArc((0, 0), (1, 0), True)

g.ajouterArc((0, 1), (0, 0), True)
g.ajouterArc((0, 1), (0, 2), True)
g.ajouterArc((0, 1), (1, 1), False)

g.ajouterArc((0, 2), (0, 1), True)
g.ajouterArc((0, 2), (1, 2), True)

g.ajouterArc((1, 0), (0, 0), True)
g.ajouterArc((1, 0), (2, 0), True)
g.ajouterArc((1, 0), (1, 1), False)

g.ajouterArc((1, 1), (1, 0), False)
g.ajouterArc((1, 1), (0, 1), False)
g.ajouterArc((1, 1), (1, 2), False)
g.ajouterArc((1, 1), (2, 1), False)

g.ajouterArc((1, 2), (2, 2), True)
g.ajouterArc((1, 2), (1, 1), False)

g.ajouterArc((2, 0), (1, 0), True)
g.ajouterArc((2, 0), (2, 1), False)

g.ajouterArc((2, 1), (2, 0), False)
g.ajouterArc((2, 1), (2, 2), False)
g.ajouterArc((2, 1), (1, 1), False)

g.ajouterArc((2, 2), (1, 2), True)
g.ajouterArc((2, 2), (2, 1), False)


g.AfficherGraphe()
search_labyrinthe = SearchLabyrinthe(g, (0,0))
successors = search_labyrinthe.successeurs((0,1))
print("les successeurs sont",successors)
verif=search_labyrinthe.dfs(g,(0,0),(2,2))
print(verif)
success, depth = search_labyrinthe.dls_incrementation((0,0), (0,2))
if success:
    print("solution triuver")
else:
    print("pas de solution")
def afficher_labyrinthe(graphe):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    for noeud1, murs in graphe.dictionnaire.items():
        for noeud2, porte in murs.items():
            if porte:  
                ax.plot([noeud1[1], noeud2[1]], [noeud1[0], noeud2[0]], 'k-')
    for noeud in graphe.listerNoeuds():
        ax.plot(noeud[1], noeud[0], 'o', color='black') 
    ax.set_xlim(-1, C)
    ax.set_ylim(-1, L)
    ax.set_xticks(range(C))
    ax.set_yticks(range(L))
    ax.grid(True)
    plt.show()

# Afficher le labyrinthe
afficher_labyrinthe(g)
