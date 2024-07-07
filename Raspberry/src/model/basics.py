import math
from operator import itemgetter, attrgetter
class vector():
    def __init__(self) -> None:
        self.x : float = 0.0
        self.y : float = 0.0
        self.z : float = 0.0
        pass
    def __repr__(self):
        return repr((self.x,self.y,self.z))
class element():
    def __init__(self)->None:
        self.path : List[basics.vector] = []
        self.positions : List[basics.vector] = []
        pass
    def print(self)->None:
        for i in range(0,len(self.path)-1):
            print(self.path[i])
class circle():
    def __init__(self) -> None:
        self.path : List[basics.vector] = []
        self.positions : List[basics.vector] = []
        self.arc_len : float = 1.0
        self.center : basics.vector = vector()
        self.radius : float = 1.0
        self.c_positions : List[basics.vector] = []
        pass
    def calculate(self)->None:
        self.positions.clear()
        self.path.clear()
        self.c_positions.clear()
        total_steps : int = int(self.calculate_circumference()/self.arc_len)
        a = (1/total_steps)*(math.pi*2)
        for i in range(0,total_steps+1):
            pos : basi+ics.vector = vector()
            c_pos : basics.vector = vector()
            c_pos.x = self.radius * math.sin(a*i)
            c_pos.y = self.radius * math.cos(a*i)
            pos.x = self.center.x + c_pos.x
            pos.y = self.center.y + c_pos.y
            self.c_positions.append(c_pos)
            self.positions.append(pos)
            self.path.append(pos)
        pass
    def calculate_circumference(self) -> float:
        return 2 * self.radius * math.pi
class arch(element):
    def __init__(self):
        super().__init__()
        self.start : basics.vector = vector()
        self.start.y = self.center.y + self.radius
        self.start.x = self.center.x
        self.start.z = self.center.z
        self.start_pos : int = 0
        self.end : basics.vector = vector()
        self.end.x = self.start.x
        self.end.y = self.start.y
        self.end.z = self.start.z
        self.end_pos : int = 0
        self.direction : int = 1
        pass
    def set_start(self,start:vector)->None:
        self.start = start
        self.start_pos = self.__getClosestPosition(start)
        pass
    def set_end(self,end:vector)->None:
        self.end = end
        self.end_pos = self.__getClosestPosition(end)
        pass
    def calculate_path(self)->None:
        if(len(self.path)==0):super().calculate_path()
        self.path.clear()
        self.path.append(self.start)
        s : int = self.start_pos
        for i in range(0,len(self.positions)-1):
            pos : int = self.start_pos + (i*self.direction)
            if(self.direction>0):
                if(pos>(len(self.positions)-1)):pos=pos-len(self.positions)
                pass
            else:
                if(pos<0):pos=len(self.positions)+pos
                pass
            self.path.append(self.positions[pos])
            if(self.start_pos != self.end_pos):
                if(pos==self.end_pos): break
        self.path.append(self.end)
        pass
    def __getClosestPosition(self,pos:vector)->int:
        if(len(self.path)==0):super().calculate_path()
        distance : List[basics.vector] = []
        for i in range(0,len(self.positions)-1):
            d = vector()
            d.x = self.positions[i].x - pos.x
            d.y = self.positions[i].y - pos.y
            d.z = self.positions[i].z - pos.z
            if(d.x<0):d.x=d.x*-1
            if(d.y<0):d.y=d.y*-1
            if(d.z<0):d.z=d.z*-1
            distance.append(d)
        smalles = sorted(distance,key=attrgetter('x','y','z'))
        for i in range(0,len(distance)-1):
            if(distance[i]==smalles[0]):
                return i
        return 0


center = vector()
center.x = 4.5
center.y = 4.5
c : circle = circle()
c.radius = 4.5
c.calculate_path()
c.print()
print('##########')
a :arch = arch()
a.radius = 4.5
a.center = center
a.calculate_path()
a.print()
print("#####")
va = vector()
va.x = 9.0
va.y = 4.5
vb = vector()
vb.x = 0.0
vb.y = 4.5
a.set_start(vb)
a.set_end(va)
a.calculate_path()
a.print()
print(a.start_pos)
print(a.end_pos)