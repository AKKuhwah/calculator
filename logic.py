from logging import exception

from PyQt6.QtWidgets import *
from gui import *
import math

class Logic(QMainWindow, Ui_MainWindow):
    """
    Logic class for handling the calculator's operations: add, subtract, divide
    multioply and geometric calculations: circle, square, rectangle, triangle

    Inherits from QMainWindow and Ui_MainWindow.
    """
    def __init__(self):
        """
        Creates the Logic class, sets up UI, and connects button actions.
        Hides geometric mode buttons and sets the display screen as read-only.
        """
        super().__init__()
        self.setupUi(self)

        #make display screen uneditable
        self.displayScreen.setReadOnly(True)

        #mode hide button
        self.circleButton.hide()
        self.squareButton.hide()
        self.rectangleButton.hide()
        self.triangleButton.hide()
        self.submitOne.hide()
        self.submitTwo.hide()
        self.label.hide()
        self.label_2.hide()
        self.inputOne.hide()
        self.inputTwo.hide()

        self.equalButton.clicked.connect(lambda: self.equal())
        self.clearButton.clicked.connect(lambda: self.clear())
        self.zeroButton.clicked.connect(lambda: self.numClick('0'))
        self.oneButton.clicked.connect(lambda: self.numClick('1'))
        self.twoButton.clicked.connect(lambda: self.numClick('2'))
        self.threeButton.clicked.connect(lambda: self.numClick('3'))
        self.fourButton.clicked.connect(lambda: self.numClick('4'))
        self.fiveButton.clicked.connect(lambda: self.numClick('5'))
        self.sixButton.clicked.connect(lambda: self.numClick('6'))
        self.sevenButton.clicked.connect(lambda: self.numClick('7'))
        self.eightButton.clicked.connect(lambda: self.numClick('8'))
        self.nineButton.clicked.connect(lambda: self.numClick('9'))
        self.divideButton.clicked.connect(lambda: self.symbolClick('/'))
        self.multiplyButton.clicked.connect(lambda: self.symbolClick('*'))
        self.subtractButton.clicked.connect(lambda: self.symbolClick('-'))
        self.addButton.clicked.connect(lambda: self.symbolClick('+'))
        self.delButton.clicked.connect(lambda: self.delete())
        self.modeButton.clicked.connect(lambda: self.mode())
        self.periodButton.clicked.connect(lambda: self.period())

        #mode method
        self.circleButton.clicked.connect(lambda: self.showEquation())
        self.squareButton.clicked.connect(lambda: self.showEquation())
        self.triangleButton.clicked.connect(lambda: self.showEquation())
        self.rectangleButton.clicked.connect(lambda: self.showEquation())


        self.firstNum = ''
        self.secondNum = ''
        self.equationSymbol = ''
        self.newNum = False

    def showEquation(self):
        """
        Shows the input fields and submit button based on the selected radio button
        """
        if self.circleButton.isChecked():
            self.label.show()
            self.label_2.hide()
            self.inputOne.show()
            self.inputTwo.hide()
            self.submitOne.show()
        if self.squareButton.isChecked():
            self.label.show()
            self.label_2.hide()
            self.inputOne.show()
            self.inputTwo.hide()
            self.submitOne.show()
        if self.rectangleButton.isChecked():
            self.label.show()
            self.label_2.show()
            self.inputOne.show()
            self.inputTwo.show()
            self.submitOne.show()
        if self.triangleButton.isChecked():
            self.label.show()
            self.label_2.show()
            self.inputOne.show()
            self.inputTwo.show()
            self.submitOne.show()

        #math lol
        self.submitOne.clicked.connect(lambda: doMath())

        def doMath():
            """
            Calculates and shows the area of the geometric radio button selected
            """
            try:
                if self.circleButton.isChecked():
                    radius = self.inputOne.text()
                    radius = float(radius)
                    answer = math.pi * radius * radius
                    self.displayScreen.setText(f'Area = {answer}')
                if self.squareButton.isChecked():
                    num = self.inputOne.text()
                    num = float(num)
                    answer = num * num
                    self.displayScreen.setText(f'Area = {answer}')
                if self.rectangleButton.isChecked():
                    numOne = self.inputOne.text()
                    numTwo = self.inputTwo.text()
                    numOne = float(numOne)
                    numTwo = float(numTwo)
                    answer = numOne * numTwo
                    self.displayScreen.setText(f'Area = {answer}')
                if self.triangleButton.isChecked():
                    numOne = self.inputOne.text()
                    numTwo = self.inputTwo.text()
                    numOne = float(numOne)
                    numTwo = float(numTwo)
                    answer = (numOne * numTwo)/2
                    self.displayScreen.setText(f'Area = {answer}')
            except:
                self.displayScreen.setText('ERROR')


    #no period after the first one there
    def period(self):
        """
        Adds a period (decimal point) to the current number being entered
        can't add more than one period to a number
        """
        displayEquation = self.displayScreen.text()
        displayEquation = list(displayEquation)
        for x in displayEquation:
            if x == '.':
                break
        else:
            if self.equationSymbol == '':
                self.firstNum += '.'
                self.displayScreen.setText(f'{self.firstNum}')
            else:
                self.secondNum += '.'
                self.displayScreen.setText(f'{self.firstNum} {self.equationSymbol} {self.secondNum}')

    def equal(self):
        """
        Caculates the operation based on the selected equation symbol and shows the result.
        """
        try:
            numOne = float(self.firstNum)
            numTwo = float(self.secondNum)
            total = 0
            if self.equationSymbol == '/':
                total = numOne / numTwo
            if self.equationSymbol == '*':
                total = numOne * numTwo
            if self.equationSymbol == '-':
                total = numOne - numTwo
            if self.equationSymbol == '+':
                total = numOne + numTwo

            self.displayScreen.setText(f'ANS = {total}')
            self.clearValue()
        except:
            self.displayScreen.setText('Error')
            self.clearValue()

    def clear(self):
        """
        Clears the current input values and resets the display screen.
        """
        self.firstNum = ''
        self.secondNum = ''
        self.equationSymbol = ''
        self.newNum = False
        self.displayScreen.setText('')

    def clearValue(self):
        """
        Clears the current equation values but keeps the UI in its current state.
        """
        self.firstNum = ''
        self.secondNum = ''
        self.equationSymbol = ''
        self.newNum = False

    def numClick(self, num):
        """
        Adds the clicked number to the current equation being built.

        :param num: The digit to add to the current equation.
        """
        if self.newNum:
            self.secondNum += num
            self.displayScreen.setText(f'{self.firstNum} {self.equationSymbol} {self.secondNum}')
        else:
            self.firstNum += num
            self.displayScreen.setText(f'{self.firstNum}')

    def symbolClick(self, symbol):
        """
        Sets the selected arithmetic operator and prepares the UI for the next number.

        :param symbol: The operator to apply to the current equation.
        """
        try:
            if self.firstNum == '':
                raise exception()
            self.equationSymbol = symbol
            self.displayScreen.setText(f'{self.firstNum} {self.equationSymbol}')
            self.newNum = True
        except:
            self.displayScreen.setText('Choose a number first')

    def delete(self):
        """
        Deletes the last character in the current equation.
        """
        if self.secondNum != '':
            self.secondNum = self.secondNum[:-1]
        elif self.equationSymbol != '':
            self.equationSymbol = self.equationSymbol[:-1]
        elif self.firstNum != '':
            self.firstNum = self.firstNum[:-1]
        wholeEquation = self.firstNum + self.equationSymbol + self.secondNum
        self.displayScreen.setText(wholeEquation)

    def mode(self):
        """
        Toggles the visibility of the geometric mode buttons.
        """
        if self.circleButton.isVisible():
            self.circleButton.hide()
            self.squareButton.hide()
            self.rectangleButton.hide()
            self.triangleButton.hide()
        else:
            self.circleButton.show()
            self.squareButton.show()
            self.rectangleButton.show()
            self.triangleButton.show()
