import sys
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QThread

from arc.arduino_interface.ard_cmd import arduino_command
class arduino_serial_usb_handler():
    commandList : List[arduino_command] = []
    def add_command(self, cmd: arduino_command)->None:
        self.commandList.append(cmd)
    def set_commandList(self, ncmdlist:List[arduino_command])->None:
        self.commandList = ncmdlist
    def work_cmd_list(slef)->None:
        for ardc in self.commandList:
            print(ardc.get_Message())
class worker_usb_serial_cmd_snd(QObject):
    finished = QtCore.pyqtSignal()
    snd_status = QtCore.pyqtSignal(int,str)
    def run(self):
        pass

class worker_usb_serial_cmd_rcv(QObject):
    def __init__(self) -> None:
        pass
    def run(self):
        pass