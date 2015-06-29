from gene import *

CHANCE_UNFIT = 0.0000001  # The default fitness a completely bad gene has

def initialize():
    return [generate() for i in range(0, 20)]

def generate_fitness(gene_array, initial_num = 42):
    return [float(5.0 / (5.0 + abs(initial_num - eval(evaluate(g, True))))) for g in gene_array]

def test_roll():
    return generate_fitness(initialize())
