from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QPainter, QTransform

from arc.arc_cmd_move import arc_cmd_move_str_offset_xy, default_test_circle
from arc.arc_commander import arc_cmd

import arc_controller

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
        image = QtGui.QImage.fromData(self.controller.get_svg_representation().encode())#.scaled(400,400,Qt.KeepAspectRatio)
        scene = QGraphicsScene()
        self.mov_actions_preview_graphicsView.setScene(scene)
        pic = QGraphicsPixmapItem()#transpose(method=Image.FLIP_TOP_BOTTOM)
        pic.setPixmap(QPixmap.fromImage(image))
        scene.setSceneRect(0, 0, 400, 400)
        scene.addItem(pic)
        '''paint = QPainter()
        paint.
        paint.scale(400,400)
        scene.render(paint)
        
        '''
        pass
    
    def movements_actions_list_add(self, command:arc_cmd):
        self.controller.arc_cmd_list_add(command)
        rtnD = QListWidgetItem(self.mov_actions_listWidget)
        rtnD.setText(command.get_representation_list_item())
        self.movements_preview_update()
        pass

    def btn_act_movements_action_list_move_up(self):
        currentRow = self.mov_actions_listWidget.currentRow()
        self.controller.arc_cmd_list_moveUp(currentRow)
        currentItem = self.mov_actions_listWidget.takeItem(currentRow)
        self.mov_actions_listWidget.insertItem(currentRow - 1, currentItem)
        self.mov_actions_listWidget.setCurrentItem(currentItem)
        self.movements_preview_update()
        pass

    def btn_act_movements_action_list_move_down(self):
        currentRow = self.mov_actions_listWidget.currentRow()
        self.controller.arc_cmd_list_moveDown(currentRow)
        currentItem = self.mov_actions_listWidget.takeItem(currentRow)
        self.mov_actions_listWidget.insertItem(currentRow + 1, currentItem)
        self.mov_actions_listWidget.setCurrentItem(currentItem)
        self.movements_preview_update()
        pass

    def btn_act_movements_action_list_remove(self):
        currentRow = self.mov_actions_listWidget.currentRow()
        self.controller.arc_cmd_list_delete(currentRow)
        self.mov_actions_listWidget.takeItem(currentRow)
        self.movements_preview_update()
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
        command = arc_cmd_move_str_offset_xy()
        command.setOffset(int(x),int(y))
        self.movements_actions_list_add(command)
    
    def btn_act_movements_test(self):
        self.controller.test()
        circle = default_test_circle()
        self.movements_actions_list_add(circle)
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
        self.mov_tab_test_pushButton.clicked.connect(self.btn_act_movements_test)
        #mov_actions_preview_graphicsView
        #Patttern
        #GCode
        pass
    
    def init_view(self):
        self.init_listeners()
        pass
    def init_model(self):
        pass