#------------------------------------------------------------------------------
# memoriaVirtual.py
# es un objeto que maneja la memoria de la maquina virtual
# cuenta con las funciones getValue(), setValue(), getType()
#------------------------------------------------------------------------------


from dirFunc import *
from cuadruplo import *

class memoriaVirtual():
    def __init__(self):
        self.memGlobal = memoriaFuncion(1000,1200,1400,1600)
        self.memLocal = memoriaFuncion(2000,3000,4000,5000)
        self.memTemporal = memoriaFuncion(6000,7000,8000,9000)
        self.memConst = memoriaFuncion(0,200,400,600)

    def printMemoria(self):
        print('Constantes')
        if self.memConst.varInt:
            print('int:')
            print(self.memConst.varInt)
        if self.memConst.varFloat:
            print('float:')
            print(self.memConst.varFloat)
        if self.memConst.varBool:
            print('bool:')
            print(self.memConst.varBool)
        if self.memConst.varChar:
            print('char:')
            print(self.memConst.varChar)
        print('Variables Globales')
        if self.memGlobal.varInt:
            print('int:')
            print(self.memGlobal.varInt)
        if self.memGlobal.varFloat:
            print('float:')
            print(self.memGlobal.varFloat)
        if self.memGlobal.varBool:
            print('bool:')
            print(self.memGlobal.varBool)
        if self.memGlobal.varChar:
            print('char:')
            print(self.memGlobal.varChar)
        print('Variables Locales')
        if self.memLocal.varInt:
            print('int:')
            print(self.memLocal.varInt)
        if self.memLocal.varFloat:
            print('float:')
            print(self.memLocal.varFloat)
        if self.memLocal.varBool:
            print('bool:')
            print(self.memLocal.varBool)
        if self.memLocal.varChar:
            print('char:')
            print(self.memLocal.varChar)
        print('Variables Temporales')
        if self.memTemporal.varInt:
            print('int:')
            print(self.memTemporal.varInt)
        if self.memTemporal.varFloat:
            print('float:')
            print(self.memTemporal.varFloat)
        if self.memTemporal.varBool:
            print('bool:')
            print(self.memTemporal.varBool)
        if self.memTemporal.varChar:
            print('char:')
            print(self.memTemporal.varChar)
    def fixType(self,dir,value):
        if dir < 1000:
            return self.memConst.fixType(dir,value)
        elif dir < 2000:
            return self.memGlobal.fixType(dir,value)
        elif dir < 6000:
            return self.memLocal.fixType(dir,value)
        elif dir < 10000:
            return self.memTemporal.fixType(dir,value)
    def getType(self,dir):
        if dir < 1000:
            return self.memConst.getType(dir)
        elif dir < 2000:
            return self.memGlobal.getType(dir)
        elif dir < 6000:
            return self.memLocal.getType(dir)
        elif dir < 10000:
            return self.memTemporal.getType(dir)
    def getValue(self,dir):
        if dir < 1000:
            return self.memConst.getValue(dir)
        elif dir < 2000:
            return self.memGlobal.getValue(dir)
        elif dir < 6000:
            return self.memLocal.getValue(dir)
        elif dir < 10000:
            return self.memTemporal.getValue(dir)
    def setValue(self,value,dir):
        if dir < 1000:
            self.memConst.setValue(value,dir)
        elif dir < 2000:
            self.memGlobal.setValue(value,dir)
        elif dir < 6000:
            self.memLocal.setValue(value,dir)
        elif dir < 10000:
            self.memTemporal.setValue(value,dir)
    def setFunctionValues(self,func):
        if func.id != 'const':
            for i in range(0, len(func.varTable)):
                self.setValue(0, func.varTable[i].dir)
        else:
            for i in range(0, len(func.varTable)):
                self.setValue(func.varTable[i].id, func.varTable[i].dir)

class memoriaFuncion():
    def __init__(self,startInt,startFloat,startBool,startChar):
        self.startInt = startInt
        self.startFloat = startFloat
        self.startBool = startBool
        self.startChar = startChar
        self.varInt = []
        self.varFloat = []
        self.varBool = []
        self.varChar = []

    def fixType(self,dir,value):
        if dir < self.startFloat:
            return int(value)
        elif dir < self.startBool:
            return float(value)
        elif dir < self.startChar:
            return value
        else:
            return str(value)
    def getType(self,dir):
        if dir < self.startFloat:
            return 'int'
        elif dir < self.startBool:
            return 'float'
        elif dir < self.startChar:
            return 'bool'
        else:
            return 'char'
    def getValue(self,dir):
        if dir < self.startFloat:
            return self.varInt[dir-self.startInt]
        elif dir < self.startBool:
            return self.varFloat[dir-self.startFloat]
        elif dir < self.startChar:
            return self.varBool[dir-self.startBool]
        else:
            return self.varChar[dir-self.startChar]
    def setValue(self,value,dir):
        if dir < self.startFloat:
            if len(self.varInt) > dir-self.startInt:
                self.varInt[dir-self.startInt] = value
            else:
                self.varInt.append(value)
        elif dir < self.startBool:
            if len(self.varFloat) > dir-self.startFloat:
                self.varFloat[dir-self.startFloat] = value
            else:
                self.varFloat.append(value)
        elif dir < self.startChar:
            if len(self.varBool) > dir-self.startBool:
                self.varBool[dir-self.startBool] = value
            else:
                self.varBool.append(value)
        else:
            if len(self.varChar) > dir-self.startChar:
                self.varChar[dir-self.startChar] = value
            else:
                self.varChar.append(value)


memoria=memoriaVirtual()
#memoria.setFunctionValues(func)

#for i in range(0,len(memoria.memConst.varBool)):
#    print(memoria.memConst.varBool[i])