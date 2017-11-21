#----------------------------------------------
# Regina Gallardo A00815711
# Arturo Moran A00
# cubo semantico
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


cubo = {
# int operacion tipo 
    Type.INT: {
    #int operacion int
      Type.INT: {
        Operation.PLUS:Type.INT,
        Operation.MINUS:Type.INT,
        Operation.MULTIPLY:Type.INT,
        Operation.DIVIDE:Type.INT,
        Operation.GREATER:Type.BOOL,
        Operation.GREATEREQUAL:Type.BOOL,
        Operation.LESSEQUAL:Type.BOOL,
        Operation.LESS:Type.BOOL,
        Operation.ASIGN:Type.INT,
        Operation.EQUAL: Type.BOOL,
        Operation.NOTEQUAL:Type.BOOL,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.INT
        },
    #int operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.FLOAT,
        Operation.MINUS:Type.FLOAT,
        Operation.MULTIPLY:Type.FLOAT,
        Operation.DIVIDE:Type.FLOAT,
        Operation.GREATER:Type.BOOL,
        Operation.GREATEREQUAL:Type.BOOL,
        Operation.LESSEQUAL:Type.BOOL,
        Operation.LESS:Type.BOOL,
        Operation.ASIGN:Type.INT,
        Operation.EQUAL: Type.BOOL,
        Operation.NOTEQUAL:Type.BOOL,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD:Type.FLOAT
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
        },
      },
#float operacion tipo
    Type.FLOAT:{
    #float operacion int
      Type.INT: {
        Operation.PLUS:Type.FLOAT,
        Operation.MINUS:Type.FLOAT,
        Operation.MULTIPLY:Type.FLOAT,
        Operation.DIVIDE:Type.FLOAT,
        Operation.GREATER:Type.BOOL,
        Operation.GREATEREQUAL:Type.BOOL,
        Operation.LESSEQUAL:Type.BOOL,
        Operation.LESS:Type.BOOL,
        Operation.ASIGN:Type.FLOAT,
        Operation.EQUAL: Type.BOOL,
        Operation.NOTEQUAL:Type.BOOL,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
        },
    #float operacion float
      Type.FLOAT: {
        Operation.PLUS:Type.FLOAT,
        Operation.MINUS:Type.FLOAT,
        Operation.MULTIPLY:Type.FLOAT,
        Operation.DIVIDE:Type.FLOAT,
        Operation.GREATER:Type.BOOL,
        Operation.GREATEREQUAL:Type.BOOL,
        Operation.LESSEQUAL:Type.BOOL,
        Operation.LESS:Type.BOOL,
        Operation.ASIGN:Type.FLOAT,
        Operation.EQUAL: Type.BOOL,
        Operation.NOTEQUAL:Type.BOOL,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
        },
    #CHAR operacion CHAR
      Type.CHAR: {
        Operation.PLUS:Type.CHAR,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.CHAR,
        Operation.EQUAL: Type.BOOL,
        Operation.NOTEQUAL:Type.BOOL,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.MOD: Type.ERROR
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
        Operation.ASIGN:Type.BOOL,
        Operation.EQUAL:Type.BOOL,
        Operation.NOTEQUAL:Type.BOOL,
        Operation.AND:Type.BOOL,
        Operation.OR:Type.BOOL,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
        Operation.MOD: Type.ERROR
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
        Operation.MOD: Type.ERROR
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
        Operation.EQUAL: Type.ERROR,
        Operation.NOTEQUAL:Type.ERROR,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        Operation.MOD: Type.ERROR
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
