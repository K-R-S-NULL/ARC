import RPi.GPIO as GPIO
"""
Rotary Encoder with Switch
CLK ▁▁██▁▁██▁▁██▁▁██▁▁██▁▁██
DT  ▁██▁▁██▁▁██▁▁██▁▁██▁▁██▁
    123412341234123412341234
  <1> 00
  <2> 01
  <3> 11
  <4> 10
    Clockwise
CLK 001100110011001100110011
DT  011001100110011001100110
    <1> --> <2> --> <3> --> <4> --> <1>
    Counter-Clockwise
CLK 110110011011001101100110
DT  011001100110011001100110
    <4> --> <3> --> <2> --> <1> --> <4>
"""
class RotaryEncoder:
    pinCLK = 3
    pinDT = 4
    pinSW = 5

    def __init__(self,pinCLK,pinDT,pinSW,callback=None):
        self.pinCLK = pinCLK
        self.pinDT = pinDT
        self.pinSW = pinSW
        self.callback = callback
        self.value = 0
        self.state = '00'
        self.direction = 0
        self.switchchange = 0
        GPIO.setup(self.pinCLK, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinDT, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pinSW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        clk = GPIO.input(self.pinCLK)
        dt = GPIO.input(self.pinDT)
        self.state = "{}{}".format(clk,dt)
        self.switch = GPIO.input(self.pinSW)
        GPIO.add_event_detect(self.pinCLK, GPIO.BOTH,callback=self.rotation)
        GPIO.add_event_detect(self.pinDT, GPIO.BOTH,callback=self.rotation)
        GPIO.add_event_detect(self.pinSW, GPIO.BOTH,callback=self.switch)
        pass
    def rotation(self,chan):
        clk = GPIO.input(self.pinCLK)
        dt = GPIO.input(self.pinDT)
        newState = "{}{}".format(clk,dt)
        if self.state == "00":      #STATE <1>
            if newState == "01":    #CW  - <2>
                self.rotationCW(chan)
                pass
            elif newState == "10":  #CCW - <4>
                self.rotationCCW(chan)
                pass
        elif self.state == "01":    #STATE <2>
            if newState == "11":    #CW  - <3>
                self.rotationCW(chan)
                pass
            elif newState == "00":  #CCW - <1>
                self.rotationCCW(chan)
                pass
        elif self.state == "11":    #STATE <3>
            if newState == "10":    #CW  - <4>
                self.rotationCW(chan)
                pass
            elif newState == "01":  #CCW - <2>
                self.rotationCCW(chan)
                pass
            pass
        elif self.state == "10":    #STATE <4>
            if newState == "00":    #CW  - <1>
                self.rotationCW(chan)
                pass
            if newState == "11":    #CCW - <3>
                self.rotationCCW(chan)
                pass
            pass
        self.state = newState
        pass
    def rotationCW(self,chan):
        self.value += 1
        self.direction = 1
        if self.callback is not None:
            self.callback()
            pass
        pass
    def rotationCCW(self,chan):
        self.value -=1
        self.direction = -1
        if self.callback is not None:
            self.callback()
            pass
        pass
    def getValue(self):
        return self.value
    def getDirection(self):
        return self.direction
    def switch(self,chan):
        switchstate = GPIO.input(self.pinSW)
        if switchstate != self.switch:
            #switch triggered
            self.switchchange =  switchstate - self.switch
            if self.callback is not None:
                self.callback()
                pass
            pass
        self.switch = switchstate
        pass
    def getSwitchChange(self):
        return self.switchchange
    def selfPrint(self) -> None:
        print(str(self.pinCLK) + " " + str(self.pinDT) + " " + str(self.pinSW))