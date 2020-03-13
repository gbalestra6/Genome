from genome import *

def test_clump_finder_1():
	assert(set(clump_finder("""CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA""",5,50,4)) == set(["CGACA","GAAGA"]))

def test_clump_finder_2():
	assert(set(clump_finder("AAAACGTCGAAAAA",2,4,2)) == set(["AA"]))

def test_clump_finder_3():
	assert(set(clump_finder("ACGTACGT",1,5,2)) == set(["A","C","G","T"]))

def test_clump_finder_4():
	assert(set(clump_finder("""CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG""",3,25,3)) == set(["AAA","CAG","CAT","CCA","GCC","TTC"]))