from arc_cmd.arduino_interface import *

class arc_cmd():
    def __init__(self) -> None:
        self.arduino_cmd = []
        pass
    def get_All_arduino_commands(self) -> list:
        return self.arduino_cmd
    def get_representation_list_item(self) -> str:
        raise NotImplementedError("Implement method: get_representation_list_item")
    def get_representation_svg_part(self) -> str:
        raise NotImplementedError("Implement method: get_representation_svg_part")