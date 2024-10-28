from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Créer la liste
        self.list_widget = QListWidget()
        self.setCentralWidget(self.list_widget)

        # Ajouter un bouton pour ajouter un livre
        add_button = QPushButton('Ajouter un livre', self)
        add_button.clicked.connect(self.add_book)
        self.toolbar = self.addToolBar('Ajouter un livre')
        self.toolbar.addWidget(add_button)

    def add_book(self):
        # Créer une boîte de dialogue pour saisir les caractéristiques du livre
        dialog = QDialog(self)
        dialog.setWindowTitle('Ajouter un livre')
        form = QFormLayout(dialog)

        Réference = QLineEdit()
        titre = QLineEdit()
        nom_prenon_auteur = QLineEdit()
        année_edition = QLineEdit()
        nombre_d_exemplaires = QLineEdit()
        form.addRow('Réference : ', Réference)
        form.addRow('titre : ', titre)
        form.addRow(' nom_prenon_auteur: ', nom_prenon_auteur)
        form.addRow('année_edition : ', année_edition)
        form.addRow('nombre d exemplaires : ', nombre_d_exemplaires)

        # Ajouter un bouton pour valider la saisie
        submit_button = QPushButton('Valider', dialog)
        submit_button.clicked.connect(lambda: self.submit_book(Réference.text(), titre.text(), nom_prenon_auteur.text(),année_edition.text(),nombre_d_exemplaires.text()))
        form.addRow(submit_button)

        # Afficher la boîte de dialogue
        dialog.exec_()

    def submit_book(self, Réference,titre,nom_prenom_auteur,année_edition,nombre_d_exemplaires):
        # Ajouter le livre à la liste
        book =f'({Réference},{titre},{nom_prenom_auteur},{année_edition},{nombre_d_exemplaires})'
        self.list_widget.addItem(book)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())