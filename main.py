#!/usr/bin/python

import manage
import gene
import os
from sys import argv

P_VERSION = "1.0"

FILE_OUT = "output.txt"
MUTATION_RATE = 0.15
REPRODUCTION_RATE = 0.7
# MAX_GENE_POOL is set in manage.py <- bad design...

argv.pop(0)

for index, arg in enumerate(argv):
    if arg == '-f':
        FILE_OUT = argv[index+1]
    elif arg == '-M':
        try:
            m = float(argv[index+1])
            if m < 0 or m > 1:
                raise ValueError('dummy error')
            MUTATION_RATE = m
        except ValueError:
            print "No valid Mutation Rate, proceeding with default...(%10.5f)" % (
                MUTATION_RATE)
    elif arg == '-R':
        try:
            r = float(argv[index+1])
            if r < 0 or r > 1:
                raise ValueError('dummy error')
            REPRODUCTION_RATE = r
        except ValueError:
            print "No valid Reproduction Rate, proceeding with default...(%10.5f)" % (
                REPRODUCTION_RATE)
    elif arg == '--help' or arg == '-h':
        print "EquationCreator %s:" % (P_VERSION)
        print "Creates an equation which equates to a given number."
        print "Usage:"
        print "./main.py <args> <arg value>"
        print "<args>:"
        print "\t-f: Set the output file. Default is output.txt"
        print "\t-M: Set the Mutation Rate. Default is %0.5f" % (MUTATION_RATE)
        print "\t-R: Set the Reproduction Rate. Default is %0.5f" % (
            REPRODUCTION_RATE)
        exit()

FINAL_NUMBER = 42

#try:
#    a = int(raw_input("Please Enter a Natural Number (0 <= n ) : "))
#    
#    if a < 0:
#        raise ValueError("Invalid Input. Please Enter a number greater than 0")
#
#except ValueError:
#    print "bad input, defaulting to 42"

# TODO: set the userinput number to whatever they choose

f = open(FILE_OUT, "w")
generation = 0

gene_pool = manage.start()

if manage.initial_scan(gene_pool):
    print "Found a solution!"
    print "That wasn't that interesting though...try again..."
    exit()

prev_gene = ""

while not gene_pool[-1][1] == 1:
    f.write("\nGENERATION: %d\n" % (generation))
    for g, fit in gene_pool:
        f.write("%s  %1.8f  %s\n" % (g, fit, gene.show_eq(g)))

    if not (prev_gene == gene_pool[-1][0]):
        os.system('clear')
        print "GENERATION: %d\n" % (generation)
        print "Best Gene\n\t - Fitness: %1.5f\n" % (gene_pool[-1][1])
        print "\t - Value: %d\n" % (gene.evaluate(gene_pool[-1][0]))
        for g, fit in gene_pool:
            print "%s  %1.8f  %s" % (g, fit, gene.show_eq(g))

    ng1, ng2 = manage.reproduce(gene_pool, REPRODUCTION_RATE, MUTATION_RATE)
    manage.add(gene_pool, ng1, FINAL_NUMBER)
    manage.add(gene_pool, ng2, FINAL_NUMBER)

    generation += 1
    prev_gene = gene_pool[-1][1]


f.write("\nGENERATION: %d\n" % (generation))
for g, fit in gene_pool:
    f.write("%s  %1.8f  %s\n" % (g, fit, gene.show_eq(g)))
f.write("\nSolved!\n")
f.write("Took %d generations\n" % (generation))
f.write("Final Gene: %s\n" % (gene_pool[-1][0]))
f.write("Equation: %s\n" % (gene.show_eq(gene_pool[-1][0])))

os.system('clear')
print "GENERATION: %d\n" % (generation)
print "Best Gene\n\t - Fitness: %1.5f\n" % (gene_pool[-1][1])
print "\t - Value: %d\n" % (gene.evaluate(gene_pool[-1][0]))
for n, gfit in enumerate(gene_pool):
    g, fit = gfit
    print "%4d  %s  %1.8f  %s" % (n, g, fit, gene.show_eq(g))

