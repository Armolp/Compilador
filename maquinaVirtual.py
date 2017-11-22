from Compilador.cuadruplo import *
from Compilador.dirFunc import *
from Compilador.memoriaVirtual import *

var1 =Var(0,'int', 0)
var2 =Var(3,'int', 1)
var3 =Var(1,'int', 2)
var4 =Var('x','int', 2000)
var5 =Var('y','int', 2000)
var6 =Var('func','int', 1000)

func1 = Func('const','constante',0)
func1.varTable.append(var1)
func1.varTable.append(var2)
func1.varTable.append(var3)

func2 = Func('glob','global',1)
func2.varTable.append(var6)

func3 = Func('loc','local',2)
func3.varTable.append(var4)
func3.varTable.append(var5)

dir = DirFunc()
dir.functions.append(func1)
dir.functions.append(func2)
dir.functions.append(func3)

cuads =[]

cuads.append(cuadruplo(len(cuads),'goto','none', 'none', 13))
cuads.append(cuadruplo(len(cuads),'==',2000, 0, 8000))
cuads.append(cuadruplo(len(cuads),'gotoF',8000, 'none',5))
cuads.append(cuadruplo(len(cuads),'return',0, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'goto','none', 'none', 12))
cuads.append(cuadruplo(len(cuads),'era',1000, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'-',2000, 2, 6000))
cuads.append(cuadruplo(len(cuads),'param',6000, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'gosub',1, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'=',1000, 'none', 6001))
cuads.append(cuadruplo(len(cuads),'+',2000, 6001, 6002))
cuads.append(cuadruplo(len(cuads),'return',6002, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'EndProc','none', 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'era',1000, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'param',1,'none', 'none'))
cuads.append(cuadruplo(len(cuads),'gosub',1, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'=',1000, 'none', 6000))
cuads.append(cuadruplo(len(cuads),'=',6000, 'none', 2000))
cuads.append(cuadruplo(len(cuads),'print',2000, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'END','none', 'none', 'none'))

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
    def era(self,cuad):
        self.returnDir.append(cuad.arg1)
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
    def printVar(self,cuad,memoria):
        value = memoria.getValue(cuad.arg1)
        print(value)
    def run(self,begin,end):
        memoria = memoriaVirtual()
        memoria.memGlobal = self.memVirtual.memGlobal
        memoria.memConst = self.memVirtual.memConst
        self.vaciarParametros(memoria)
        self.cuadActual = begin
        while self.cuadruplos[self.cuadActual].accion != end:
            cuadruplo = self.cuadruplos[self.cuadActual]
            accion = cuadruplo.accion
            #print('do: ' + str(self.cuadruplos[self.cuadActual]))
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

            else:
                print('ERROR, cuadruplo no acceptado: ')
                print(cuadruplo)

            self.cuadActual = self.cuadActual + 1
        self.memVirtual.memConst = memoria.memConst
        self.memVirtual.memGlobal = memoria.memGlobal

maquina = maquinaVirtual(dir,cuads)
maquina.run(0,'END')
#maquina.memVirtual.printMemoria()






