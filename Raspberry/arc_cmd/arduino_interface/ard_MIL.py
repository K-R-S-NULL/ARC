from arc_cmd.arduino_interface.ard_cmd import arduino_command

class arduino_mill_command(arduino_command):
    def __init__(self) -> None:
        super().__init__()
        ident = "MIL"
        pass
    def get_ident(self) -> str:
        return str(self.ident)

class arduino_mill_init(arduino_mill_command):
    def __init__(self) -> None:
        super().__init__()
        pass