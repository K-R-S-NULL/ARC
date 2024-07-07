from typing import List

from .ARC_Action import *
from .ARC_Action_utils import *

class Commander():
    def __init__(self)->None:
        pass
class Workspace():
    def __init__(self)->None:
        self.__mm_tool_diameter : float = 4.0
        self.__mm_dim_x : floar = 500.0
        self.__mm_dim_x : floar = 100.0
        self.__piece : Workpiece = Workpiece()
        pass
class Workpiece():
    def __init__(self)->None:
        self.__mm_dim_x : float = 0.0
        self.__mm_dim_y : float = 0.0
        self.__mm_pos_x : float = 0.0
        self.__mm_pos_y : float = 0.0
        pass