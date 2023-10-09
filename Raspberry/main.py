# This Python file uses the following encoding: utf-8
import sys
import os
import i_arduino_xyz

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

def movement_straight(x,y):
    return "G00;X"+str(int(x))+";Y"+str(int(y))+";"

class arc(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

    def pattern_actions_list_add(self, action):
        rtnD = QListWidgetItem(self.pat_actions_listWidget)
        rtnD.setText(action)

    def btn_act_pattern_action_list_move_up(self):
        print("up")

    def btn_act_pattern_action_list_move_down(self):
        print("down")

    def btn_act_pattern_action_list_remove(self):
        print("remove")

    def btn_act_pattern_action_list_execute(self):
        print("go")

    def btn_act_pattern_straight_xy(self):
        x = self.pat_str_offset_x_doubleSpinBox.value()
        y = self.pat_str_offset_y_doubleSpinBox.value()
        self.pattern_actions_list_add(movement_straight(x*1000,y*1000))

    def init_listeners(self):
        print("go")
        self.pat_str_offset_pushButton.clicked.connect(self.btn_act_pattern_straight_xy)
        self.pat_actions_down_pushButton.clicked.connect(self.btn_act_pattern_action_list_move_down)
        self.pat_actions_up_pushButton.clicked.connect(self.btn_act_pattern_action_list_move_up)
        self.pat_actions_go_pushButton.clicked.connect(self.btn_act_pattern_action_list_execute)
        self.pat_actions_remove_pushButton.clicked.connect(self.btn_act_pattern_action_list_remove)

    def init_serial_communications(self):
        print("init serial communications")

        '''
    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "main.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()
        print("nogo")
        self.pat_str_offset_pushButton.clicked.connect(self.test)
'''

if __name__ == "__main__":
    app = QApplication([])
    widget = arc()
    widget.show()
    widget.init_listeners ()
    widget.init_serial_communications()
    sys.exit(app.exec_())
