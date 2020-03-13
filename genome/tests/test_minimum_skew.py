from genome import *

def test_min_skew_1():
	genome = Genome('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')
	assert(set(genome.minimum_skew()) == set([11,24]))

def test_min_skew_2():
	genome = Genome('ACCG')
	assert(set(genome.minimum_skew()) == set([3]))

def test_min_skew_3():
	genome = Genome('ACCC')
	assert(set(genome.minimum_skew()) == set([4]))

def test_min_skew_4():
	genome = Genome('CCGGGT')
	assert(set(genome.minimum_skew()) == set([2]))

def test_min_skew_5():
	genome = Genome('CCGGCCGG')
	assert(set(genome.minimum_skew()) == set([2,6]))