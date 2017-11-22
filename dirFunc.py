#----------------------------------------------
# DirFunc
# una lista de funciones con su tipo, direccion y lsta de variables
#----------------------------------------------


class DirFunc:
    def __init__(self):
        self.functions = []


class Func:
    def __init__(self, id, type, dir):
        self.type = type
        self.id = id
        self.type = type
        self.dir = dir
        self.globDir = None
        self.varTable = []

    def __str__(self):
        res = str(self.id)
        res += " " + str(self.type)
        res += " " + str(self.dir)
        return res

class Var:
    def __init__(self, id, type, dir):
        self.id = id
        self.type = type
        self.dir = dir
        self.dim = []

    def __str__(self):
        res = str(self.id)
        res += " " + str(self.type)
        res += " " + str(self.dir)
        #res += " " + str(self.dim)
        return res

class DimNode:
    def __init__(self, d, m):
        self.d
        self.m
        self.nextNode
