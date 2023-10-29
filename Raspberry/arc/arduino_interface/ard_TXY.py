from arc.arduino_interface.ard_cmd import arduino_command
class arduino_xy_command(arduino_command):
    def __init__(self) -> None:
        super().__init__()
        self.ident = "TXY"
        pass
    def get_ident(self) -> str:
        return self.ident
#command to trigger an initialisation
class arduino_xy_init(arduino_xy_command):
    def __init__(self) -> None:
        super().__init__()
        pass
#command to make the table move to relative x and y coordinates as fast as posible
class arduino_xy_rapidMove(arduino_xy_command):
    def __init__(self) -> None:
        super().__init__()
        self.x = int(0)
        self.y = int(0)
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
        self.x = int(0)
        self.y = int(0)
        self.speed = float(0.0)
    def setattr(self, x:int, y:int, speed:float) -> None:
        self.x = x
        self.y = y
        self.speed = speed
    def get_Command(self) -> str:
        return "G01;X"+str(self.x)+";Y"+str(self.y)+";F"+str(self.speed)+";"
