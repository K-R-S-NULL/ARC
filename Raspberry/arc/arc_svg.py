from typing import List
import xml.etree.ElementTree as ET

from xml.dom import minidom 
from xml.dom.minidom import *

from arc.arc_commander import *
#from arc.arc_commander import arc_cmd

class arc_svg_builder():
    def __init__(self) -> None:
        self.dimension_x : int = 0
        self.dimension_y : int = 0
        self.cmd_list: List[arc_cmd] = []
        self.svg = arc_svg()
        pass
    def set_cmd_list(self, cmdlist)->None:
        self.cmd_list = cmdlist.getList()
        pass
    def build(self)-> None:
        self.svg = arc_svg()
        start_off_x : int = 0
        start_off_y : int = 0
        self.last_end_x : int = 0
        self.last_end_y : int = 0
        for cmd in self.cmd_list:
            nsvg = cmd.get_representation_svg_part(self.last_end_x,self.last_end_y)
            self.svg.append(nsvg)
            self.last_end_x = nsvg.box_x + nsvg.end_x
            self.last_end_y = nsvg.box_y + nsvg.end_y
            #print(nsvg.)
            print('last x:'+str(self.last_end_x)+' y:'+str(self.last_end_y))
        self.svg.build()
        pass
    def getString(self)->str:
        self.build()
        return self.svg.toString()
class arc_svg_element():
    def __init__(self) -> None:
        self.start_x   : int = 0
        self.start_y   : int = 0
        self.end_x     : int = 0
        self.end_y     : int = 0
        self.box_x     : int = 0
        self.box_y     : int = 0
        self.box_dim_x : int = 0
        self.box_dim_y : int = 0
        pass
    def buid_node(self) -> minidom.Element:
        raise NotImplementedError("Implement method: get_string for arc_svg_element children") 
class arc_svg():
    def __init__(self) -> None:
        self.svg_dimension_x : int = 10000
        self.svg_dimension_y : int = 10000
        self.svg_box_list : List[arc_svg_element] = []
        pass
    def append(self, element:arc_svg_element) -> None:
        self.svg_box_list.append(element)
        pass
    def clear(self)->None:
        self.svg_box_list : List[arc_svg_element] = []
        pass
    def build(self) -> None:
        #svg = ET.Element('svg')
        #svg.set('')

        self.root = minidom.Document()
        self.svg = self.root.createElement('svg')
        self.svg.setAttribute('width',  str(self.svg_dimension_x))
        self.svg.setAttribute('height', str(self.svg_dimension_y))
        self.svg.setAttribute('viewBox','0 0 '+str(self.svg_dimension_x)+' '+str(self.svg_dimension_y))
        self.svg.setAttribute('xmlns','http://www.w3.org/2000/svg')
        self.svg.setAttribute('xmlns:xlink','http://www.w3.org/1999/xlink')
        for box in self.svg_box_list:
            self.svg.appendChild(box.buid_my_node(self.root))
        self.root.appendChild(self.svg)
        #print(self.root.toprettyxml())
        pass
    def toString(self) -> str:
        print(str(self.root.toprettyxml()))
        return str(self.root.toprettyxml())


class arc_svg_group(arc_svg_element):
    def __init__(self) -> None:
        super().__init__()
        self.svg_elements : List[arc_svg_element]=[]
        pass
    def append(self, element:arc_svg_element) -> None:
        self.svg_elements.append(element)
        pass
    def buid_my_node(self,root:minidom.Document) -> minidom.Element:
        rtn = root.createElement('g')
        rtn.setAttribute('opacity','0.8')
        for element in self.svg_elements:
             rtn.appendChild(element.buid_my_node(root))
        return rtn

class arc_svg_line(arc_svg_element):
    def __init__(self) -> None:
        super().__init__()
        pass
    def setAttrbutes(self,start_x:int,start_y:int,end_x:int,end_y:int)->None:
        if end_x < 0:
            self.box_x = start_x-end_x
            self.box_dim_x = end_x * (-1)
        else:
            self.box_x = start_x
            self.box_dim_x = end_x
        self.start_x = self.box_x -start_x
        self.end_x = end_x
        if end_y < 0:
            self.box_y = start_y - end_y
            self.box_dim_y = end_y * (-1)
        else:
            self.box_y = start_y
            self.box_dim_y = end_y
        self.start_y = self.box_y -start_y
        self.end_y = end_y
        pass
    def buid_my_node(self,root:minidom.Document) -> minidom.Element:
        rtn = root.createElement('line')
        rtn.setAttribute('x1',str((self.box_x + self.start_x)))
        rtn.setAttribute('y1',str((self.box_y + self.start_y)))
        rtn.setAttribute('x2',str((self.box_x + self.end_x)))
        rtn.setAttribute('y2',str((self.box_y + self.end_y)))
        rtn.setAttribute('stroke','blue')
        rtn.setAttribute('stroke-width','3')
        return rtn