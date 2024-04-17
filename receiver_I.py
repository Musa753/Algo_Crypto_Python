import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from receiver import Receiver

class Receiving(QWidget):
    def __init__(self):
        super().__init__()

        # Création d'un objet receiver
        self.receiver= Receiver()

        # Création des boutons et du layout vertical associé
        self.recv = QPushButton('recv')
        self.recv.clicked.connect(self.recv_clicked)
        self.recv.setEnabled(False)

        self.decode = QPushButton('decodage')
        self.decode.clicked.connect(self.decodage)
        self.decode.setEnabled(True)

        self.con_checkBox = QCheckBox('Connect')
        self.con_checkBox.stateChanged.connect(self.connect_choice)

        layout_H1 = QHBoxLayout()
        layout_H1.addWidget(self.con_checkBox)
        layout_H1.addWidget(self.recv)
     
        # Création des widgets pour la zone de texte
        self.message_label = QLabel('Message:')
        self.key_label = QLabel('clé')

        layout_V = QVBoxLayout()
        layout_V.addWidget(self.message_label)
        layout_V.addWidget(self.key_label)

        # Ajout d'un QTextEdit pour afficher le message
        self.message_text_edit = QTextEdit()
        layout_V.addWidget(self.message_text_edit)
        layout_V.addWidget(self.decode)

        # Ajout des widgets aux layouts horizontaux et verticaux
        layout_H = QVBoxLayout()
        layout_H.addLayout(layout_H1)
        layout_H.addLayout(layout_V)
        

        self.setLayout(layout_H)

    def recv_clicked(self):
        self.receiver.RecvMessage()
        self.key_label.setText("clé:"+self.receiver.key)
        self.recv.setText("recv clicked")
 
    def connect_choice(self):
        if self.con_checkBox.isChecked():
            self.recv.setEnabled(True)
            self.receiver.connexion()
        else:
            self.recv.setEnabled(False)
 
    def decodage(self):
        self.message_label.setText(self.receiver.data)
        self.message_text_edit.setPlainText('\n'.join(self.receiver.get_Hist()))

if __name__ == '__main__':           
    app2 = QApplication(sys.argv)
    receiving_window = Receiving()
    receiving_window.setWindowTitle('Fenêtre de réception')
    receiving_window.setGeometry(500, 100, 400, 400)
    receiving_window.show()
    
    sys.exit(app2.exec_())
