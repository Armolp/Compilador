import ply.lex as lex
import ply.yacc as yacc
from dirFunc import *
from cuadruplo import *
from cubo import *
from maquinaVirtual import *

StackDebuging = False

tokens = [
    'LPAR','RPAR','LBRACE','RBRACE','LBRACKET','RBRACKET',
    'NOT','AND','OR',
    'LT','LET','GT','GET','EQT','NEQT',
    'EQ','SUM','SUB','MULT','DIV','MOD',
    'COMA','SEMI',
    'INT','STRING','FLOAT','CHAR',
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
    'void' : 'TYPEVOID',
    'int' : 'TYPEINT',
    'float' : 'TYPEFLOAT',
    'bool' : 'TYPEBOOL',
    'char' : 'TYPECHAR',
    'true' : 'BOOL',
    'false' : 'BOOL',
    'return' : 'RETURN',
    'func' : 'FUNC',

    'sin' : 'SINFUNC',
    'cos' : 'COSFUNC',
    'drawPoint' : 'POINTFUNC',
    'drawCircle' : 'CIRCLEFUNC',
    'drawRect' : 'RECTFUNC',
    'drawLine' : 'LINEFUNC',

    'print' : 'PRINTFUNC'
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
    "programa : startQuad prog init loop"

def p_prog(p):
    """prog : variable prog
            | funcion prog
            | empty"""

def p_startQuad(p):
    "startQuad :"
    act = "goto"
    cuads.append(cuadruplo(len(cuads), act, None, None, None))
    jumps.append(len(cuads)-1)
# funcion init y loop -----------------------------------------------
def p_init(p):
    "init : INIT addInit initQuad1 bloque"

def p_loop(p):
    "loop : LOOP addInit loopQuad1 bloque loopQuad2"

def p_addInit(p):
    "addInit : empty"
    functions.append(Func(p[-1], "void", len(cuads)))
    global scope
    scope = len(functions) -1

def p_initQuad1(p):
    "initQuad1 :"
    idx = jumps.pop()
    cuads[idx].arg3 = len(cuads)
def p_loopQuad1(p):
    "loopQuad1 :"
    jumps.append(len(cuads))
    act = "delete"
    cuads.append(cuadruplo(len(cuads), act, None, None, None))
def p_loopQuad2(p):
    "loopQuad2 :"
    act = "update"
    cuads.append(cuadruplo(len(cuads), act, None, None, None))
    act = "goto"
    arg3 = jumps.pop()
    cuads.append(cuadruplo(len(cuads), act, None, None, arg3))

# variable (int x = 0;) -----------------------------------------

currentVarType = None
def p_variable(p):
    "variable : tipo setCurrType var SEMI"
def p_var(p):
    "var : ID addVar arr var2"
def p_var2(p):
    """var2 : COMA var
            | empty"""
def p_arr(p):
    """arr : LBRACKET INT RBRACKET arr2
           | empty
       arr2 : LBRACKET INT RBRACKET
            | empty"""

def p_setCurrType(p):
    "setCurrType :"
    global currentVarType
    currentVarType = p[-1]

def p_addVar(p):
    "addVar :"
    global scope

    ID = p[-1]
    localVars = list(map(lambda x: x.id ,functions[scope].varTable))
    globalVars = list(map(lambda x: x.id ,functions[1].varTable))
    if ID in localVars or ID in globalVars:
        msg = "ERROR: "+ID+" is already defined."
        raise ValueError(msg)
    else:
        global currentVarType
        newDir = getDir(currentVarType)
        functions[scope].varTable.append(Var( ID, currentVarType, newDir))


# funcion --------------------------------------------------
def p_funcion(p):
    "funcion : FUNC funcType ID addFunc LPAR func1 RPAR bloque endProcQuad"
    global scope
    scope = 1
    resetVarCounters()
def p_funcType(p):
    """funcType : TYPEVOID
                | tipo"""
    p[0] = p[1]
def p_func1(p):
    """func1 : func2
            | empty"""
def p_func2(p):
    "func2 : parametro func3"
def p_func3(p):
    """func3 : COMA func2
            | empty"""

def p_addFunc(p):
    "addFunc : empty"
    functions.append(Func(p[-1], p[-2], len(cuads)))
    global scope
    scope = len(functions) -1

def p_endProcQuad(p):
    "endProcQuad :"
    act = "EndProc"
    cuads.append(cuadruplo(len(cuads), act, None, None, None))
# tipo -------------------------------------------------------
def p_tipo(p):
    """tipo : TYPEINT
            | TYPEFLOAT
            | TYPEBOOL
            | TYPECHAR"""
    p[0] = p[1]
def p_parametro(p):
    "parametro : tipo ID arr"
    ID = p[2]
    localVars = list(map(lambda x: x.id ,functions[scope].varTable))
    globalVars = list(map(lambda x: x.id ,functions[1].varTable))
    if ID in localVars or ID in globalVars:
        msg = "ERROR: "+ID+" is already defined."
        raise ValueError(msg)
    else:
        global currentVarType
        newDir = getDir(p[1])
        functions[scope].varTable.append(Var( ID, p[1], newDir))

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
                | invocacion SEMI
                | ciclo
                | return """

# return --------------------------------------------------

def p_return(p):
    "return : RETURN expresion returnQuad SEMI"

def p_returnQuad(p):
    "returnQuad :"
    act = "return"
    arg1 = getDirById(operands.pop())
    cuads.append(cuadruplo(len(cuads), act, arg1, None, None))


# asignacion ----------------------------------------
def p_asignacion(p):
    "asignacion : ID arr EQ expresion SEMI eqQuad"

def p_eqQuad(p):
    "eqQuad :"
    if StackDebuging:
        print (operators)
        print (operands)

    ID = p[-5]
    localVars = list(map(lambda x: x.id ,functions[scope].varTable))
    globalVars = list(map(lambda x: x.id ,functions[1].varTable))
    if ID in localVars or ID in globalVars:
        global tempNum
        act = "="
        arg1 = getDirById(operands.pop())
        typ1 = types.pop()
        res = getDirById(ID)
        typ2 = getTypeById(ID)
        resType = getCubeType(typ1,typ2,act)
        if(resType == Type.ERROR):
            msg = "ERROR: can't assign "+typ1+" to "+typ2+"."
            raise ValueError(msg)
        cuads.append(cuadruplo(len(cuads), act, arg1, None, res))
    else:
        msg = "ERROR: "+ID+" is not defined."
        raise ValueError(msg)

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
        print (jumps)

    global tempNum
    act = "gotoF"
    arg1 = getDirById(operands.pop())
    typ1 = types.pop()
    if(typ1 != "bool"):
        msg = "ERROR: Not a boolean expresion."
        raise ValueError(msg)
    cuads.append(cuadruplo(len(cuads), act, arg1, None, None))
    jumps.append(len(cuads)-1)

def p_ifQuad2(p):
    "ifQuad2 :"
    if StackDebuging:
        print (jumps)

    act = "goto"
    cuads.append(cuadruplo(len(cuads),act,None,None,None))
    # modify last goto
    idx = jumps.pop()
    cuads[idx].arg3 = len(cuads)

    jumps.append(len(cuads)-1)

def p_ifQuad3(p):
    "ifQuad3 :"
    if StackDebuging:
        print (jumps)
    act = "goto"
    idx = jumps.pop()
    cuads[idx].arg3 = len(cuads)


# invocacion -------------------------------------
def p_invocacion(p):
    """invocacion : pushPar reserved popPar
                  | ID eraQuad LPAR pushPar invo1 RPAR popPar gosubQuad"""
    p[0] = p[1]

def p_reserved(p):
    """reserved : SINFUNC LPAR expresion RPAR sinQuad
                | COSFUNC LPAR expresion RPAR cosQuad
                | PRINTFUNC LPAR expresion RPAR printQuad
                | POINTFUNC LPAR expresion COMA expresion RPAR pointQuad
                | CIRCLEFUNC LPAR expresion COMA expresion COMA expresion RPAR circleQuad
                | LINEFUNC LPAR expresion COMA expresion COMA expresion COMA expresion RPAR lineQuad
                | RECTFUNC LPAR expresion COMA expresion COMA expresion COMA expresion RPAR rectQuad"""
    p[0] = None

def p_invo1(p):
    """invo1 : expresion paramQuad invo2
            | empty"""
def p_invo2(p):
    """invo2 : COMA expresion paramQuad invo2
            | empty"""

paramNum = 1

def p_eraQuad(p):
    "eraQuad :"

    ID = p[-1]
    funcs = list(map(lambda x: x.id ,functions))
    if ID in funcs:
        act = "era"
        arg1 = p[-1]
        cuads.append(cuadruplo(len(cuads), act, arg1, None, None))
        global paramNum
        paramNum = 1
    else:
        msg = "ERROR: "+ID+" is not defined."
        raise ValueError(msg)


def p_paramQuad(p):
    "paramQuad :"
    global paramNum
    act = "param"
    arg1 = getDirById(operands.pop())
    typ1 = types.pop()
    arg3 = "param"+str(paramNum)
    paramNum += 1
    cuads.append(cuadruplo(len(cuads), act, arg1, None, arg3))

#TODO gosub
def p_gosubQuad(p):
    "gosubQuad :"
    act = "gosub"
    arg1 = p[-7]
    cuads.append(cuadruplo(len(cuads), act, arg1, None, None))
    global paramNum
    paramNum = 1

def p_sinQuad(p):
    "sinQuad :"
    global tempNum
    act = "sin"
    arg1 = getDirById(operands.pop())
    typ1 = types.pop()
    res = "t" + str(tempNum)
    resType = "float"
    newDir = getTemporalDir(resType)
    functions[scope].varTable.append(Var( res, resType, newDir))
    cuads.append(cuadruplo(len(cuads), act, arg1, None, newDir))
    operands.append(res)
    types.append(resType)
    tempNum += 1

def p_cosQuad(p):
    "cosQuad :"
    global tempNum
    act = "cos"
    arg1 = getDirById(operands.pop())
    typ1 = types.pop()
    res = "t" + str(tempNum)
    resType = "float"
    newDir = getTemporalDir(resType)
    functions[scope].varTable.append(Var( res, resType, newDir))
    cuads.append(cuadruplo(len(cuads), act, arg1, None, newDir))
    operands.append(res)
    types.append(resType)
    tempNum += 1

def p_printQuad(p):
    "printQuad :"
    act = "print"
    arg1 = getDirById(operands.pop())
    typ1 = types.pop()
    cuads.append(cuadruplo(len(cuads), act, arg1, None, None))

def p_pointQuad(p):
    "pointQuad :"
    act = "drawPoint"
    arg2 = getDirById(operands.pop())
    typ2 = types.pop()
    arg1 = getDirById(operands.pop())
    typ1 = types.pop()
    cuads.append(cuadruplo(len(cuads), act, arg1, arg2, None))

def p_circleQuad(p):
    "circleQuad :"
    act = "drawCircle"
    arg3 = getDirById(operands.pop())   # radius
    typ3 = types.pop()
    arg2 = getDirById(operands.pop())   # y position
    typ2 = types.pop()
    arg1 = getDirById(operands.pop())   # x position
    typ1 = types.pop()
    cuads.append(cuadruplo(len(cuads), act, arg1, arg2, arg3))

def p_lineQuad(p):
    "lineQuad :"
    arg4 = getDirById(operands.pop())   # to y position
    typ4 = types.pop()
    arg3 = getDirById(operands.pop())   # to x position
    typ3 = types.pop()
    arg2 = getDirById(operands.pop())   # from y position
    typ2 = types.pop()
    arg1 = getDirById(operands.pop())   # from x position
    typ1 = types.pop()
    act = "from"
    cuads.append(cuadruplo(len(cuads), act, arg1, arg2, None))
    act = "to"
    cuads.append(cuadruplo(len(cuads), act, arg3, arg4, None))

def p_rectQuad(p):
    "rectQuad :"
    arg4 = getDirById(operands.pop())   # second y position
    typ4 = types.pop()
    arg3 = getDirById(operands.pop())   # second x position
    typ3 = types.pop()
    arg2 = getDirById(operands.pop())   # y position
    typ2 = types.pop()
    arg1 = getDirById(operands.pop())   # x position
    typ1 = types.pop()
    act = "rect1"
    cuads.append(cuadruplo(len(cuads), act, arg1, arg2, None))
    act = "rect2"
    cuads.append(cuadruplo(len(cuads), act, arg3, arg4, None))

# ciclo ------------------------------------------
def p_ciclo(p):
    """ciclo : WHILE whileQuad1 LPAR expresion RPAR whileQuad2 bloque whileQuad3
            | DO bloque WHILE LPAR expresion RPAR SEMI
            | FOR LPAR ciclo1 SEMI expresion SEMI ciclo1 RPAR"""
def p_ciclo1(p):
    """ciclo1 : asignacion
            | empty"""
def p_whileQuad1(p):
    "whileQuad1 :"
    jumps.append(len(cuads))
def p_whileQuad2(p):
    "whileQuad2 :"
    act = "gotoF"
    arg1 = getDirById(operands.pop())
    typ1 = types.pop()
    jumps.append(len(cuads))
    cuads.append(cuadruplo(len(cuads),act, arg1, None, None))
def p_whileQuad3(p):
    "whileQuad3 :"
    act = "goto"
    idx = jumps.pop()
    arg3 = jumps.pop()
    cuads.append(cuadruplo(len(cuads),act, None, None, arg3))
    cuads[idx].arg3 = len(cuads)


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
                print (operators)
                print (operands)

            act = operators.pop()
            arg2 = getDirById(operands.pop())
            typ2 = types.pop()
            arg1 = getDirById(operands.pop())
            typ1 = types.pop()
            res = "t" + str(tempNum)
            resType = getCubeType(typ1,typ2,act)
            if(resType == Type.ERROR):
                msg = "ERROR: can't use "+act+" with "+typ1+" and "+typ2+"."
                raise ValueError(msg)
            newDir = getTemporalDir(resType)
            functions[scope].varTable.append(Var( res, resType, newDir))
            cuads.append(cuadruplo(len(cuads),act,arg1, arg2, newDir))
            operands.append(res)
            types.append(resType)
            tempNum += 1

# expresion relacional (<,>,==) -------------------------------------
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
                print (operators)
                print (operands)

            act = operators.pop()
            arg2 = getDirById(operands.pop())
            typ2 = types.pop()
            arg1 = getDirById(operands.pop())
            typ1 = types.pop()
            res = "t" + str(tempNum)
            resType = getCubeType(typ1,typ2,act)
            if(resType == Type.ERROR):
                msg = "ERROR: can't use "+act+" with "+typ1+" and "+typ2+"."
                raise ValueError(msg)
            newDir = getTemporalDir(resType)
            functions[scope].varTable.append(Var( res, resType, newDir))
            cuads.append(cuadruplo(len(cuads),act,arg1, arg2, newDir))
            operands.append(res)
            types.append(resType)
            tempNum += 1

# expresion aritmetica (+,-) --------------------------------------
def p_exp(p):
    "exp : term popExp exp1"

def p_popExp(p):
    "popExp :"
    global tempNum
    oper = ["+","-"]
    if len(operators) > 0:
        if  operators[-1] in oper:
            if StackDebuging:
                print (operators)
                print (operands)

            act = operators.pop()
            arg2 = getDirById(operands.pop())
            typ2 = types.pop()
            arg1 = getDirById(operands.pop())
            typ1 = types.pop()
            res = "t" + str(tempNum)
            resType = getCubeType(typ1,typ2,act)
            if(resType == Type.ERROR):
                msg = "ERROR: can't use "+act+" with "+typ1+" and "+typ2+"."
                raise ValueError(msg)
            newDir = getTemporalDir(resType)
            functions[scope].varTable.append(Var( res, resType, newDir))
            cuads.append(cuadruplo(len(cuads),act,arg1, arg2, newDir))
            operands.append(res)
            types.append(resType)
            tempNum += 1


def p_exp1(p):
    """exp1 : opexp exp
            | empty"""
def p_opexp(p):
    """opexp : SUB
            | SUM"""
    operators.append(p[1])
    #print operators

# term (*,/,%) -----------------------------------------------------------
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
                print (operators)
                print (operands)

            act = operators.pop()
            arg2 = getDirById(operands.pop())
            typ2 = types.pop()
            arg1 = getDirById(operands.pop())
            typ1 = types.pop()
            res = "t" + str(tempNum)
            resType = getCubeType(typ1,typ2,act)
            if(resType == Type.ERROR):
                msg = "ERROR: can't use "+act+" with "+typ1+" and "+typ2+"."
                raise ValueError(msg)
            newDir = getTemporalDir(resType)
            functions[scope].varTable.append(Var( res, resType, newDir))
            cuads.append(cuadruplo(len(cuads), act, arg1, arg2, newDir))
            operands.append(res)
            types.append(resType)
            tempNum += 1

def p_opterm(p):
    """opterm : MULT
            | DIV
            | MOD"""
    operators.append(p[1])

# factor (ids, Const, ())---------------------------------------------
def p_factor(p):
    "factor : opfactor fact1"

def p_fact1(p):
    """fact1 : ID pushID
             | INT pushIntType
             | FLOAT pushFloatType
             | BOOL pushBoolType
             | CHAR pushCharType
             | LPAR pushPar expresion RPAR popPar
             | invocacion funcQuad"""

def p_opfactor(p):
    """opfactor : SUB subQuad
            | empty"""

def p_pushID(p):
    "pushID :"
    ID = p[-1]

    #IDtype = getTypeById(ID)
    localVars = list(map(lambda x: x.id ,functions[scope].varTable))
    globalVars = list(map(lambda x: x.id ,functions[1].varTable))
    if ID in localVars:
        operands.append(ID)
        idx = localVars.index(ID)
        types.append(functions[scope].varTable[idx].type)
    elif ID in globalVars:
        operands.append(ID)
        idx = globalVars.index(ID)
        types.append(functions[1].varTable[idx].type)
    else:
        msg = "ERROR: "+p[-1]+" is not defined."
        raise ValueError(msg)

def p_pushIntType(p):
    "pushIntType :"
    types.append("int")
    operands.append(p[-1])
    global constIntVars
    functions[0].varTable.append(Var(p[-1], "int", 0+constIntVars))
    constIntVars += 1

def p_pushFloatType(p):
    "pushFloatType :"
    types.append("float")
    operands.append(p[-1])
    global constFloatVars
    functions[0].varTable.append(Var(p[-1], "float", 200+constFloatVars))
    constFloatVars += 1

def p_pushBoolType(p):
    "pushBoolType :"
    types.append("bool")
    operands.append(p[-1])
    global constBoolVars
    functions[0].varTable.append(Var(p[-1], "bool", 400+constBoolVars))
    constBoolVars += 1

def p_pushCharType(p):
    "pushCharType :"
    types.append("char")
    operands.append(p[-1])
    global constCharVars
    functions[0].varTable.append(Var(p[-1], "char", 600+constCharVars))
    constCharVars += 1

def p_pushPar(p):
    "pushPar :"
    operators.append("(")
    #print operators

def p_popPar(p):
    "popPar :"
    operators.pop()
    #print operators

def p_subQuad(p):
    "subQuad :"
    operators.append("*")
    operands.append("-1")
    types.append("int")

def p_funcQuad(p):
    "funcQuad :"
    ID = p[-1]
    # if the function has no name then it is a reserved function
    if (ID != None):
        global tempNum
        act = "="
        arg1 = ID
        res = "t" + str(tempNum)
        resType = getFunctionTypeById(ID)
        if(resType == "void"):
            msg = "ERROR: "+ID+" Function has no return value."
            raise ValueError(msg)
        cuads.append(cuadruplo(len(cuads), act, arg1, None, res))
        newDir = getTemporalDir(resType)
        functions[scope].varTable.append(Var( res, resType, newDir))
        operands.append(res)
        types.append(resType)
        tempNum += 1

# empty rule -----------------------------------------------------------
def p_empty(p):
    'empty :'
    pass

# parser end -----------------------------------------------------------

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

def getDir(varType):
    global scope
    if(scope == 1):
        global globalIntVars,globalFloatVars,globalBoolVars,globalCharVars
        if(varType == 'int'):
            newDir = 1000 + globalIntVars
            globalIntVars += 1
        elif(varType == 'float'):
            newDir = 1200 + globalFloatVars
            globalFloatVars += 1
        elif(varType == 'bool'):
            newDir = 1400 + globalBoolVars
            globalBoolVars += 1
        elif(varType == 'char'):
            newDir = 1600 + globalCharVars
            globalCharVars += 1
    else:
        global localIntVars,localFloatVars,localBoolVars,localCharVars
        if(varType == 'int'):
            newDir = 2000 + localIntVars
            localIntVars += 1
        elif(varType == 'float'):
            newDir = 3000 + localFloatVars
            localFloatVars += 1
        elif(varType == 'bool'):
            newDir = 4000 + localBoolVars
            localBoolVars += 1
        elif(varType == 'char'):
            newDir = 5000 + localCharVars
            localCharVars += 1
    return newDir

def getTemporalDir(varType):
    newDir = 0
    global temporalIntVars,temporalFloatVars,temporalBoolVars,temporalCharVars
    if(varType == 'int'):
        newDir = 6000 + temporalIntVars
        temporalIntVars += 1
    elif(varType == 'float'):
        newDir = 7000 + temporalFloatVars
        temporalFloatVars += 1
    elif(varType == 'bool'):
        newDir = 8000 + temporalBoolVars
        temporalBoolVars += 1
    elif(varType == 'char'):
        newDir = 9000 + temporalCharVars
        temporalCharVars += 1
    return newDir

def getFunctionTypeById(ID):
    functionNames = list(map(lambda x: x.id , functions))
    idx = functionNames.index(ID)
    if idx >= 0:
        return functions[idx].type

def getTypeById(ID):
    localVars = list(map(lambda x: x.id ,functions[scope].varTable))
    globalVars = list(map(lambda x: x.id ,functions[1].varTable))
    if ID in localVars:
        idx = localVars.index(ID)
        return functions[scope].varTable[idx].type
    elif ID in globalVars:
        idx = globalVars.index(ID)
        return functions[1].varTable[idx].type
    return False

def getDirById(ID):
    localVars = list(map(lambda x: x.id ,functions[scope].varTable))
    globalVars = list(map(lambda x: x.id ,functions[1].varTable))
    constVars = list(map(lambda x: x.id ,functions[0].varTable))
    if ID in localVars:
        idx = localVars.index(ID)
        return functions[scope].varTable[idx].dir
    elif ID in globalVars:
        idx = globalVars.index(ID)
        return functions[1].varTable[idx].dir
    elif ID in constVars:
        idx = constVars.index(ID)
        return functions[0].varTable[idx].dir
    return False

def resetVarCounters():
    global localIntVars, localFloatVars, localCharVars, localBoolVars
    global temporalIntVars, temporalFloatVars, temporalCharVars, temporalBoolVars

    localIntVars = 0
    localFloatVars = 0
    localCharVars = 0
    localBoolVars = 0

    temporalIntVars = 0
    temporalFloatVars = 0
    temporalCharVars = 0
    temporalBoolVars = 0

#list of functions that holds Func objects
functions = []
# list of cuad commands
cuads = []
# temporal directions counter
tempNum = 1
# current scope start in global scope
scope = 1
# stacks
jumps = []
operators = []
operands = []
types = []

constIntVars = 0
constFloatVars = 0
constCharVars = 0
constBoolVars = 0

globalIntVars = 0
globalFloatVars = 0
globalCharVars = 0
globalBoolVars = 0

localIntVars = 0
localFloatVars = 0
localCharVars = 0
localBoolVars = 0

temporalIntVars = 0
temporalFloatVars = 0
temporalCharVars = 0
temporalBoolVars = 0

# Initialize the function list with the default functions
functions.append(Func("const", "void", -1))
functions[0].varTable.append(Var("-1","int", 0))
constIntVars += 1
functions.append(Func("global", "void", -1))

# functions[1].varTable.append(Var("i", "int", -1))
# functions[1].varTable.append(Var("j", "int", -1))
# functions[1].varTable.append(Var("k", "int", -1))

readFile("testing\codigoPrueba.txt")

def printDirFunc():

    print ("\nDirectorio de funciones:")
    for i in range(0,len(functions)):
        print (str(functions[i]))
        for j in range(0, len(functions[i].varTable)):
            print("\t" + str(functions[i].varTable[j]))

    print ("\nQuadruplos:")
    for i in range(0, len(cuads)):
        print(str(cuads[i]))

    print (types)

printDirFunc()
mydirFunc = DirFunc()
mydirFunc.functions = functions
maquina = maquinaVirtual(mydirFunc,cuads)
#maquina.run(0,"END")
