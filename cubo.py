#----------------------------------------------
# cubo semantico
# clase que guarda las reglas de operaciones
# recibe 3 parametros
# tipo 1, tipo 2, y la operacion
#----------------------------------------------

from enum import Enum
class Type(Enum):
     INT = 1
     FLOAT = 2
     CHAR = 3
     BOOL = 4
     ARRAY = 5
     ERROR = -1

class Operation(Enum):
     PLUS = 1
     MINUS = 2
     MULTIPLY = 3
     DIVIDE = 4
     GREATER = 5
     GREATEREQUAL = 6
     LESS = 7
     LESSEQUAL = 8
     ASIGN = 9
     EQUAL = 10
     NOTEQUAL = 11
     AND = 12
     OR = 13
     MOD = 14

charToEnum = {
    "+" : Operation.PLUS,
    "-" : Operation.MINUS,
    "*" : Operation.MULTIPLY,
    "/" : Operation.DIVIDE,
    ">" : Operation.GREATER,
    ">=" : Operation.GREATEREQUAL,
    "<" : Operation.LESS,
    "<=" : Operation.LESSEQUAL,
    "=" : Operation.ASIGN,
    "==" : Operation.EQUAL,
    "!=" : Operation.NOTEQUAL,
    "&&" : Operation.AND,
    "||" : Operation.OR,
    "%" : Operation.MOD,
    "int" : Type.INT,
    "float" : Type.FLOAT,
    "char" : Type.CHAR,
    "bool" : Type.BOOL,
    "arr" : Type.ARRAY,
    "err" : Type.ERROR
}
def getCubeType(typ1,typ2,act):
    return cubo[charToEnum[typ1]][charToEnum[typ2]][charToEnum[act]]

cubo = {
# int operacion tipo
    Type.INT: {
    #int operacion int
      Type.INT: {
        Operation.PLUS:"int",
        Operation.MINUS:"int",
        Operation.MULTIPLY:"int",
        Operation.DIVIDE:"int",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"int",
        Operation.EQUAL:"bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:"int"
        },
    #int operacion float
      Type.FLOAT: {
        Operation.PLUS:"float",
        Operation.MINUS:"float",
        Operation.MULTIPLY:"float",
        Operation.DIVIDE:"float",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"int",
        Operation.EQUAL:"bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:"float"
        },
    #int operacion CHAR
      Type.CHAR: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #int operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #int operacion array
      Type.ARRAY: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#float operacion tipo
    Type.FLOAT:{
    #float operacion int
      Type.INT: {
        Operation.PLUS:"float",
        Operation.MINUS:"float",
        Operation.MULTIPLY:"float",
        Operation.DIVIDE:"float",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"float",
        Operation.EQUAL: "bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion float
      Type.FLOAT: {
        Operation.PLUS:"float",
        Operation.MINUS:"float",
        Operation.MULTIPLY:"float",
        Operation.DIVIDE:"float",
        Operation.GREATER:"bool",
        Operation.GREATEREQUAL:"bool",
        Operation.LESSEQUAL:"bool",
        Operation.LESS:"bool",
        Operation.ASIGN:"float",
        Operation.EQUAL: "bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion CHAR
      Type.CHAR: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #float operacion array
      Type.ARRAY: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#CHAR operacion tipo
    Type.CHAR:{
    #CHAR operacion int
      Type.INT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #CHAR operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #CHAR operacion CHAR
      Type.CHAR: {
        Operation.PLUS:"char",
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:"char",
        Operation.EQUAL: "bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #CHAR operacion CHAR
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #CHAR operacion array
      Type.ARRAY: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#bool operacion tipo
    Type.BOOL:{
    #bool operacion int
      Type.INT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #bool operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #bool operacion CHAR
      Type.CHAR: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #bool operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:"bool",
        Operation.EQUAL:"bool",
        Operation.NOTEQUAL:"bool",
        Operation.AND:"bool",
        Operation.OR:"bool",
        Operation.MOD:Type.ERROR
        },
    #bool operacion array
      Type.ARRAY: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
#array operacion tipo
    Type.ARRAY:{
    #array operacion int
      Type.INT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #array operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #array operacion CHAR
      Type.CHAR: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #array operacion bool
      Type.BOOL: {
        Operation.PLUS:Type.ERROR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
    #array operacion array
      Type.ARRAY: {
        Operation.PLUS:Type.ARRAY,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.ERROR,
        Operation.EQUAL:Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.ERROR
        },
      },
    }

#prueba = cubo[Type.INT][Type.INT][Operation.PLUS]
#print (prueba)
# prueba = cubo[Type.INT][Type.FLOAT][Operation.DIVIDE]
# print (prueba)
# prueba = cubo[Type.BOOL][Type.INT][Operation.PLUS]
# print (prueba)
# prueba = cubo[Type.BOOL][Type.BOOL][Operation.AND]
# print (prueba)
# prueba = cubo[Type.ARRAY][Type.INT][Operation.PLUS]
# print (prueba)
