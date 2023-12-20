import sys
from PyQt5.QtWidgets import *
from functools import partial
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.buffer = ''
        self.value_buffer = False

    def init_ui(self):
        main_layout = QVBoxLayout()

        layout_equation_solution = QFormLayout()

        self.equation = QLineEdit("")

        layout_equation_solution.addRow(self.equation)

        main_layout.addLayout(layout_equation_solution)

        grid_layout = QGridLayout()

        buttons = [
            ('%', 0, 0),('CE', 0, 1),('C', 0, 2),('<-', 0, 3),
            ('1/x', 1, 0),('x²', 1, 1),('2√x', 1, 2),('÷', 1, 3),
            ('7', 2, 0),('8', 2, 1),('9', 2, 2),('x', 2, 3),
            ('4', 3, 0),('5', 3, 1),('6', 3, 2),('-', 3, 3),
            ('1', 4, 0),('2', 4, 1),('3', 4, 2),('+', 4, 3),
            ('00', 5, 0),('0', 5, 1),('.', 5, 2),('=', 5, 3)
        ]

        for btn_text, row, col in buttons:
            button = QPushButton(btn_text)
            if btn_text.isdigit():
                button.clicked.connect(partial(self.number_button_clicked, btn_text))
            else:
                if btn_text in ['+', '-', '*']:
                    button.clicked.connect(partial(self.button_operation_clicked, btn_text))
                if btn_text == '÷':
                    button.clicked.connect(partial(self.button_operation_clicked, '/'))
                if btn_text == '=':
                    button.clicked.connect(self.button_equal_clicked)
                if btn_text == 'C':
                    button.clicked.connect(self.button_clear_clicked)
                if btn_text == '<-':
                    button.clicked.connect(self.button_backspace_clicked)
                if btn_text == '%':
                    button.clicked.connect(partial(self.button_operation_clicked, btn_text))
                if btn_text == 'CE':
                    button.clicked.connect(self.button_ce_clicked)
                if btn_text == '1/x':
                    button.clicked.connect(self.button_inverse_clicked)
                if btn_text == 'x²':
                    button.clicked.connect(self.button_square_clicked)
                if btn_text == '2√x':
                    button.clicked.connect(self.button_square_root_clicked)
            grid_layout.addWidget(button, row, col)

        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)


    def button_equal_clicked(self):
        result = self.buffer
        try:
            solution = str(eval(result))
            self.equation.setText(solution)  # 계산 결과를 해당 LineEdit에 표시
        except Exception as e:
            self.equation.setText("Error")

    def button_clear_clicked(self):
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

    def button_ce_clicked(self):
        self.equation.setText("")

    def button_inverse_clicked(self):
        try:
            value = float(self.equation.text())
            result = 1 / value
            self.equation.setText(str(result))
        except ValueError:
            self.equation.setText("Error")
    
    def button_square_clicked(self):
        try:
            value = float(self.equation.text())
            result = value ** 2
            self.equation.setText(str(result))
        except ValueError:
            self.equation.setText("Error")

    def button_square_root_clicked(self):
        try:
            value = float(self.equation.text())
            result = math.sqrt(value)
            self.equation.setText(str(result))
        except ValueError:
            self.equation.setText("Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())