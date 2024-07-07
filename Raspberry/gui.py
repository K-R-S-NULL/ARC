from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDoubleSpinBox, QListWidget,QListWidgetItem
import sys
import serial
import time
serial1 = serial.Serial('/dev/ttyUSB1',115200, timeout=1.0)
time.sleep(3)#arduino bootup time
serial1.reset_input_buffer()


def clickMethod():
    x = input_x.value()
    y = input_y.value()
    command = "G00;X"+str(x)+";Y"+str(y)+";"
    cmdD = QListWidgetItem(returnData)
    cmdD.setText("cmd:"+command)
    command += '\n'
    serial1.write(bytes(command.encode()))
    time.sleep(4)
    notdone = True
    line = ""
    while(line==""):
        if(serial1.in_waiting > 0):
            line = serial1.readline().decode('utf-8').rstrip()
        if(line.endswith(";")):
            notdone = False

    rtnD = QListWidgetItem(returnData)
    rtnD.setText("ans:"+line)

app = QApplication([])
win = QMainWindow()
win.setWindowTitle("Test")
win.resize(550,480)
win.move(100,200)

label_x = QLabel("X:", win)
label_x.move(20,0)

input_x = QDoubleSpinBox(win)
input_x.move(40,0)
input_x.setSingleStep(1000)
input_x.setMaximum(100000000.0)
input_x.setMinimum(-100000000.0)

label_y = QLabel("Y:", win)
label_y.move(20,40)

input_y = QDoubleSpinBox(win)
input_y.move(40,40)
input_y.setSingleStep(1000.0)
input_y.setMaximum(100000000.0)
input_y.setMinimum(-100000000.0)

button = QPushButton("Click here - - ", win)
button.move(20,80)
button.clicked.connect(clickMethod)

returnData = QListWidget(win)
returnData.move(20,120)
returnData.setMinimumHeight(300)
returnData.setMinimumWidth(500)

win.show()

sys.exit(app.exec_())