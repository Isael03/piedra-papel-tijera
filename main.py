from juego import maquina, match, resultado
from PyQt5 import QtWidgets, uic
from PyQt5 import *
from PyQt5.QtWidgets import *
import sys
from os import path


class UI_Choose(QtWidgets.QMainWindow):
    appWindow = None
    playerChoice: str = ''
    radioGroup = None

    def __init__(self):
        super(UI_Choose, self).__init__()
        self.appWindow = uic.loadUi(path.join('ui', 'choose.ui'), self)
        #self.appWindow = uic.loadUi('choose.ui', self)

        self.appWindow.btnExit.clicked.connect(self.exitApp)
        self.appWindow.btnPlay.clicked.connect(self.showResults)

        self.radioGroup = QButtonGroup()
        self.radioGroup.addButton(self.rdbPiedra)
        self.radioGroup.addButton(self.rdbTijera)
        self.radioGroup.addButton(self.rdbPapel)

        self.show()
        self.init_ui()

    def init_ui(self):
        self.rdbPiedra.toggled.connect(self.onClicked)
        self.rdbPapel.toggled.connect(self.onClicked)
        self.rdbTijera.toggled.connect(self.onClicked)

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.playerChoice = radioBtn.text()
            # print(self.playerChoice)

    def showResults(self):
        if self.playerChoice != '':
            uiResult = UI_Result(self.playerChoice, self.appWindow)
            uiResult.show()

            self.radioGroup.setExclusive(False)
            self.rdbPapel.setChecked(False)
            self.rdbTijera.setChecked(False)
            self.rdbPiedra.setChecked(False)
            self.radioGroup.setExclusive(True)

            self.hide()

    def exitApp(self):
        sys.exit(app.exec())


class UI_Result(QtWidgets.QMainWindow):
    playerChoice: str
    machineChoice: str
    result: str
    appWindow = None
    ui_choose = None

    def __init__(self, playerChoice, ui_choose):
        super(UI_Result, self).__init__()
        self.appWindow = uic.loadUi(path.join('ui', 'result.ui'), self)
        #self.appWindow = uic.loadUi('result.ui', self)
        self.playerChoice = playerChoice
        self.machineChoice = maquina()
        self.ui_choose = ui_choose

        self.appWindow.btnExit.clicked.connect(self.exitApp)
        self.appWindow.btnAgain.clicked.connect(self.comeback)

        self.lblJugador.setText(self.playerChoice)
        self.lblMaquina.setText(self.machineChoice)

        self.result = match(self.playerChoice.lower(), self.machineChoice.lower())
        self.lblResultado.setText(resultado(self.result).upper())

    def comeback(self):
        self.ui_choose.show()
        self.close()

    def exitApp(self):
        sys.exit(app.exec())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    windowWelcome = UI_Choose()
    sys.exit(app.exec())
