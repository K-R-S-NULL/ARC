from typing import List
from arc.arduino_interface import ard_cmd
from arc.arc_svg import arc_svg_element
#from arc.arduino_interface import *

class arc_cmd():
    def __init__(self) -> None:
        self.arduino_cmd: List[ard_cmd.arduino_command] = []
        self.start_x : int = 0
        self.start_y : int = 0
        self.end_x : int = 0
        self.end_y : int = 0
        self.dimension_x : int = 0
        self.dimension_y : int = 0
        pass
    def get_All_arduino_commands(self) -> List[ard_cmd.arduino_command]:
        return self.arduino_cmd
    def get_representation_list_item(self) -> str:
        raise NotImplementedError("Implement method: get_representation_list_item")
    def get_representation_svg_part(self, start_x :int, start_y:int) -> arc_svg_element:
        raise NotImplementedError("Implement method: get_representation_svg_part")
    def get_offset_x(self) -> int:
        raise NotImplementedError("Implement method: ")
    def get_offset_y(self) -> int:
        raise NotImplementedError("Implement method: ")

class arc_cmd_list():
    def __init__(self) -> None:
        self.arc_cmd_list: List[arc_cmd] = []
        pass
    def add(self, cmd:arc_cmd) -> None:
        self.arc_cmd_list.append(cmd)
        pass
    def reset(self) -> None:
        self.arc_cmd_list.clear()
        pass
    def delete(self, index:int) -> None:
        if(len(self.arc_cmd_list)>0):
            self.arc_cmd_list.pop(index)
        pass
    def moveUp(self, index:int) -> None:
        if(len(self.arc_cmd_list)>0):
            if(index > 0):
                self.arc_cmd_list.insert(index-1, self.arc_cmd_list.pop(index))
        pass
    def moveDown(self, index:int) -> None:
        if(len(self.arc_cmd_list)>0):
            if(len(self.arc_cmd_list)>index):
                self.arc_cmd_list.insert(index+1, self.arc_cmd_list.pop(index))
        pass
    def getList(self) -> List[arc_cmd]:
        return self.arc_cmd_list
