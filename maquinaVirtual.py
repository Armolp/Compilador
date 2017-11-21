from dirFunc import *
from cuadruplo import *
from cubo import *
from memoriaVirtual import *

var1 =Var('1','int', 0)
var2 =Var('5','int', 1)
var3 =Var('true',bool, 400)
var4 =Var(.5,'float', 200)
var5 =Var('c','char', 600)
var6 =Var('a','char', 601)

func = Func('cons','constante',0)
func.varTable.append(var1)
func.varTable.append(var2)
func.varTable.append(var3)
func.varTable.append(var4)
func.varTable.append(var5)
func.varTable.append(var6)

cuads =[]

cuads.append(cuadruplo(len(cuads),'goto','none', 'none', 4))
cuads.append(cuadruplo(len(cuads),'=',0, 'none', 2000))
cuads.append(cuadruplo(len(cuads),'return',2000, 'none','none'))
cuads.append(cuadruplo(len(cuads),'EndProc','none', 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'era',1000, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'param',1, 'none', 'param1'))
cuads.append(cuadruplo(len(cuads),'gosub',1, 'none', 'none'))
cuads.append(cuadruplo(len(cuads),'+',1, 1, 1001))
cuads.append(cuadruplo(len(cuads),'END','none', 'none', 'none'))

dir = DirFunc()
dir.functions.append(func)

class maquinaVirtual():

    def __init__(self, fd, cuadruplos):
        self.cuadruplos = cuadruplos
        self.fd = fd
        self.cuadActual = 0
        self.returnDir = []
        self.cuadReturn = []
        self.memVirtual = memoriaVirtual()
        self.memVirtual.setFunctionValues(self.fd.functions[0])
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
        self.parametros.append(cuad.arg1)
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
        arg1 = memoria.fixTypeType(cuad.arg1, arg1)
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
            valor = memoria.getValue(var)
            tipo = memoria.getType(var)
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
        memoria = self.memVirtual
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
            else:
                print('not implemented yet')

            self.cuadActual = self.cuadActual + 1
        self.memVirtual.memConst = memoria.memConst
        self.memVirtual.memGlobal = memoria.memGlobal




maquina = maquinaVirtual(dir,cuads)
maquina.run(0,'END')
maquina.memVirtual.printMemoria()




