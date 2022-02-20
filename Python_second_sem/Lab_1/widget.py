import sys
import math
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.uic.properties import QtCore

from form import Ui_MainWindow
from about import Ui_Dialog


class Calculator(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Calculator, self).__init__(*args, **kwargs)
        self.setupUi(self)
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
        self.pushButton_14.clicked.connect(self.digit_pressed)
        self.pushButton_15.clicked.connect(self.digit_pressed)
        self.pushButton_11.clicked.connect(self.quinary_pressed)
        self.pushButton_12.clicked.connect(self.declaminal_pressed)
        self.pushButton_13.clicked.connect(self.clear)
        self.actionClear_Input.triggered.connect(self.clear)
        self.actionTo_5th_from_10th.triggered.connect(self.quinary_pressed)
        self.actionTo_10th_from_5th.triggered.connect(self.declaminal_pressed)
        self.actionAbout_the_creator_2.triggered.connect(self.about)
        self.show()

    def about(self):
        dialog = QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.exec()

    def float_num_validation(self, input):
        is_float = False
        try:
            input = float(input)
            is_float = True
        finally:
            return is_float


    def quinary_pressed(self):
        entered_num = self.lineEdit.text()
        if not self.float_num_validation(entered_num):
            self.label.setText("ERROR: Isn't a number!")
            return -1
        result = self.conversion(float(entered_num), 5, int(self.spinBox.text()))
        self.lineEdit.setText(result)


    def declaminal_pressed(self):
        entered_num = self.lineEdit.text()
        if not self.float_num_validation(entered_num):
            self.label.setText("ERROR: Isn't a number!")
            return -1
        if [i for i in '56789' if i in entered_num]:
            self.label.setText("ERROR: Isn't a quinary number!")
            return -1
        self.label.setText('')
        result = self.conversion(str(float(entered_num)), 5, int(self.spinBox.text()))
        self.lineEdit.setText(result)

    def clear(self):
        self.lineEdit.setText('0')


    def conversion(self, num, to_radix, maxlen):
        def i_conversion(n, radix=5):
            new = []
            while n:
                n, p = divmod(n, radix)
                new.append('%d' % p)
                if maxlen and len(new) > maxlen:
                    break
            new.reverse()
            return ''.join(new)

        def f_conversion(n, radix=5):
            new = []
            f = math.modf(n)[0]
            while f:
                f, p = math.modf(f * radix)
                new.append('%.0f' % p)
                if maxlen and len(new) > maxlen:
                    break
            return ''.join(new)

        def extract_sign(num):
            num = str(num)
            sign = ''
            if num[0] == '-':
                sign = '-'
                num = num[1:]
            return sign, float(num)

        if isinstance(num, float):
            sign, num = extract_sign(num)

            return sign + (i_conversion(num, to_radix) if i_conversion(num, to_radix) else '0') + '.'\
                   + (f_conversion(num, to_radix) if f_conversion(num, to_radix) else '0')

        elif isinstance(num, str):
            sign, num = extract_sign(num)

            f_string = '{:.' + str(maxlen) + 'f}'
            n, f = f_string.format(num).split('.')
            n = int(n, to_radix)
            f = int(f, to_radix) / float(to_radix ** len(f))
            return sign + str(float(n + f))



    def digit_pressed(self):
        button = self.sender()
        text = self.lineEdit.text()
        if text == '0' and not button.text() == '.':
            self.lineEdit.setText(button.text())
        else:
            self.lineEdit.setText(self.lineEdit.text() + button.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    app.exec()
