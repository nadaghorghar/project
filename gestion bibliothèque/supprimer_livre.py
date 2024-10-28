from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class BookDeleteWindow(QMainWindow):
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

# Créer une liste de livres pour tester la fonction
book_list = [
    {'titre': 'L\'Étranger', 'auteur': 'Albert Camus', 'annee': 1942},
    {'titre': 'La Peste', 'auteur': 'Albert Camus', 'annee': 1947},
    {'titre': 'Les Misérables', 'auteur': 'Victor Hugo', 'annee': 1862},
    {'titre': 'Madame Bovary', 'auteur': 'Gustave Flaubert', 'annee': 1856}
]

# Créer et afficher la fenêtre de suppression
app = QApplication([])
window = BookDeleteWindow(book_list)
window.show()
app.exec_()

