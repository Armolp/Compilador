import ply.lex as lex
import ply.yacc as yacc
from dirFunc import *
from cuadruplo import *

StackDebuging = False

tokens = [
    'LPAR','RPAR','LBRACE','RBRACE','LBRACKET','RBRACKET',
    'NOT','AND','OR',
    'LT','LET','GT','GET','EQT','NEQT',
    'EQ','SUM','SUB','MULT','DIV','MOD',
    'COMA','SEMI',
    'INT','STRING','FLOAT','BOOL','CHAR',
    'ID'
]

reserved = {
    'init' : 'INIT',
    'loop' : 'LOOP',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'do' : 'DO',
    'while' : 'WHILE',
    'sin' : 'SINFUNC',
    'void' : 'TYPEVOID',
    'int' : 'TYPEINT',
    'float' : 'TYPEFLOAT',
    'bool' : 'TYPEBOOL',
    'char' : 'TYPECHAR'
}

tokens += reserved.values()

t_LPAR = r'\('
t_RPAR = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r']'

t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'

t_LT = r'<'     #Less Than
t_LET = r'<='   #Less or Equal Than
t_GT = r'\>'     #Greater Than
t_GET = r'>='   #Greater or Equal Than
t_EQT = r'=='   #EQual To
t_NEQT = r'!='  #Not EQual To

t_EQ = r'\='
t_SUM = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'\%'

t_COMA = r'\,'
t_SEMI = r';'


t_INT = r'\d+'
t_FLOAT = r'[0-9]+\.[0-9]+((E|e)[+,-]?[0-9]+)?'
t_BOOL = r'(true|false)'
t_CHAR = r'.'
t_STRING = r'(\'.*\' | \".*\")'

t_ignore = ' \t'

def t_ID(t):
    r'[a-z](_?[a-zA-Z0-9])*'
    if t.value in reserved:
      if(t.value == 'program'):
        t.lexer.lineno = 0
      t.type = reserved[t.value]
      return t
    t.value = str(t.value)
    #print(t)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#Es llamado cuando sucede un error en el scanner
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
#fin de scanner

#--------------------------------------------------------------

#inicio de parser

def p_programa(p):
    "programa : prog init loop endQuad"

def p_endQuad(p):
    "endQuad :"
    act = "END"
    cuads.append(cuadruplo(len(cuads), act, None, None, None))

def p_prog(p):
    """prog : variable prog
            | funcion prog
            | empty"""

def p_init(p):
    #init(INT,INT){}
    "init : INIT addFunc LPAR INT COMA INT RPAR bloque"

def p_addFunc(p):
    "addFunc : empty"
    if p[-2] == None:
        functions.append(Func(p[-1], "void", -1))
    else:
        functions.append(Func(p[-1], p[-2], -1))
    global scope
    scope = len(functions) -1

def p_loop(p):
    "loop : LOOP addFunc bloque"

# variable (int x = 0;) -----------------------------------------
def p_variable(p):
    "variable : tipo var SEMI"
    functions[scope].varTable.append(Var(p[2], p[1], -1))
def p_var(p):
    "var : ID arr var2"
    p[0] = p[1]

def p_var2(p):
    """var2 : COMA var
            | empty"""
def p_arr(p):
    """arr : LBRACKET INT RBRACKET arr2
           | empty
       arr2 : LBRACKET INT RBRACKET
            | empty"""
# funcion --------------------------------------------------
def p_funcion(p):
    "funcion : tipo ID addFunc LPAR func1 RPAR bloque"
    global scope
    scope = 0
def p_func1(p):
    """func1 : func2
            | empty"""
def p_func2(p):
    "func2 : parametro func3"
def p_func3(p):
    """func3 : COMA func2
            | empty"""
# tipo -------------------------------------------------------
def p_tipo(p):
    """tipo : TYPEVOID
            | TYPEINT
            | TYPEFLOAT
            | TYPEBOOL
            | TYPECHAR"""
    p[0] = p[1]

def p_parametro(p):
    "parametro : tipo ID arr"
    functions[scope].varTable.append(Var(p[2], p[1], -1))

# bloque -------------------------------------------------
def p_bloque(p):
    "bloque : LBRACE bloq1 RBRACE"
def p_bloq1(p):
    """bloq1 : estatuto bloq1
            | empty"""
# estatuto ------------------------------------------------
def p_estatuto(p):
    """estatuto : asignacion
            | condicion
            | variable
            | invocacion
            | ciclo"""
# asignacion ----------------------------------------
def p_asignacion(p):
    "asignacion : ID arr EQ expresion SEMI eqQuad"

def p_eqQuad(p):
    "eqQuad :"
    if StackDebuging:
        print operators
        print operands

    global tempNum
    act = "="
    arg1 = operands.pop()
    res = p[-5]
    cuads.append(cuadruplo(len(cuads), act, arg1, None, res))
    #operands.append(res)
    tempNum += 1

# condicion --------------------------------------
def p_condicion(p):
    "condicion : IF LPAR expresion RPAR ifQuad1 bloque cond1 ifQuad3"
def p_cond1(p):
    """cond1 : ELSE ifQuad2 bloque
            | empty"""
# gotoF generation
def p_ifQuad1(p):
    "ifQuad1 :"
    if StackDebuging:
        print jumps

    global tempNum
    act = "gotoF"
    arg1 = operands.pop()
    cuads.append(cuadruplo(len(cuads), act, arg1, None, None))
    jumps.append(len(cuads)-1)

def p_ifQuad2(p):
    "ifQuad2 :"
    if StackDebuging:
        print jumps

    act = "goto"
    cuads.append(cuadruplo(len(cuads),act,None,None,None))
    # modify last goto
    idx = jumps.pop()
    cuads[idx].arg3 = len(cuads)

    jumps.append(len(cuads)-1)

def p_ifQuad3(p):
    "ifQuad3 :"
    if StackDebuging:
        print jumps
    act = "goto"
    idx = jumps.pop()
    cuads[idx].arg3 = len(cuads)


# invocacion -------------------------------------
def p_invocacion(p):
    "invocacion : ID LPAR invo1 RPAR SEMI"
def p_invo1(p):
    """invo1 : expresion invo2
            | empty"""
def p_invo2(p):
    """invo2 : COMA expresion invo2
            | empty"""

# ciclo ------------------------------------------
def p_ciclo(p):
    """ciclo : WHILE LPAR expresion RPAR bloque
            | DO bloque WHILE LPAR expresion RPAR SEMI
            | FOR LPAR ciclo1 SEMI expresion SEMI ciclo1 RPAR"""
def p_ciclo1(p):
    """ciclo1 : asignacion
            | empty"""

# expresion binaria (&&,||) -----------------------------
def p_expresion(p):
    "expresion : not expbool popBinExp bin"
def p_not(p):
    """not : NOT
            | empty"""
def p_bin(p):
    """bin : opbin expresion
            | empty"""
def p_opbin(p):
    """opbin : AND
            | OR"""
    operators.append(p[1])
def p_popBinExp(p):
    "popBinExp :"
    global tempNum
    oper = ["||","&&"]
    if len(operators) > 0:
        if  operators[-1] in oper:
            if StackDebuging:
                print operators
                print operands

            act = operators.pop()
            arg2 = operands.pop()
            arg1 = operands.pop()
            res = "t" + str(tempNum)
            cuads.append(cuadruplo(len(cuads),act,arg1, arg2, res))
            operands.append(res)
            tempNum += 1


def p_expbool(p):
    "expbool : exp expbool1"
def p_expbool1(p):
    """expbool1 : opbool exp popBoolExp
            | empty"""
def p_opbool(p):
    """opbool : LT
            | GT
            | LET
            | GET
            | EQT
            | NEQT"""
    operators.append(p[1])

def p_popBoolExp(p):
    "popBoolExp :"
    global tempNum
    oper = ["<","<=",">",">=","==","!="]
    if len(operators) > 0:
        if  operators[-1] in oper:
            if StackDebuging:
                print operators
                print operands

            act = operators.pop()
            arg2 = operands.pop()
            arg1 = operands.pop()
            res = "t" + str(tempNum)
            cuads.append(cuadruplo(len(cuads),act,arg1, arg2, res))
            operands.append(res)
            tempNum += 1


def p_exp(p):
    "exp : term popExp exp1"

def p_popExp(p):
    "popExp :"
    global tempNum
    oper = ["+","-"]
    if len(operators) > 0:
        if  operators[-1] in oper:
            if StackDebuging:
                print operators
                print operands

            act = operators.pop()
            arg2 = operands.pop()
            arg1 = operands.pop()
            res = "t" + str(tempNum)
            cuads.append(cuadruplo(len(cuads),act,arg1, arg2, res))
            operands.append(res)
            tempNum += 1


def p_exp1(p):
    """exp1 : opexp exp
            | empty"""
def p_opexp(p):
    """opexp : SUB
            | SUM"""
    operators.append(p[1])
    #print operators

def p_term(p):
    "term : factor popFactor term1"
def p_term1(p):
    """term1 : opterm term
            | empty"""

def p_popFactor(p):
    "popFactor :"
    global tempNum
    oper = ["*","/","%"]
    if len(operators) > 0:
        if  operators[-1] in oper:
            if StackDebuging:
                print operators
                print operands

            act = operators.pop()
            arg2 = operands.pop()
            arg1 = operands.pop()
            res = "t" + str(tempNum)
            cuads.append(cuadruplo(len(cuads),act,arg1, arg2, res))
            operands.append(res)
            tempNum += 1

def p_opterm(p):
    """opterm : MULT
            | DIV
            | MOD"""
    operators.append(p[1])
    #print operators

def p_factor(p):
    "factor : opfactor fact1"

def p_fact1(p):
    """fact1 : ID pushConst
            | INT pushConst
            | FLOAT pushConst
            | BOOL pushConst
            | CHAR pushConst
            | LPAR pushPar expresion RPAR popPar
            | invocacion"""

def p_pushConst(p):
    "pushConst :"
    operands.append(p[-1])
    #print operands

def p_pushPar(p):
    "pushPar :"
    operators.append(p[-1])
    #print operators

def p_popPar(p):
    "popPar :"
    operators.pop()
    #print operators

def p_opfactor(p):
    """opfactor : SUB subQuad
            | empty"""

def p_subQuad(p):
    "subQuad :"
    operators.append("*")
    operands.append(-1)

def p_empty(p):
    'empty :'
    pass

#

#Es llamado cuando sucede un error en el parser
def p_error(p):
    print("Syntax error at '%s' in line '%s'" % (p.value, p.lineno))

# Crea el parser dandole el estado inicial
parser = yacc.yacc(start = 'programa')

def readFile(file):
    file_in = open(file, 'r')
    data = file_in.read()
    file_in.close()
    parser.parse(data)




#list of functions that holds Func objects
functions = []
# list of cuad commands
cuads = []
# temporal directions counter
tempNum = 1
# current scope start in global scope
scope = 0
# stacks
jumps = []
operators = []
operands = []
types = []

# Initialize the function list with the default functions
functions.append(Func("global", "void", -1))

# functions[0].varTable.append(Var("i", "int", -1))
# functions[0].varTable.append(Var("j", "int", -1))
# functions[0].varTable.append(Var("k", "int", -1))

readFile("testing\codigoPrueba.txt")

def printDirFunc():
    for i in range(0,len(functions)):
        print(functions[i].id)
        for j in range(0, len(functions[i].varTable)):
            print("\t" + functions[i].varTable[j].id)

for i in range(0, len(cuads)):
    print str(cuads[i])
