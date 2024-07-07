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
        self.id = None
        self.start_x   : int = 0
        self.start_y   : int = 0
        self.end_x     : int = 0
        self.end_y     : int = 0
        self.box_x     : int = 0
        self.box_y     : int = 0
        self.box_dim_x : int = 0
        self.box_dim_y : int = 0
        self.tool_diameter : int = 1
        self.stroke_color : str = 'blue'
        pass
    def buid_node(self) -> minidom.Element:
        raise NotImplementedError("Implement method: get_string for arc_svg_element children")
    def set_id(self,id) -> None:
        self.id = id
        pass
class arc_svg():
    def __init__(self) -> None:
        self.svg_dimension_x : int = 100
        self.svg_dimension_y : int = 100
        self.svg_box_list : List[arc_svg_element] = []
        self.min_box_x : int = 0
        self.min_box_y : int = 0
        self.max_abs_dim_x : int = 0
        self.max_abs_dim_y : int = 0
        pass
    def append(self, element:arc_svg_element) -> None:
        e_abs_box_dim_x : int = element.box_x + element.box_dim_x
        e_abs_box_dim_y : int = element.box_y + element.box_dim_y
        if e_abs_box_dim_x > self.max_abs_dim_x: self.max_abs_dim_x = e_abs_box_dim_x
        if e_abs_box_dim_y > self.max_abs_dim_y: self.max_abs_dim_y = e_abs_box_dim_y
        if self.min_box_x > element.box_x: self.min_box_x = element.box_x
        if self.min_box_y > element.box_y: self.min_box_y = element.box_y
        self.svg_dimension_x = self.max_abs_dim_x - self.min_box_x
        self.svg_dimension_y = self.max_abs_dim_y - self.min_box_y
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
        self.svg.setAttribute('width', '400') #str(self.svg_dimension_x * self.scaling_factor))
        self.svg.setAttribute('height', '400') #str(self.svg_dimension_y * self.scaling_factor))
        tmpx = self.min_box_x
        if self.min_box_x < 0 : tmpx = self.min_box_x * -1
        tmpy = self.min_box_y
        if self.min_box_y < 0 : tmpy = self.min_box_y * -1
        self.svg.setAttribute('viewBox',str(self.min_box_x)+' '+str(self.min_box_y) + ' '+str((self.max_abs_dim_x+tmpx))+' '+str((self.max_abs_dim_y+tmpy )))
        self.svg.setAttribute('preserveAspectRatio','xMaxYMin meet')
        self.svg.setAttribute('xmlns','http://www.w3.org/2000/svg')
        self.svg.setAttribute('xmlns:xlink','http://www.w3.org/1999/xlink')
        self.svg.setAttribute('style','background-color:green')
        for box in self.svg_box_list:
            boxplot = arc_svg_element_boxplot()
            boxplot.loadElement(box)
            self.svg.appendChild(boxplot.buid_my_node(self.root))
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
        self.abs_box_dim_x : int = 0
        self.abs_box_dim_y : int = 0
        pass
    def append(self, element:arc_svg_element) -> None:
        if len(self.svg_elements) == 0:
            self.start_x   = element.start_x
            self.start_y   = element.start_y
            self.box_x     = element.box_x
            self.box_y     = element.box_y
            self.box_dim_x = element.box_dim_x
            self.box_dim_y = element.box_dim_y
            self.abs_box_dim_x  = self.box_x + self.box_dim_x
            self.abs_box_dim_y  = self.box_y + self.box_dim_y
            self.end_x     = element.end_x
            self.end_y     = element.end_y
        else:
            self.end_x     = element.end_x
            self.end_y     = element.end_y
        e_abs_box_dim_x : int = element.box_x + element.box_dim_x
        e_abs_box_dim_y : int = element.box_y + element.box_dim_y
        if e_abs_box_dim_x > self.abs_box_dim_x: self.abs_box_dim_x = e_abs_box_dim_x
        if e_abs_box_dim_y > self.abs_box_dim_y: self.abs_box_dim_y = e_abs_box_dim_y
        if self.box_x > element.box_x: self.box_x = element.box_x
        if self.box_y > element.box_y: self.box_y = element.box_y
        self.box_dim_x = self.abs_box_dim_x - self.box_x
        self.box_dim_y = self.abs_box_dim_y - self.box_y
        self.svg_elements.append(element)
        pass
    def buid_my_node(self,root:minidom.Document) -> minidom.Element:
        rtn = root.createElement('g')
        rtn.setAttribute('opacity','0.8')
        if self.id is not None:
            rtn.setAttribute('id',str(self.id))
        for element in self.svg_elements:
            rtn.appendChild(element.buid_my_node(root))
        return rtn

class arc_svg_line(arc_svg_element):
    def __init__(self) -> None:
        super().__init__()
        pass
    def setAttrbutes(self,start_x:int,start_y:int,end_x:int,end_y:int)->None:
        if end_x < 0:
            self.box_x = start_x+end_x
            self.box_dim_x = end_x * (-1)
            self.start_x = self.box_dim_x
            self.end_x = 0
        else:
            self.box_x = start_x
            self.box_dim_x = end_x
            self.start_x = 0
            self.end_x = self.box_dim_x
        if end_y < 0:
            self.box_y = start_y + end_y
            self.box_dim_y = end_y * (-1)
            self.start_y = self.box_dim_y
            self.end_y = 0
        else:
            self.box_y = start_y
            self.box_dim_y = end_y
            self.start_y = 0
            self.end_y = self.box_dim_y
        pass
    def buid_my_node(self,root:minidom.Document) -> minidom.Element:
        rtn = root.createElement('line')
        rtn.setAttribute('x1',str((self.box_x + self.start_x)))
        rtn.setAttribute('y1',str((self.box_y + self.start_y)))
        rtn.setAttribute('x2',str((self.box_x + self.end_x)))
        rtn.setAttribute('y2',str((self.box_y + self.end_y)))
        rtn.setAttribute('stroke',self.stroke_color)
        rtn.setAttribute('stroke-width',str(self.tool_diameter))
        return rtn
class arc_svg_rect(arc_svg_element):
    def __init__(self) -> None:
        super().__init__()
        pass
    def buid_my_node(self,root:minidom.Document) -> minidom.Element:
        rtn = root.createElement('rect')
        rtn.setAttribute('x',str(self.box_x))
        rtn.setAttribute('y',str(self.box_y))
        rtn.setAttribute('width', str(self.box_dim_x))
        rtn.setAttribute('height',str(self.box_dim_y))
        style : str = 'fill:blue;'
        style += 'stroke:'+self.stroke_color+';'
        style += 'stroke-width:'+str(self.tool_diameter)+';'
        style += 'fill-opacity:0;'
        style += 'stroke-opacity:0.9'
        rtn.setAttribute('style',
         )
        return rtn
class arc_svg_element_boxplot(arc_svg_rect):
    def __init__(self) -> None:
        super().__init__()
        pass
    def loadElement(self,element:arc_svg_element) -> None:
        self.box_x = element.box_x
        self.box_y = element.box_y
        self.box_dim_x = element.box_dim_x
        self.box_dim_y = element.box_dim_y
        self.stroke_color = 'red'
        self.tool_diameter = 2