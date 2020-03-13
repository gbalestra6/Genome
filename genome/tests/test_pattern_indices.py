from genome import *

def test_pattern_indices_1():
	assert(set(pattern_indices("ATAT","GATATATGCATATACTT")) == set([1,3,9]))

def test_pattern_indices_2():
	assert(set(pattern_indices("ACAC","TTTTACACTTTTTTGTGTAAAAA")) == set([4]))

def test_pattern_indices_3():
	assert(set(pattern_indices("AAA","""AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGACTTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTACACAACATCCAT""")) == set([0,46,51,74]))

def test_pattern_indices_4():
	assert(set(pattern_indices("TTT","""AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT""")) == set([88,92,98,132]))

def test_pattern_indices_5():
	assert(set(pattern_indices("ATA","ATATATA")) == set([0,2,4]))