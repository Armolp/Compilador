#----------------------------------------------
# Regina Gallardo A00815711
# Arturo Moran A00
# cubo semantico
#----------------------------------------------

from enum import Enum
class Type(Enum):
     INT = 1
     FLOAT = 2
     STRING = 3
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
        },
    #int operacion string
      Type.STRING: {
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
        },
    #float operacion string
      Type.STRING: {
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
        },
      },
#string operacion tipo
    Type.STRING:{
    #string operacion int
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
        },
    #string operacion float
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
        },
    #string operacion string
      Type.STRING: {
        Operation.PLUS:Type.STRING,
        Operation.MINUS:Type.ERROR,
        Operation.MULTIPLY:Type.ERROR,
        Operation.DIVIDE:Type.ERROR,
        Operation.GREATER:Type.ERROR,
        Operation.GREATEREQUAL:Type.ERROR,
        Operation.LESSEQUAL:Type.ERROR,
        Operation.LESS:Type.ERROR,
        Operation.ASIGN:Type.STRING,
        Operation.EQUAL: Type.BOOL,
        Operation.NOTEQUAL:Type.BOOL,
        Operation.AND:Type.ERROR,
        Operation.OR:Type.ERROR,
        },
    #string operacion string
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
        },
    #string operacion array
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
        },
    #bool operacion string
      Type.STRING: {
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
        },
    #array operacion string
      Type.STRING: {
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
        },
      },
    }

# prueba = cubo[Type.INT][Type.INT][Operation.PLUS]
# print (prueba)
# prueba = cubo[Type.INT][Type.FLOAT][Operation.DIVIDE]
# print (prueba)
# prueba = cubo[Type.BOOL][Type.INT][Operation.PLUS]
# print (prueba)
# prueba = cubo[Type.BOOL][Type.BOOL][Operation.AND]
# print (prueba)
# prueba = cubo[Type.ARRAY][Type.INT][Operation.PLUS]
# print (prueba)
