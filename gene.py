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
            result += " n/a "
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

def evaluate(gene_str):
    if validate_gene(gene_str):
        return eval(gene_str)