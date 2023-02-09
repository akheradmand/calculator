import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

operator=""

def num(x):
    main_window.txt_box.setText(main_window.txt_box.text()+x)

def decimal_point():
    main_window.txt_box.setText(main_window.txt_box.text()+'.')

def AC():
    main_window.txt_box.setText("")

def change_sign():
    main_window.txt_box.setText(str(-1*float(main_window.txt_box.text())))

def percent():
    main_window.txt_box.setText(str(float(main_window.txt_box.text())/100))

def reverse():
    main_window.txt_box.setText(str(1/float(main_window.txt_box.text())))

def sum():
    global a,operator
    a=float(main_window.txt_box.text())
    operator="+"
    main_window.txt_box.setText("")

def sub():
    global a,operator
    a=float(main_window.txt_box.text())
    operator="-"
    main_window.txt_box.setText("")

def mul():
    global a,operator
    a=float(main_window.txt_box.text())
    operator="*"
    main_window.txt_box.setText("")

def div():
    global a,operator
    a=float(main_window.txt_box.text())
    operator="/"
    main_window.txt_box.setText("")

def sin():
    main_window.txt_box.setText(str(math.sin(float(main_window.txt_box.text()))))

def cos():
    main_window.txt_box.setText(str(math.cos(float(main_window.txt_box.text()))))

def tan():
    main_window.txt_box.setText(str(math.tan(float(main_window.txt_box.text()))))

def cot():
    main_window.txt_box.setText(str(1/math.tan(float(main_window.txt_box.text()))))

def log():
    main_window.txt_box.setText(str(math.log(float(main_window.txt_box.text()))))

def sqrt():
    main_window.txt_box.setText(str(math.sqrt(float(main_window.txt_box.text()))))

def result():
    b=float(main_window.txt_box.text())
    if operator=="+":
        c=a+b
    elif operator=="-":
        c=a-b
    elif operator=="*":
        c=a*b
    elif operator=="/":
        if b!=0:
            c=a/b
        elif b==0:
            c="Cannot divide by zero"
    main_window.txt_box.setText(str(c))

app=QApplication([])
loader=QUiLoader()
main_window=loader.load("calculator/calculator.ui")
main_window.show()

main_window.btn_zero.clicked.connect(partial(num,"0"))
main_window.btn_one.clicked.connect(partial(num,"1"))
main_window.btn_two.clicked.connect(partial(num,"2"))
main_window.btn_three.clicked.connect(partial(num,"3"))
main_window.btn_four.clicked.connect(partial(num,"4"))
main_window.btn_five.clicked.connect(partial(num,"5"))
main_window.btn_six.clicked.connect(partial(num,"6"))
main_window.btn_seven.clicked.connect(partial(num,"7"))
main_window.btn_eight.clicked.connect(partial(num,"8"))
main_window.btn_nine.clicked.connect(partial(num,"9"))

main_window.btn_decimal_point.clicked.connect(decimal_point)
main_window.btn_AC.clicked.connect(AC)
main_window.btn_change_sign.clicked.connect(change_sign)
main_window.btn_percent.clicked.connect(percent)
main_window.btn_reverse.clicked.connect(reverse)

main_window.btn_sum.clicked.connect(sum)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)

main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_sqrt.clicked.connect(sqrt)
main_window.btn_log.clicked.connect(log)

main_window.btn_equal.clicked.connect(result)

app.exec()