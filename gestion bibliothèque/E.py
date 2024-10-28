import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class BookSearchWindow(QDialog):
    def __init__(self, book_list):
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        # Créer les widgets
        #self.referenceLabel = QLabel('Réference du livre:')
        #self.referenceLineEdit = QLineEdit(self)
        #self.searchButton = QPushButton('Rechercher')
        self.referenceLabel = QLabel(self)
        
        self.reference_label.setText("Entrez le referrence du livre  :")
        self.reference_label.move(20, 20)

        self.reference_edit = QLineEdit(self)
        self.reference_edit.move(150, 20)
        self.resultLabel = QLabel(self)

        # Créer la disposition de la fenêtre
        #layout = QVBoxLayout()
        #layout.addWidget(self.referenceLabel)
        #layout.addWidget(self.referenceLineEdit)
        #layout.addWidget(self.searchButton)
        #layout.addWidget(self.resultLabel)

        # Créer le widget de base et définir la disposition
        #widget = QWidget()
        #widget.setLayout(layout)
        #self.setCentralWidget(widget)

        # Définir le titre de la fenêtre
        self.setWindowTitle('Recherche de livre par Réference')

        # Connecter le bouton à la fonction de recherche
        self.rechercge_button = QPushButton(self)
        self.recherche_button.setText("recherche")
        self.searchButton.clicked.connect(self.search_book)

    def search_book(self):
        # Récupérer le titre entré par l'utilisateur
        reference = self.reference_edit.text()

        # Rechercher le livre dans la liste
        for book in self.book_list:
            if book['reference'] == reference:
                self.resultLabel.setText(f"Le réference {book['reference']} est disponible.")
                break
        else:
            self.resultLabel.setText(f"Le reference {reference} n'a pas été trouvé.")

        # Ajuster la taille de la label en fonction du texte
        self.resultLabel.adjustSize()


class BookDeleteWindows(QDialog):
    def __init__(self, book_list):
        super().__init__()
        self.setWindowTitle("Supprimer un livre")

        # Créer un champ de saisie pour l'auteur du livre à supprimer
        self.annee_label = QLabel(self)
        self.annee_label.setText("Entrez l'année d'dedition du livre à supprimer :")
        self.annee_label.move(20, 20)

        self.annee_edit = QLineEdit(self)
        self.annee_edit.move(150, 20)

        # Créer le bouton de suppression
        self.delete_button = QPushButton(self)
        self.delete_button.setText("Supprimer")
        self.delete_button.move(150, 50)
        self.delete_button.clicked.connect(self.delete_book)

        # Définir la liste de livres
        self.book_list = book_list

    def delete_book(self):
        # Récupérer le nom de l'auteur entré par l'utilisateur
        annee = self.annee_edit.text()

        # Chercher le livre dans la liste
        index_to_remove = None
        for i, book in enumerate(self.book_list):
            if book['annee'].lower() == annee.lower():
                index_to_remove = i
                break

        # Si le livre a été trouvé, le supprimer de la liste
        if index_to_remove is not None:
            del self.book_list[index_to_remove]
            print(f"Livre supprimé : {annee}")
        else:
            print(f"Livre non trouvé : {annee}")

        # Fermer la fenêtre de suppression
        self.close()

class BookEditWindow(QDialog):
    def __init__(self, book_list):
        super().__init__()
        self.setWindowTitle("Modifier le nombre d'exemplaires d'un livre")

        # Créer un champ de saisie pour le titre du livre à modifier
        self.nombre_label = QLabel(self)
        self.nombre_label.setText("Entrez le nombre d'exemplaire du livre  :")
        self.nombre_label.move(20, 20)

        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.move(300, 20)

        # Créer un champ de saisie pour le nouveau titre
        self.new_nombre_label = QLabel(self)
        self.new_nombre_label.setText("Entrez le nouveau nombre d'exemplaire :")
        self.new_nombre_label.move(20, 50)

        self.new_nombre_edit = QLineEdit(self)
        self.new_nombre_edit.move(300, 50)

        # Créer le bouton de modification
        self.edit_button = QPushButton(self)
        self.edit_button.setText("Modifier")
        self.edit_button.move(300, 80)
        self.edit_button.clicked.connect(self.edit_book)

        # Définir la liste de livres
        self.book_list = book_list

    def edit_book(self):
        # Récupérer le titre et le nouveau titre entrés par l'utilisateur
        nombre = self.nombre_edit.text()
        new_nombre = self.new_nombre_edit.text()

        # Chercher le livre dans la liste
        book_found = False
        for book in self.book_list:
            if book['nombre'].lower() == nombre.lower():
                book_found = True
                book['nombre'] = new_nombre
                print(f"Titre modifié : {nombre} -> {new_nombre}")
                break

        # Si le livre n'a pas été trouvé, afficher un message d'erreur
        if not book_found:
            print(f"Livre non trouvé : {nombre}")

        # Fermer la fenêtre de modification
        self.close()
class BookDeleteWindow(QDialog):
    def __init__(self, book_list):
        super().__init__()
        self.setWindowTitle("Supprimer un livre")

        # Créer un champ de saisie pour l'auteur du livre à supprimer
        self.author_label = QLabel(self)
        self.author_label.setText("Entrez l'auteur du livre à supprimer :")
        self.author_label.move(20, 20)

        self.author_edit = QLineEdit(self)
        self.author_edit.move(150, 20)

        # Créer le bouton de suppression
        self.delete_button = QPushButton(self)
        self.delete_button.setText("Supprimer")
        self.delete_button.move(150, 50)
        self.delete_button.clicked.connect(self.delete_book)

        # Définir la liste de livres
        self.book_list = book_list

    def delete_book(self):
        # Récupérer le nom de l'auteur entré par l'utilisateur
        author = self.author_edit.text()

        # Chercher le livre dans la liste
        index_to_remove = None
        for i, book in enumerate(self.book_list):
            if book['auteur'].lower() == author.lower():
                index_to_remove = i
                break

        # Si le livre a été trouvé, le supprimer de la liste
        if index_to_remove is not None:
            del self.book_list[index_to_remove]
            print(f"Livre supprimé : {author}")
        else:
            print(f"Livre non trouvé : {author}")

        # Fermer la fenêtre de suppression
        self.close()
class Ajouter_livre(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ajouter un livre")
        self.reference_edit = QLineEdit()
        self.title_edit = QLineEdit()
        self.author_edit = QLineEdit()
        self.year_edit = QLineEdit()
        self.copies_edit = QlineEdit()

        self.delete_button = QPushButton(self)
        self.delete_button.setText("ajouter")
        self.delete_button.move(150, 50)
        self.delete_button.clicked.connect(self.ajouter_book)
    def ajouter_book(self):
        
        # Ajouter le livre à la liste
        reference = self.author_edit.text()
        titre=self.title_edit.text()
        auteur=self.author_edit.text()
        annee=self.year_edit.text()
        copies=self.copies_edit.text()
        book = {'Référence': reference, 'Titre': titre, 'Auteur': auteur, 'Année': annee, 'Nombre d\'exemplaires': copies}
        self.book_list.append(book)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion ")
        menu_bar = self.menuBar()
        afficher_menu = menu_bar.addMenu("Gestion livre")
        afficher_livre_action = QAction("Ajouter un livre", self)
        afficher_livre_action.triggered.connect(self.ajouterlivre)
        afficher_menu.addAction(afficher_livre_action)
        supprimer_livre_action = QAction("Supprimer un livre par  auteur", self)
        supprimer_livre_action.triggered.connect(self.supprimer_livre)
        afficher_menu.addAction(supprimer_livre_action)
        supprimer_livre_annee_action = QAction("Supprimer un livre par anne", self)
        supprimer_livre_annee_action.triggered.connect(self.supprimer_livre_annee)
        afficher_menu.addAction(supprimer_livre_annee_action)
        modifier_livre_action = QAction("Modifier un livre", self)
        modifier_livre_action.triggered.connect(self.modifier_livre)
        afficher_menu.addAction(modifier_livre_action)
        recherche_livreR_action = QAction("recherche un livre par reference", self)
        recherche_livreR_action.triggered.connect(self.recherche_livreR)
        afficher_menu.addAction(recherche_livreR_action)
    def supprimer_livre_annee(self):
        dialog = BookDeleteWindows(book_list)
        dialog.exec_()

    def afficher_etudiants(self):
        dialog = AfficherEtudiantDialog(self)
        dialog.exec_()
    def ajouterlivre(self):
        dialog = Ajouter_livre(book_list)
        dialog.exec_()
    def supprimer_livre(self):
        dialog = BookDeleteWindow(book_list)
        dialog.exec_()
    def modifier_livre(self):
        dialog = BookEditWindow(book_list)
        dialog.exec_()
    def recherche_livreR(self):
        dialog = BookSearchWindow(book_list)
        dialog.exec_()  
book_list = [
    {"reference":"1234",'titre': 'L\'Étranger', 'auteur': 'Albert Camus', 'annee': "1942","nombre_exemplaire":"4678"},
    {"reference":"134",'titre': 'La Peste', 'auteur': 'Albert Camus', 'annee': "1947","nombre_exemplaire":"4568"},
    {"reference":"124",'titre': 'Les Misérables', 'auteur': 'Victor Hugo', 'annee': "1862","nombre_exemplaire":"4567"},
 ]
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

        