import ply.yacc as yacc
from analizadorLexico import tokens

'''
expresion   : expresion + termino
            | expresion - termino
            | expresion == termino
            | termino
            
termino     : termino * factor
            | termino / factor
            | factor

factor      : NUMERO
            | (expresion)
'''

def p_expresion_suma(p):
    '''expresion : expresion SUMA termino'''
    p[0] = p[1] + p[3]
    p[0] = print('La función de SUMA es correcta.')
    
def p_expresion_resta(p):
    '''expresion : expresion RESTA termino'''
    p[0] = p[1] - p[3]
    p[0] = print('La función de RESTA es correcta.')

def p_expresion_igual_que(p):
    'expresion : expresion IGUAL_QUE termino'
    p[0] = p[1] == p[3]

def p_termino_multiplicacion(p):
    'termino : termino MULTIPLICACION factor'
    p[0] = p[1] * p[3]

def p_termino_division(p):
    'termino : termino DIVISION factor'
    p[0] = p[1] / p[3]

def p_termino_factor(p):
    '''termino : factor'''
    p[0] = p[1]

def p_factor_NUMERO(p):
    '''factor : NUMERO'''
    p[0] = p[1]

def p_factor_parentesis(p):
    'factor : PARENTESIS_IZQ expresion PARENTESIS_DER'
    p[0] = p[2]

def p_error(p):
    print('ERROR DE SINTAXIS: ')

parser = yacc.yacc()

while True:
    try:
        entrada = input('> ')
    except EOFError:
        break
    
    if entrada == 'exit':
        break
    if not entrada:
        continue

    resultado = parser.parse(entrada)
    print(resultado)
