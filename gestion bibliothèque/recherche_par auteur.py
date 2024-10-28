from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class BookSearchWindow(QMainWindow):
    def __init__(self, book_list):
        super().__init__()
        self.book_list = book_list
        self.init_ui()

    def init_ui(self):
        # Créer les widgets
        self.auteurLabel = QLabel('auteur du livre:')
        self.auteurLineEdit = QLineEdit()
        self.searchButton = QPushButton('Rechercher')
        self.resultLabel = QLabel()

        # Créer la disposition de la fenêtre
        layout = QVBoxLayout()
        layout.addWidget(self.auteurLabel)
        layout.addWidget(self.auteurLineEdit)
        layout.addWidget(self.searchButton)
        layout.addWidget(self.resultLabel)

        # Créer le widget de base et définir la disposition
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Définir le titre de la fenêtre
        self.setWindowTitle('Recherche de livre par auteur')

        # Connecter le bouton à la fonction de recherche
        self.searchButton.clicked.connect(self.search_book)

    def search_book(self):
        # Récupérer le titre entré par l'utilisateur
        auteur = self.auteurLineEdit.text()

        # Rechercher le livre dans la liste
        for book in self.book_list:
            if book['auteur'] == auteur:
                self.resultLabel.setText(f"Le auteur {book['auteur']} est disponible.")
                break
        else:
            self.resultLabel.setText(f"Le auteur {auteur} n'a pas été trouvé.")

        # Ajuster la taille de la label en fonction du texte
        self.resultLabel.adjustSize()

if __name__ == '__main__':
    # Créer une liste de livres
    book_list = [
        {'titre': 'Le Seigneur des Anneaux', 'auteur': 'J.R.R. Tolkien', 'annee': 1954},
        {'titre': 'Harry Potter à l\'école des sorciers', 'auteur': 'J.K. Rowling', 'annee': 1997},
        {'titre': '1984', 'auteur': 'George Orwell', 'annee': 1949},
        {'titre': 'Le Petit Prince', 'auteur': 'Antoine de Saint-Exupéry', 'annee': 1943},
        {'titre': 'Le Comte de Monte-Cristo', 'auteur': 'Alexandre Dumas', 'annee': 1844}
    ]

    # Créer l'application et la fenêtre de recherche de livre
    app = QApplication([])
    search_window = BookSearchWindow(book_list)

    # Afficher la fenêtre de recherche de livre
    search_window.show()

    # Exécuter l'application
    app.exec_()

