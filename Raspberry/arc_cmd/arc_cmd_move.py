from arc_cmd import *
from arc_cmd.arduino_interface.ard_TXY import *
'''
##########################

##########################
'''
class arc_cmd_move(arc_cmd.arc_cmd):
    def __init__(self) -> None:
        super().__init__()
        pass


class arc_cmd_move_str_offset_xy(arc_cmd_move):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        pass
    def setOffset(self, x:int, y:int)-> None:
        self.x = x
        self.y = y
        self.arduino_cmd.clear()
        arduino_cmd = arduino_xy_rapidMove()
        arduino_cmd.setattr(x,y)
        self.arduino_cmd.append(arduino_cmd)
        pass
    def get_representation_list_item(self) -> str:
        return self.arduino_cmd[0].get_ident() + ";" + self.arduino_cmd[0].get_Command()

class arc_cmd_move_str_angle(arc_cmd_move):
    def __init__(self) -> None:
        super().__init__()
        pass
    def get_representation_list_item(self) -> str:
        return "ARGK"