from arc_cmd import *
'''
##########################

##########################
'''
class arc_cmd_move(arc_cmd.arc_cmd):
    def __init__(self) -> None:
        super().__init__()
        pass


class arc_cmd_move_str_offset(arc_cmd_move):
    def __init__(self) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        pass
    def setOffset(self, x:int, y:int)-> None:
        self.x = x
        self.y = y
        #self.arduino_cmd = [].append()
        pass
    def get_representation_list_item(self) -> str:
        return "Gxx;X"+str(self.x)+";Y"+str(self.y)+";"

class arc_cmd_move_str_angle(arc_cmd_move):
    def __init__(self) -> None:
        super().__init__()
        pass
    def get_representation_list_item(self) -> str:
        return "ARGK"