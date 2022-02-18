import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from form import Ui_MainWindow


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)
        self.setupUi(self)
        '''pattern = '(0-9)'
        re = QtCore.QRegularExpression(pattern)
        validator = QtGui.QRegularExpressionValidator(re, self)
        print(validator.regularExpression())
        self.lineEdit.setValidator(validator)'''
        self.lineEdit.setText('0')
        self.pushButton.clicked.connect(self.digit_pressed)  # 1
        self.pushButton_2.clicked.connect(self.digit_pressed)  # 2
        self.pushButton_3.clicked.connect(self.digit_pressed)  # 3
        self.pushButton_4.clicked.connect(self.digit_pressed)  # 4
        self.pushButton_5.clicked.connect(self.digit_pressed)  # 5
        self.pushButton_6.clicked.connect(self.digit_pressed)  # 6
        self.pushButton_7.clicked.connect(self.digit_pressed)  # 7
        self.pushButton_8.clicked.connect(self.digit_pressed)  # 8
        self.pushButton_9.clicked.connect(self.digit_pressed)  # 9
        self.pushButton_10.clicked.connect(self.digit_pressed)  # 0
        self.pushButton_11.clicked.connect(self.quinary_pressed)
        self.pushButton_12.clicked.connect(self.declaminal_pressed)
        self.pushButton_13.clicked.connect(self.clear)
        self.pushButton_14.clicked.connect(self.digit_pressed)
        self.show()

    def quinary_pressed(self):
        entered_num = str(float(self.lineEdit.text()))
        result = self.quinary_convertion(entered_num)
        self.lineEdit.setText(result)

    def declaminal_pressed(self):
        entered_num = str(float(self.lineEdit.text()))
        if [i for i in '56789' if i in entered_num]:
            self.label.setText("ERROR: Isn't a quinary number!")
            return -1
        self.label.setText("")
        result = self.declaminal_convertion(entered_num)
        self.lineEdit.setText(result)

    def clear(self):
        self.lineEdit.setText('0')

    def quinary_convertion(self, num):
        num = str(float(num)).split('.')
        new = ''
        sign = ''
        if num[0][0] == '-' or num[0][0] == '+':
            sign = num[0][0]
            num[0] = num[0][1:]

        num[0] = int(num[0])
        while num[0]:
            new += str(num[0] % 5)
            num[0] //= 5

        new = new[::-1]
        new += '.'

        num[1] = float('0.' + num[1])
        for i in range(int(self.spinBox.text())):
            num[1] = str(float(num[1]) * 5)
            new += num[1][0]
            num[1] = '0' + num[1][1:]

        print(float(sign + str(new)))
        return f'{float(sign + str(new)):.{int(self.spinBox.text())}f}'


    def declaminal_convertion(self, num):
        num = str(num).split('.')
        new = 0

        sign = ''
        if num[0][0] == '-' or num[0][0] == '+':
            sign = num[0][0]
            num[0] = num[0][1:]

        counter = 0
        for i in num[0][::-1]:
            new += float(i) * (5 ** counter)
            counter += 1

        counter = 1
        for j in num[1]:
            new += float(j) * (5 ** -counter)
            counter += 1
        print(float(sign + str(new)))
        return str(float(sign + str(new)))

    def digit_pressed(self):
        button = self.sender()
        text = self.lineEdit.text()
        if text == '0' and not button.text() == '.':
            self.lineEdit.setText(button.text())
        else:
            self.lineEdit.setText(self.lineEdit.text() + button.text())


app = QtWidgets.QApplication(sys.argv)
window = Calculator()
app.exec()
