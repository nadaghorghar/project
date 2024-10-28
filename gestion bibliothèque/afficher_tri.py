from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QListWidget, QVBoxLayout, QWidget

class BookListWindow(QMainWindow):
    def __init__(self, book_list):
        super().__init__()
        self.setWindowTitle("Liste des livres par titre")

        # Créer un widget de liste pour afficher les livres
        self.book_list_widget = QListWidget(self)

        # Trier la liste des livres par titre
        sorted_book_list = sorted(book_list, key=lambda x: x['titre'])

        # Ajouter chaque livre à la liste
        for book in sorted_book_list:
            self.book_list_widget.addItem(f"{book['titre']} - {book['auteur']} ({book['annee']})")

        # Ajouter le widget de liste à un layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.book_list_widget)

        # Ajouter le layout à un widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Définir la taille de la fenêtre
        self.setGeometry(200, 200, 600, 400)

# Créer une liste de livres pour tester la fonction
book_list = [
    {'titre': 'L\'Étranger', 'auteur': 'Albert Camus', 'annee': 1942},
    {'titre': 'La Peste', 'auteur': 'Albert Camus', 'annee': 1947},
    {'titre': 'Les Misérables', 'auteur': 'Victor Hugo', 'annee': 1862},
    {'titre': 'Madame Bovary', 'auteur': 'Gustave Flaubert', 'annee': 1856},
    {'titre': '1984', 'auteur': 'George Orwell', 'annee': 1949},
    {'titre': 'Le Rouge et le Noir', 'auteur': 'Stendhal', 'annee': 1830},
    {'titre': 'Voyage au bout de la nuit', 'auteur': 'Louis-Ferdinand Céline', 'annee': 1932},
    {'titre': 'Les Fleurs du mal', 'auteur': 'Charles Baudelaire', 'annee': 1857}
]

# Créer et afficher la fenêtre de liste des livres
app = QApplication([])
window = BookListWindow(book_list)
window.show()
app.exec_()

