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


cuboSemantico = {
# int operacion tipo 
    Type.INT: {
    #int operacion int
      Type.INT: {
        "+":Type.INT,
        "-":Type.INT,
        "*":Type.INT,
        "/":Type.INT,
        ">":Type.BOOL,
        ">=":Type.BOOL,
        "<=":Type.BOOL,
        "<":Type.BOOL,
        "=":Type.INT,
        "==": Type.BOOL,
        "!=":Type.BOOL,
        "and":"Error",
        "or":"Error",
        },
    #int operacion float
      Type.FLOAT: {
        "+":Type.FLOAT,
        "-":Type.FLOAT,
        "*":Type.FLOAT,
        "/":Type.FLOAT,
        ">":Type.BOOL,
        ">=":Type.BOOL,
        "<=":Type.BOOL,
        "<":Type.BOOL,
        "=":Type.INT,
        "==": Type.BOOL,
        "!=":Type.BOOL,
        "and":"Error",
        "or":"Error",
        },
    #int operacion string
      "string": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #int operacion bool
      Type.BOOL: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #int operacion array
      "array": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
      },
#float operacion tipo
    Type.FLOAT:{
    #float operacion int
      Type.INT: {
        "+":Type.FLOAT,
        "-":Type.FLOAT,
        "*":Type.FLOAT,
        "/":Type.FLOAT,
        ">":Type.BOOL,
        ">=":Type.BOOL,
        "<=":Type.BOOL,
        "<":Type.BOOL,
        "=":Type.FLOAT,
        "==": Type.BOOL,
        "!=":Type.BOOL,
        "and":"Error",
        "or":"Error",
        },
    #float operacion float
      Type.FLOAT: {
        "+":Type.FLOAT,
        "-":Type.FLOAT,
        "*":Type.FLOAT,
        "/":Type.FLOAT,
        ">":Type.BOOL,
        ">=":Type.BOOL,
        "<=":Type.BOOL,
        "<":Type.BOOL,
        "=":Type.FLOAT,
        "==": Type.BOOL,
        "!=":Type.BOOL,
        "and":"Error",
        "or":"Error",
        },
    #float operacion string
      "string": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #float operacion bool
      Type.BOOL: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #float operacion array
      "array": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
      },
#string operacion tipo
    "string":{
    #string operacion int
      Type.INT: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #string operacion float
      Type.FLOAT: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #string operacion string
      "string": {
        "+":"string",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"string",
        "==": Type.BOOL,
        "!=":Type.BOOL,
        "and":"Error",
        "or":"Error",
        },
    #string operacion string
      Type.BOOL: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #string operacion array
      "array": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
      },
#bool operacion tipo
    Type.BOOL:{
    #bool operacion int
      Type.INT: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #bool operacion float
      Type.FLOAT: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #bool operacion string
      "string": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==":"Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #bool operacion bool
      Type.BOOL: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":Type.BOOL,
        "==":Type.BOOL,
        "!=":Type.BOOL,
        "and":Type.BOOL,
        "or":Type.BOOL,
        },
    #bool operacion array
      "array": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
      },
#array operacion tipo
    "array":{
    #array operacion int
      Type.INT: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #array operacion float
      Type.FLOAT: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #array operacion string
      "string": {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==":"Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #array operacion bool
      Type.BOOL: {
        "+":"Error",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==":"Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
    #array operacion array
      "array": {
        "+":"Array",
        "-":"Error",
        "*":"Error",
        "/":"Error",
        ">":"Error",
        ">=":"Error",
        "<=":"Error",
        "<":"Error",
        "=":"Error",
        "==": "Error",
        "!=":"Error",
        "and":"Error",
        "or":"Error",
        },
      },
    }

prueba = cuboSemantico['int']['int']['+']
print (prueba)
prueba = cuboSemantico['int']['float']['/']
print (prueba)
prueba = cuboSemantico['bool']['int']['+']
print (prueba)
prueba = cuboSemantico['bool']['bool']['and']
print (prueba)
prueba = cuboSemantico['array']['int']['+']
print (prueba)
