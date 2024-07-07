#from arc.arc_commander import 
import math
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
        return self.arduino_cmd[0].get_ident() + ";" + 'line x:' + str(self.end_x) + 'mm y:'+ str(self.end_y) + 'mm'
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

class default_test_circle(arc_cmd_move):
    def __init__(self) -> None:
        super().__init__()
        pass
    def get_representation_list_item(self) -> str:
        return 'Test Circle'
    def get_representation_svg_part(self, start_x :int, start_y:int) -> arc_svg_element:
        self.start_x = start_x
        self.start_y = start_y
        arc_len : float = 1.0
        radius : float = 100.0
        self.end_x = radius
        self.end_y = 0
        center_x :float=float(start_x)
        center_y :float=float(start_y+radius)
        umfang : float = 2 * radius * math.pi
        group = arc_svg_group()
        
        group.set_id('TEST-CIRCLE')
        last_x : float = center_x + radius * math.sin(0) # sin(0)
        last_y : float = center_y + radius * math.cos(0) # cos(0)
        total_steps = int(umfang/arc_len)
        a=(1/total_steps)*(math.pi*2)
        print(a)
        for i in range(1, total_steps+1):
            total_x : float = center_x + radius * math.sin(a*i)
            total_y : float = center_y + radius * math.cos(a*i)
            #print(str(last_x)+ ' '+str(last_y))
            line = arc_svg_line()
            line.setAttrbutes(last_x,last_y,total_x-last_x,total_y-last_y)
            last_x = total_x
            last_y = total_y
            group.append(line)
        return group