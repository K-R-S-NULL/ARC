#from arc.arc_commander import 
from arc.arc_commander import arc_cmd
from arc.arc_svg import arc_svg_element
from arc.arc_svg import arc_svg_line
from arc.arc_svg import arc_svg_group
from arc.arduino_interface.ard_TXY import *
'''
##########################

##########################
'''
class arc_cmd_move(arc_cmd):
    def __init__(self) -> None:
        super().__init__()

        pass


class arc_cmd_move_str_offset_xy(arc_cmd_move):
    def __init__(self) -> None:
        super().__init__()
        pass
    def setOffset(self, x:int, y:int)-> None:
        self.end_x = x
        self.end_y = y
        self.arduino_cmd.clear()
        arduino_cmd = arduino_xy_rapidMove()
        arduino_cmd.setattr(x,y)
        self.arduino_cmd.append(arduino_cmd)
        pass
    def get_representation_list_item(self) -> str:
        return self.arduino_cmd[0].get_ident() + ";" + self.arduino_cmd[0].get_Command()
    def get_representation_svg_part(self, start_x :int, start_y:int) -> arc_svg_element:
        group = arc_svg_group()
        group.set_id('G00')
        line = arc_svg_line()
        line.setAttrbutes(start_x,start_y,self.end_x,self.end_y)
        group.append(line)
        return group
    def get_offset_x(self) -> int:
        return self.end_x
    def get_offset_y(self) -> int:
        return self.end_y


class arc_cmd_move_str_angle(arc_cmd_move):
    def __init__(self) -> None:
        super().__init__()
        pass
    def get_representation_list_item(self) -> arc_svg_element:
        pass