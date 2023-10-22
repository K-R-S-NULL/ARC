from typing import Any


'''
######################
   abstract command
######################
'''
class arduino_command():
    def __init__(self) -> None:
        pass
    def get_ident(self) -> str:
        raise NotImplementedError("Please Implement method: get_ident")
    def get_Command(self) -> str:
        raise NotImplementedError("Please Implement method: get_Command")
    def get_Message(self) -> str:
        return self.get_ident + ";" + self.get_Command+"\n"
'''
######################
General Error Message
    (modifiable)
######################
'''
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
'''
######################
    X-Y Table
######################
'''
class arduino_xy_command(arduino_command):
    def __init__(self) -> None:
        super().__init__()
        ident = "TXY"
        pass
    def get_ident(self) -> str:
        return str(self.ident)
#command to trigger an initialisation
class arduino_xy_init(arduino_xy_command):
    def __init__(self) -> None:
        super().__init__()
        pass
#command to make the table move to relative x and y coordinates as fast as posible
class arduino_xy_rapidMove(arduino_xy_command):
    def __init__(self) -> None:
        super().__init__()
        x = int(0)
        y = int(0)
        pass
    def setattr(self, x:int , y:int) -> None:
        self.x = x
        self.y = y
        pass
    def get_Command(self) -> str:
        return "G00;X"+str(self.x)+";Y"+str(self.y)+";"
#command to make the table move to relative x and y coordinates with given speed
class arduino_xy_straightMove(arduino_xy_command):
    def __init__(self) -> None:
        super().__init__()
        x = int(0)
        y = int(0)
        speed = float(0.0)
    def setattr(self, x:int, y:int, speed:float) -> None:
        self.x = x
        self.y = y
        self.speed = speed
    def get_Command(self) -> str:
        return "G01;X"+str(self.x)+";Y"+str(self.y)+";F"+str(self.speed)+";"

'''
######################
Mill speed Control
######################
'''
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