from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class BookEditWindow(QMainWindow):
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

# Créer une liste de livres pour tester la fonction
book_list = [
    {'nombre': 'L\'Étranger', 'auteur': 'Albert Camus', 'annee': 1942},
    {'nombre': 'La Peste', 'auteur': 'Albert Camus', 'annee': 1947},
    {'nombre': 'Les Misérables', 'auteur': 'Victor Hugo', 'annee': 1862},
    {'nombre': 'Madame Bovary', 'auteur': 'Gustave Flaubert', 'annee': 1856}
]

# Créer et afficher la fenêtre de modification
app = QApplication([])
window = BookEditWindow(book_list)
window.show()
app.exec_()
