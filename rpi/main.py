#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from threading import Thread
from rotartEncoder import RotaryEncoder
#from gui import MainGUI


def gui():
    #gui = MainGUI()
    print("sleep 5")
    sleep(5)
    print("gui")
    #gui.show()
    print("GUI")

def rotartyInput_Left():
    while(True):
        rt = RotaryEncoder(1,2,3)
        rt.selfPrint()
        sleep(20)
def rotartyInput_Right():
    while(True):
        rt = RotaryEncoder(4,5,6)
        rt.selfPrint()
        sleep(22)
def rotartyInput_Main():
    while(True):
        rt = RotaryEncoder(9,8,10)
        rt.selfPrint()
        sleep(24)

thread_gui = Thread(target=gui)
thread_gui.start()
thread_rt_l = Thread(target=rotartyInput_Left)
thread_rt_l.start()
thread_rt_r = Thread(target=rotartyInput_Right)
thread_rt_r.start()
thread_rt_m = Thread(target=rotartyInput_Main)
thread_rt_m.start()