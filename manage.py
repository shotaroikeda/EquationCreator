import gene
import numpy as np


CHANCE_UNFIT = 0.0000001  # The default fitness a completely bad gene has

def initialize():
    return [gene.generate() for i in range(0, 20)]

def generate_fitness(gene_array, initial_num=42):
    return [float((1.0 / (1.0 +
                          abs(initial_num - gene.evaluate(g, True)))))
            for g in gene_array]

def superfast():
    a = initialize()
    b = generate_fitness(a)
    return sorted(list(zip(a, b)), key=lambda x : x[1])

def test_roll():
    return generate_fitness(initialize())

def get_probability(num, total):
    return float(num / total)

def weighted_choice(gene_array, fitness_array):
    fix = np.vectorize(get_probability)
    draw1, draw2 = np.random.choice(gene_array,
                                    2,
                                    replace=False,
                                    p=fix(fitness_array, sum(fitness_array)))
    return (draw1, draw2)

def f():
    a = initialize()
    b = generate_fitness(a)

    print weighted_choice(a, b)

