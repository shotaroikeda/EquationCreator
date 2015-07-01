##############################################################
# Everything that has to do with simple single genes will be #
# in here. Otherwise it will belong in manage.py             #
##############################################################


import random

_GENE_ENCODING_DICT = {
    "0000" : '0',
    "0001" : '1',
    "0010" : '2',
    "0011" : '3',
    "0100" : '4',
    "0101" : '5',
    "0110" : '6',
    "0111" : '7',
    "1000" : '8',
    "1001" : '9',
    "1010" : '+',
    "1011" : '-',
    "1100" : '*',
    "1101" : '/',
    "1110" : None,
    "1111" : None
}

_GENE_LENGTH = 4

def generate(num_digit=9):
    """
    Generates a gene to be used.
    A list of strings with 0 and 1 will be created.
    num_digit defines how large the pattern will be.

    """
    return "".join([str(random.randint(0, 1)) for n in range(0, num_digit*_GENE_LENGTH)])

def peek_gene(gene_str):
    """
    Allows you to see what kind of gene the gene_list is.
    Also peek_gene()[1] returns if the equation contains invalid bits.

    Ex.
    ("1+2 n/a /3", False)
    """
    result = ""
    flg = True
    for n in range(0, len(gene_str) / _GENE_LENGTH):
        if n is 0:
            continue
        
        char = _GENE_ENCODING_DICT.get(
            gene_str[(n-1) * _GENE_LENGTH : n * _GENE_LENGTH])

        if char:
            result += char
        else:
            result += ' '
            flg = False

    return (result, flg)

def validate_gene(gene_str):
    """Validates the gene to make it can be evaluated"""
    OPERATOR = list("*/-+")

    a = peek_gene(gene_str)

    if not a[1]:
        return False

    for n in range(0, len(a[0])):
        if n % 2 == 0:
            if a[0][n] not in OPERATOR:
                return False

        else:
            if a[0][n] in OPERATOR:
                return False

    return True

def evaluate_old_unused(gene_str, v=False):
    if v:
        print "Gene Looks like: %s" % peek_gene(gene_str)[0]

    if validate_gene(gene_str):
        if v:
            print "Valid Gene! Calculating..."

        return eval(gene_str)

def evaluate(gene_str, v=False):
    OPERATOR = list("*/-+")
    NUMBER = list("0123456789")

    gene_str = list(peek_gene(gene_str)[0])
    tggl = True

    final = ""
    for n in range(0, len(gene_str)):
        if tggl:
            if gene_str[n] in NUMBER:
                final += gene_str[n]
                tggl = False

        else:
            if gene_str[n] in OPERATOR:
                final += gene_str[n]
                tggl = True

    if len(final) > 0 and list(final)[-1] in OPERATOR:
        final = final[:-1]

    if v:
        print "Equation: %s" % final

    try:
        if v:
            print "Evaluates to: %d" % eval(final)
        return int(eval(final))
    except ZeroDivisionError:
        return -1000
