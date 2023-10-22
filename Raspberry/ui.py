from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import i_arduino

class mainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()
        self.pattern_actions_list = []
        pass

    def movements_preview_update(self):
        #self.mov_actions_preview_graphicsView
        pass
    
    def movements_actions_list_add(self, action:i_arduino.arduino_command):
        self.pattern_actions_list.append(action)
        rtnD = QListWidgetItem(self.pat_actions_listWidget)
        rtnD.setText(action.get_Command)
        pass

    def btn_act_movements_action_list_move_up(self):
        currentRow = self.mov_actions_listWidget.currentRow()
        currentItem = self.mov_actions_listWidget.takeItem(currentRow)
        self.mov_actions_listWidget.insertItem(currentRow - 1, currentItem)
        self.mov_actions_listWidget.setCurrentItem(currentItem)
        pass

    def btn_act_movements_action_list_move_down(self):
        currentRow = self.mov_actions_listWidget.currentRow()
        currentItem = self.mov_actions_listWidget.takeItem(currentRow)
        self.mov_actions_listWidget.insertItem(currentRow + 1, currentItem)
        self.mov_actions_listWidget.setCurrentItem(currentItem)
        pass

    def btn_act_movements_action_list_remove(self):
        currentRow = self.mov_actions_listWidget.currentRow()
        currentItem = self.mov_actions_listWidget.takeItem(currentRow)
        pass

    def btn_act_movements_action_list_execute(self):
        rowPosition = self.master_com_log_tableWidget.rowCount()
        self.master_com_log_tableWidget.insertRow(rowPosition)
        self.master_com_log_tableWidget.setItem(rowPosition , 0, QTableWidgetItem("text1"))
        self.master_com_log_tableWidget.selectRow(rowPosition)
        self.master_com_log_tableWidget.clearSelection()
        pass

    def btn_act_movements_straight_xy(self):
        x = self.pat_str_offset_x_doubleSpinBox.value()
        y = self.pat_str_offset_y_doubleSpinBox.value()
        action = i_arduino.arduino_xy_rapidMove()
        action.setattr(int(x*1000),int(y*1000))
        self.movements_actions_list_add(action)
        pass

    def init_listeners(self):
        print("initializing listeners")
        #Main
        #Move
        self.mov_str_offset_pushButton.clicked.connect(self.btn_act_movements_straight_xy)
        self.mov_actions_down_pushButton.clicked.connect(self.btn_act_movements_action_list_move_down)
        self.mov_actions_up_pushButton.clicked.connect(self.btn_act_movements_action_list_move_up)
        self.mov_actions_go_pushButton.clicked.connect(self.btn_act_movements_action_list_execute)
        self.mov_actions_remove_pushButton.clicked.connect(self.btn_act_movements_action_list_remove)
        #mov_actions_preview_graphicsView
        #Patttern
        #GCode
        pass