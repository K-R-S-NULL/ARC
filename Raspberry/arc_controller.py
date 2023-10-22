import arc_cmd.arc_cmd
import arc_cmd.arc_cmd_move

class arc_control():
    def __init__(self) -> None:
        self.arc_cmd_list = []
        pass
    def add_command(self, command:arc_cmd) -> None:
        self.arc_cmd_list.append(command)
        pass
    def build_svg(self) -> str:
        pass