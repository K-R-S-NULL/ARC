class arduino_command():
    def __init__(self) -> None:
        pass
    def get_ident(self) -> str:
        raise NotImplementedError("Please Implement method: get_ident")
    def get_Command(self) -> str:
        raise NotImplementedError("Please Implement method: get_Command")
    def get_Message(self) -> str:
        return self.get_ident() + ";" + self.get_Command()+"\n"