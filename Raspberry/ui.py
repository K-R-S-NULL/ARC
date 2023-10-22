from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import i_arduino

import arc_controller
from arc_cmd.arc_cmd import *
from arc_cmd.arc_cmd_move import *

class mainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.controller = arc_controller.arc_control()
        self.pattern_actions_list = []
        self.init_model()
        self.init_view()

        self.show()
        pass

    def movements_preview_update(self):
        #self.mov_actions_preview_graphicsView
        pass
    
    def movements_actions_list_add(self, command:arc_cmd):
        self.controller.add_command(command)
        rtnD = QListWidgetItem(self.mov_actions_listWidget)
        rtnD.setText(command.get_representation_list_item())
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
        x = self.mov_str_offset_x_doubleSpinBox.value()
        y = self.mov_str_offset_y_doubleSpinBox.value()
        command = arc_cmd_move_str_offset()
        command.setOffset(int(x*1000),int(y*1000))
        self.movements_actions_list_add(command)

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
    
    def init_view(self):
        self.init_listeners()
        pass
    def init_model(self):
        pass