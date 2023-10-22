from arc_cmd.arduino_interface.ard_cmd import arduino_command

class arduino_error(arduino_command):
    def __init__(self) -> None:
        super().__init__()
        ident = "ERR"
        code = "00"
        message = "basic"
        pass
    def get_ident(self) -> str:
        return str(self.ident)
    def setattr(self, code:str, message:str) -> None:
        self.code = code
        self.message = message
        pass
    def get_Command(self) -> str:
        return "C"+str(self.code)+";M"+str(self.message)+";"