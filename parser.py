import ply.lex as lex
import ply.yacc as yacc

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
t_GT = r'>'     #Greater Than
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
    print(t)
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
    "programa : prog init loop"

def p_prog(p):
    """prog : variable prog
            | funcion prog
            | empty"""

def p_init(p):
    #init(INT,INT)
    "init : INIT LPAR INT COMA INT RPAR bloque"

def p_loop(p):
    "loop : LOOP bloque"

def p_variable(p):
    "variable : tipo var SEMI"
def p_var(p):
    "var : ID arr var1 var2"
def p_var1(p):
    """var1 : EQ expresion
            | empty"""
def p_var2(p):
    """var2 : COMA var
            | empty"""
def p_arr(p):
    """arr : LBRACKET INT RBRACKET arr2
           | empty
       arr2 : LBRACKET INT RBRACKET
            | empty"""

def p_funcion(p):
    "funcion : tipo ID LPAR func1 RPAR bloque"
def p_func1(p):
    """func1 : func2
            | empty"""
def p_func2(p):
    "func2 : parametro func3"
def p_func3(p):
    """func3 : COMA func2
            | empty"""

def p_tipo(p):
    """tipo : TYPEVOID
            | TYPEINT
            | TYPEFLOAT
            | TYPEBOOL
            | TYPECHAR"""

def p_parametro(p):
    "parametro : tipo ID arr"

def p_bloque(p):
    "bloque : LBRACE bloq1 RBRACE"
def p_bloq1(p):
    """bloq1 : estatuto bloq1
            | empty"""
#TODO incluir declaracion de variable
def p_estatuto(p):
    """estatuto : asignacion
            | condicion
            | variable
            | invocacion
            | ciclo"""

def p_asignacion(p):
    "asignacion : ID arr EQ expresion SEMI"

def p_condicion(p):
    "condicion : IF LPAR expresion RPAR bloque cond1"
def p_cond1(p):
    """cond1 : ELSE bloque
            | empty"""

def p_invocacion(p):
    "invocacion : ID LPAR invo1 RPAR SEMI"
def p_invo1(p):
    """invo1 : expresion invo2
            | empty"""
def p_invo2(p):
    """invo2 : COMA expresion invo2
            | empty"""

def p_ciclo(p):
    """ciclo : WHILE LPAR expresion RPAR bloque
            | DO bloque WHILE LPAR expresion RPAR SEMI
            | FOR LPAR ciclo1 SEMI expresion SEMI ciclo1 RPAR"""
def p_ciclo1(p):
    """ciclo1 : asignacion
            | empty"""

def p_expresion(p):
    "expresion : not expbool bin"
def p_not(p):
    """not : NOT
            | empty"""
def p_bin(p):
    """bin : opbin expresion
            | empty"""
def p_opbin(p):
    """opbin : AND
            | OR"""

def p_expbool(p):
    "expbool : exp expbool1"
def p_expbool1(p):
    """expbool1 : opbool exp
            | empty"""
def p_opbool(p):
    """opbool : LT
            | GT
            | LET
            | GET
            | EQT
            | NEQT"""

def p_exp(p):
    "exp : term exp1"
def p_exp1(p):
    """exp1 : opexp exp
            | empty"""
def p_opexp(p):
    """opexp : SUB
            | SUM"""

def p_term(p):
    "term : factor term1"
def p_term1(p):
    """term1 : opterm term
            | empty"""
def p_opterm(p):
    """opterm : MULT
            | DIV
            | MOD"""

def p_factor(p):
    "factor : opfactor fact1"
def p_fact1(p):
    """fact1 : ID
            | INT
            | FLOAT
            | BOOL
            | CHAR
            | LPAR expresion RPAR
            | invocacion"""
def p_opfactor(p):
    """opfactor : SUM
            | SUB
            | empty"""

def p_empty(p):
    'empty :'
    pass

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


readFile("codigoPrueba.txt")
