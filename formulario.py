import sys
from typing import List
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QApplication, QPushButton, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class Funcionario:

    def __init__(self, nome = None, sexo = None) -> None:
        self.nome = nome
        self.sexo = sexo


class Formulario(QMainWindow):

    def __init__(self, parent = None) -> None:
        super().__init__(parent=parent)        

        self.funcionarios : List[Funcionario] = []
        
        self.label_mensagem = QLabel()
        self.label_mensagem.setVisible(False)
        self.label_mensagem.setStyleSheet('''
            color: green;
            font-weight: bold;
        ''')

        self.label_nome = QLabel()  
        self.label_nome.setText('Digite seu nome')
        self.line_edit_nome = QLineEdit()
        self.line_edit_nome.textChanged.connect(self.change_text)

        self.label_sexo = QLabel()
        self.label_sexo.setText('Digite seu sexo')        
        self.line_edit_sexo = QLineEdit()
        self.line_edit_sexo.textChanged.connect(self.change_text)

        self.button_adicionar = QPushButton('Adicionar')
        self.button_adicionar.setEnabled(False)
        self.button_adicionar.clicked.connect(self.adicionar)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(['Nome', 'Sexo'])
        self.tabela.setRowCount(0)

        # space = QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)

        self.vertical = QVBoxLayout()

        self.vertical.addWidget(self.label_mensagem)

        self.vertical.addWidget(self.label_nome)
        self.vertical.addWidget(self.line_edit_nome)

        self.vertical.addWidget(self.label_sexo)
        self.vertical.addWidget(self.line_edit_sexo)

        self.vertical.addWidget(self.button_adicionar)

        self.vertical.addWidget(self.tabela)
        
        # self.vertical.addItem(space)

        self.widget = QWidget()
        self.widget.setLayout(self.vertical)

        self.setCentralWidget(self.widget)

        self.setWindowTitle('Curso de Python Básico')
        self.setGeometry(300, 300, 600, 400)
    

    def change_text(self):
        self.button_adicionar.setEnabled(self.line_edit_nome.text() != '' and self.line_edit_sexo.text() != '')

    def adicionar(self):    
        funcionario = Funcionario()
        funcionario.nome = self.line_edit_nome.text()
        funcionario.sexo = self.line_edit_sexo.text()

        self.funcionarios.append(funcionario)

        self.listar()

        self.label_mensagem.setText('Adicionado com sucesso')
        self.label_mensagem.setVisible(True)

        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda : self.label_mensagem.setVisible(False))
        timer.start(2000)

    def listar(self):
        self.tabela.setRowCount(len(self.funcionarios))

        for linha, registro in enumerate(self.funcionarios):
            nome = QTableWidgetItem()
            nome.setText(registro.nome)
            nome.setData(QtCore.Qt.UserRole, registro)

            sexo = QTableWidgetItem()
            sexo.setText(registro.sexo)

            self.tabela.setItem(linha, 0, nome)
            self.tabela.setItem(linha, 1, sexo)


app = QApplication(sys.argv)


formulario = Formulario()
formulario.show()

sys.exit(app.exec_())
