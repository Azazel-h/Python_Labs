import sys
from PyQt6 import QtWidgets

from main_ui import Ui_MainWindow

class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculate)
        self.show()

    def calculate(self):
        entered_num1 = list(map(int, list(self.lineEdit.text())))[::-1]
        entered_num2 = list(map(int, list(self.lineEdit_2.text())))[::-1]

        size = max(len(entered_num1), len(entered_num2))
        entered_num1 += [0] * (size - len(entered_num1))
        entered_num2 += [0] * (size - len(entered_num2))

        overflow = 0
        result = []
        for i in zip(entered_num1, entered_num2):
            value = i[0] + i[1] + overflow
            overflow = value // 2
            result.append(value % 2)

        if overflow == 1:
            result.append(1)
        result = result[::-1]

        self.label.setText(''.join(map(str, result)))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    app.exec()