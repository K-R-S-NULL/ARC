from typing import List

import arc_cmd.arc_cmd
import arc_cmd.arc_cmd_move

class arc_control():
    def __init__(self) -> None:
        self.arc_cmd_list: List[arc_cmd.arc_cmd.arc_cmd] = []
        pass
    def arc_cmd_list_add(self, command:arc_cmd) -> None:
        self.arc_cmd_list.append(command)
        pass
    def arc_cmd_list_reset(self) -> None:
        self.arc_cmd_list.clear()
        pass
    def arc_cmd_list_delete(self, index:int) -> None:
        if(len(self.arc_cmd_list)>0):
            self.arc_cmd_list.pop(index)
        pass
    def arc_cmd_list_moveUp(self, index:int) -> None:
        if(index > 0):
            self.arc_cmd_list.insert(index-1, self.arc_cmd_list.pop(index))
        pass
    def arc_cmd_list_moveDown(self, index:int) -> None:
        if(len(self.arc_cmd_list)>index):
            self.arc_cmd_list.insert(index+1, self.arc_cmd_list.pop(index))
        pass
    def arc_cmd_list_getAs_representation_list(self) -> []:
        rtn = []
        for cmd in self.arc_cmd_list:
            rtn.append(cmd.get_representation_list_item())
        return rtn
    def build_svg(self) -> str:
        for x in self.arc_cmd_list:
            print(x.get_representation_list_item())
        pass