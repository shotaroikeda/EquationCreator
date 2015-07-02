import gene
import numpy as np

MAX_GENE_POOL = 50

#################################################
# Call these functions! For simplified usage... #
#################################################

def start():
    return superfast()

def add(g_array, g_new, initial_num=42):
    f_val = single_fit(g_new, initial_num)
    if len(g_array) > MAX_GENE_POOL:
        g_array.pop(0)
    bsearch_fit(g_array, g_new, f_val)

def initial_scan(g_array):
    for g, f in g_array:
        if f == 1:
            return g, f
    return None

def reproduce(g_array, rrep=0.7, rmut=0.0001):
    c1, c2 = weighted_choice_new(g_array)
    rand = np.random.randint(0, len(c1)+1)
    ng1, ng2 = gene.reproduce(c1, c2, rand, rrep, rmut)

    return ng1, ng2


################################################################
# Functions that are a little more complicated. Some are still #
# prototype functions that are not used.                       #
################################################################

def create_initial_population():
    return [gene.generate() for i in range(0, 20)]

def generate_fitness(gene_array, initial_num=42):
    return [float((0.00001 / (0.00001 +
                          abs(initial_num - gene.evaluate(g)))))
            for g in gene_array]

def single_fit(g, initial_num=42):
    return float((1.0 / (1.0 +
                         abs(initial_num - gene.evaluate(g)))))

def superfast():
    a = create_initial_population()
    b = generate_fitness(a)
    return sorted(list(zip(a, b)), key=lambda x : x[1])

def test_roll():
    return generate_fitness(create_initial_population())

def get_probability(num, total):
    return float(num / total)

def weighted_choice_new(g_array):
    b = zip(*g_array)
    return weighted_choice(b[0], b[1])

def weighted_choice(gene_array, fitness_array):
    fix = np.vectorize(get_probability)
    draw1, draw2 = np.random.choice(gene_array,
                                    2,
                                    replace=False,
                                    p=fix(fitness_array, sum(fitness_array)))
    return (draw1, draw2)

def bsearch_fit(a_like, new_gene, new_fitness):
    n = bsearch_rec(a_like, 0 ,len(a_like), new_fitness)
    a_like.insert(n, (new_gene, new_fitness))

def bsearch_rec(g_array, lo, hi, new_fitness):
    mid = (lo + hi) / 2

    if mid <= lo:
        if g_array[lo][1] > new_fitness:
            return lo
        else:
            return lo+1

    # if g_array[mid][1] == new_fitness:
    #     return mid + 1
    if g_array[mid][1] > new_fitness:
        return bsearch_rec(g_array, lo, mid, new_fitness)
    else:
        return bsearch_rec(g_array, mid, hi, new_fitness)

def test(g_array, lo, hi, new_fitness):
    mid = (lo + hi) / 2

    if mid <= lo:
        if g_array[lo] > new_fitness:
            return lo
        else:
            return lo+1

    # if g_array[mid][1] == new_fitness:
    #     return mid + 1
    if g_array[mid] > new_fitness:
        return test(g_array, lo, mid, new_fitness)
    else:
        return test(g_array, mid, hi, new_fitness)
