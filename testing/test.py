import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'AND',
    'OR',
    'INT',
    'STRING',
    'FLOAT',
    'ID'
]

literals = [
    '=',
    '*',
    '/',
    '+',
    '-',
    '(',
    ')',
    '<',
    '>',
    ';'
]

reserved = {
  'sin' : 'SINFUNC',
  'int' : 'TYPEINT'
}

tokens += reserved.values()

t_AND = r'&&'
t_OR = r'\|\|'
t_INT = r'[\+,-]?\d+'
t_FLOAT = r'[+,-]?[0-9]+\.[0-9]+((E|e)[+,-]?[0-9]+)?'
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
#inicio de parser
def p_init(p):
    "init : par"
    print("valid")
def p_par(p):
    """par : '(' par ')'
            | '(' par ')' par
            | empty"""
def p_empty(p):
    "empty :"
    pass
#Es llamado cuando sucede un error en el parser
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Crea el parser dandole el estado inicial
parser = yacc.yacc(start = 'init')

def readFile(file):
    file_in = open(file, 'r')
    data = file_in.read()
    file_in.close()
    parser.parse(data)

readFile("test.txt")
