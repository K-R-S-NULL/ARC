from typing import List
#from PyQt5.QtCore import QObject, QThread
from arc.arc_commander import *
from arc.arc_cmd_move import *
from arc.arc_svg import arc_svg_builder

class arc_control():
    def __init__(self) -> None:
        self.cmd_list : arc_cmd_list = arc_cmd_list()
        pass
    def arc_cmd_list_add(self, command:arc_cmd) -> None:
        self.cmd_list.add(command)
        pass
    def arc_cmd_list_reset(self) -> None:
        self.cmd_list.reset()
        pass
    def arc_cmd_list_delete(self, index:int) -> None:
        self.cmd_list.delete(index)
        pass
    def arc_cmd_list_moveUp(self, index:int) -> None:
        self.cmd_list.moveUp(index)
        pass
    def arc_cmd_list_moveDown(self, index:int) -> None:
        self.cmd_list.moveDown(index)
        pass
    def get_svg_representation(self) -> str:
        svg = arc_svg_builder()
        svg.set_cmd_list(self.cmd_list)
        return svg.getString()
    def test(self) -> None:
        print('testtest')