import sys
from PyQt5.QtWidgets import *
from sender import sender


class Sending(QWidget):
    def __init__(self):
        super().__init__()

        # Création d'un objet sender
        self.sender_I = sender('')

        # Création des boutons et du layout vertical associé
        self.send = QPushButton('Send')
        self.send.clicked.connect(self.send_clicked)
        self.send.setEnabled(False)

        self.cancel = QPushButton('Cancel')
        self.cancel.clicked.connect(self.cancel_clicked)
        self.cancel.setEnabled(False)

        self.endode = QPushButton('encodage')
        self.endode.clicked.connect(self.encodage_func)
        self.endode.setEnabled(True)

        self.con_checkBox = QCheckBox('Connect')
        self.con_checkBox.stateChanged.connect(self.connect_choice)

        layout_V1 = QVBoxLayout()
        layout_V1.addWidget(self.con_checkBox)

        layout_V1.addWidget(self.send)
        layout_V1.addWidget(self.cancel)

        # Création des widgets pour la zone de texte
        self.message_label = QLabel('Message:')
        self.message_input = QTextEdit()
 
        # Création d'un QLabel pour la clé
        self.key_label = QLabel('Clé:')

        # Création d'un QLabel pour la zone de texte
        self.text_label = QLabel('Texte:')

        # Création du layout vertical pour les QLabel
        layout_V3 = QVBoxLayout()
        layout_V3.addWidget(self.text_label)
        layout_V3.addWidget(self.message_label)

        # Création du layout vertical pour la zone de texte et le bouton encodage
        layout_V2 = QVBoxLayout()
        layout_V2.addLayout(layout_V3)
        layout_V2.addWidget(self.message_input)
        layout_V2.addWidget(self.endode)

        # Ajout des layouts verticaux aux layouts horizontaux
        layout_H = QHBoxLayout()
        layout_H.addLayout(layout_V2)
        layout_H.addLayout(layout_V1)

        # Ajout de la zone de texte et de la clé au layout vertical
        layout_V = QVBoxLayout()
        layout_V.addLayout(layout_H)
        layout_V.addWidget(self.key_label)

        self.setLayout(layout_V)

    def send_clicked(self):
        self.sender_I.data = self.message_input.toPlainText()
        self.sender_I.sendMessage()
        self.key_label.setText('Clé: ' + self.sender_I.key.lower().decode())
        self.message_input.setPlainText('\n'.join(self.sender_I.get_Hist()))
        self.send.setText('Send clicked!')

    def cancel_clicked(self):
        self.cancel.setText('Cancel clicked!')
        self.message_input.setText('')
        self.key_label.setText('Clé:')
        self.send.setText('Send')


    def connect_choice(self):
        if self.con_checkBox.isChecked():
            self.send.setEnabled(True)
            self.cancel.setEnabled(True)
            self.sender_I.connexion()
        else:
            self.send.setEnabled(False)
            self.cancel.setEnabled(False)

    def encodage_func(self):
        self.sender_I.data = self.message_input.toPlainText()
        self.sender_I.encodage_message()
        self.key_label.setText('Clé: ' + self.sender_I.key.decode())

if __name__ == '__main__':
    app1 = QApplication(sys.argv)
    sending_window = Sending()
    sending_window.setWindowTitle('Fenêtre d\'envoi')
    sending_window.setGeometry(100, 100, 400, 400)
    sending_window.show()

    sys.exit(app1.exec_())
