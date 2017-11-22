from Compilador.cuadruplo import *
from Compilador.dirFunc import *
from Compilador.memoriaVirtual import *
from tkinter import *
from math import sin, cos
import time


class parametros():
    def __init__(self,value,type):
        self.value = value
        self.type = type

class maquinaVirtual():

    def __init__(self, fd, cuadruplos):
        self.cuadruplos = cuadruplos
        self.fd = fd
        self.cuadActual = 0
        self.returnDir = []
        self.cuadReturn = []
        self.memVirtual = memoriaVirtual()
        for i in range(0,len(self.fd.functions)):
            self.memVirtual.setFunctionValues(self.fd.functions[i])
        self.parametros = []
        self.tk = Tk()
        self.c = Canvas(self.tk, width=500, height=500)
        self.c.pack()

    def goto(self,cuad):
        self.cuadActual = cuad.arg3-1
    def gotoF(self,cuad,memoria):
        arg1 = memoria.getValue(cuad.arg1)
        if not arg1:
            self.cuadActual = cuad.arg3-1
    def gotoT(self,cuad,memoria):
        arg1 = memoria.getValue(cuad.arg1)
        if not arg1:
            self.cuadActual = cuad.arg3-1
    def goSub(self,cuad):
        begin = cuad.arg1
        self.cuadReturn.append(self.cuadActual)
        self.run(begin,'EndProc')
        self.cuadActual = self.cuadReturn.pop()

    def param(self,cuad,memoria):
        valor = memoria.getValue(cuad.arg1)
        tipo = memoria.getType(cuad.arg1)
        parametro = parametros(valor,tipo)
        self.parametros.append(parametro)
    def ret(self,cuad,memoria):
        value = memoria.getValue(cuad.arg1)
        dir = self.returnDir.pop()
        memoria.setValue(value,dir)
    def verify(self):
        print("does verify")
    def era(self, cuad):
        self.returnDir.append(cuad.arg1)

    def opArit(self,cuad,memoria):
        arg1 = memoria.getValue(cuad.arg1)
        arg2 = memoria.getValue(cuad.arg2)
        arg3 = cuad.arg3
        accion = cuad.accion
        arg1 = memoria.fixType(cuad.arg1,arg1)
        arg2 = memoria.fixType(cuad.arg2,arg2)

        if accion == '+':
            value = arg1 + arg2
        elif accion == '-':
            value = arg1 - arg2
        elif accion == '*':
            value = arg1 * arg2
        elif accion == '/':
            value = arg1 / arg2
        elif accion == '%':
            value = arg1 % arg2

        memoria.setValue(value,arg3)
    def opWithDiv(self,cuad,memoria):
        arg2 = memoria.getValue(cuad.arg2)
        arg2 = memoria.fixType(cuad.arg2, arg2)
        if(arg2 == 0):
            print('ERROR division con 0')
            quit()
        self.opArit(cuad,memoria)
    def opLogic(self,cuad,memoria):
        arg1 = memoria.getValue(cuad.arg1)
        arg2 = memoria.getValue(cuad.arg2)
        arg3 = cuad.arg3
        accion = cuad.accion
        arg1 = memoria.fixType(cuad.arg1, arg1)
        arg2 = memoria.fixType(cuad.arg2, arg2)

        if accion == 'AND':
            value = arg1 and arg2
        elif accion == 'OR':
            value = arg1 or arg2
        elif accion == '<':
            value = arg1 < arg2
        elif accion == '<=':
            value = arg1 <= arg2
        elif accion == '>':
            value = arg1 > arg2
        elif accion == '>=':
            value = arg1 >= arg2
        elif accion == '!=':
            value = arg1 != arg2
        elif accion == '==':
            value = arg1 == arg2

        memoria.setValue(value, arg3)
    def asign(self,cuad,memoria):
        value = memoria.getValue(cuad.arg1)
        memoria.setValue(value,cuad.arg3)

    def printVar(self,cuad,memoria):
        value = memoria.getValue(cuad.arg1)
        print(value)
    def cosin(self,cuad,memoria):
        arg1 = memoria.getValue(cuad.arg1)
        arg1 = memoria.fixType(cuad.arg1,arg1)
        dir = cuad.arg3
        accion = cuad.accion
        if accion == 'cos':
            ans = cos(arg1)
        else:
            ans = sin(arg1)
        memoria.setValue(ans, dir)
    def draw(self,cuad,memoria):
        arg1 = memoria.getValue(cuad.arg1)
        x = memoria.fixType(cuad.arg1, arg1)
        arg2 = memoria.getValue(cuad.arg2)
        y = memoria.fixType(cuad.arg2, arg2)
        accion = cuad.accion
        if accion == 'drawPoint':
            r = 1
        else:
            arg3 = memoria.getValue(cuad.arg3)
            r = memoria.fixType(cuad.arg3, arg3)
        self.c.create_oval(x - r, y - r, x + r, y + r, fill='black')

    def draw2(self,cuad1,cuad2,memoria):
        arg1 = memoria.getValue(cuad1.arg1)
        x1 = memoria.fixType(cuad1.arg1, arg1)
        arg2 = memoria.getValue(cuad1.arg2)
        y1 = memoria.fixType(cuad1.arg2, arg2)
        arg3 = memoria.getValue(cuad2.arg1)
        x2 = memoria.fixType(cuad2.arg1, arg3)
        arg4 = memoria.getValue(cuad2.arg2)
        y2 = memoria.fixType(cuad2.arg2, arg4)
        accion = cuad1.accion
        if accion == 'rect1':
            self.c.create_rectangle(x1,y1,x2,y2, fill='black')
        else:
            self.c.create_line(x1,y1,x2,y2)

    def vaciarParametros(self,memoria):
        self.parametros.reverse()
        while self.parametros:
            var = self.parametros.pop()
            valor = var.value
            tipo = var.type
            if tipo == 'int':
                dir = 2000 + len(memoria.memLocal.varInt)
            elif tipo == 'float':
                dir = 3000 + len(memoria.memLocal.varFloat)
            elif tipo == 'bool':
                dir = 4000 + len(memoria.memLocal.varBool)
            elif tipo == 'char':
                dir = 5000 + len(memoria.memLocal.varChar)
            memoria.setValue(valor,dir)

    def run(self,begin,end):
        memoria = memoriaVirtual()
        memoria.memGlobal = self.memVirtual.memGlobal
        memoria.memConst = self.memVirtual.memConst
        self.vaciarParametros(memoria)
        self.cuadActual = begin
        while self.cuadruplos[self.cuadActual].accion != end:
            cuadruplo = self.cuadruplos[self.cuadActual]
            accion = cuadruplo.accion
            print('do: ' + str(self.cuadruplos[self.cuadActual]))
            if accion == 'goto':
                self.goto(cuadruplo)
            elif accion == 'gotoF':
                self.gotoF(cuadruplo, memoria)
            elif accion == 'gotoT':
                self.gotoT(cuadruplo, memoria)
            elif accion == 'era':
                self.era(cuadruplo)
            elif accion == 'gosub':
                self.goSub(cuadruplo)
            elif accion == 'param':
                self.param(cuadruplo,memoria)
            elif accion == 'return':
                self.ret(cuadruplo,memoria)
            elif accion == 'verify':
                self.verify()
            elif accion == '+' or accion == '-' or accion == '*':
                self.opArit(cuadruplo,memoria)
            elif accion == '/' or accion == '%':
                self.opWithDiv(cuadruplo,memoria)
            elif accion == 'AND' or accion == 'OR' or accion == '<' or accion == '<=' or accion == '>' or accion == '>=' or accion == '!=' or accion == '==':
                self.opLogic(cuadruplo,memoria)
            elif accion == '=':
                self.asign(cuadruplo,memoria)
            elif accion == 'print':
                self.printVar(cuadruplo,memoria)
            elif accion == 'cos' or accion == 'sin':
                self.cosin(cuadruplo,memoria)
            elif accion == 'drawPoint' or accion == 'drawCircle':
                self.draw(cuadruplo,memoria)
            elif accion == 'rect1' or accion == 'from':
                self.cuadActual+=1
                cuad2 = self.cuadruplos[self.cuadActual]
                self.draw2(cuadruplo,cuad2,memoria)
            elif accion == 'update':
                time.sleep(0.01)
                self.tk.update()
            elif accion =='delete':
                self.c.delete(ALL)
            else:
                print('ERROR, cuadruplo no acceptado: ')
                print(cuadruplo)

            self.cuadActual = self.cuadActual + 1
        self.memVirtual.memConst = memoria.memConst
        self.memVirtual.memGlobal = memoria.memGlobal

#maquina = maquinaVirtual(dir,cuads)
#maquina.run(0,'END')







