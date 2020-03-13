from genome import *
"""Multiple tests taken from the debug datasets"""

def test_pattern_count_1():
	assert(pattern_count('GCGCG','GCG') == 2)

def test_pattern_count_2():
	assert(pattern_count('ACGTACGTACGT','CG') == 3)

def test_pattern_count_3():
	assert(pattern_count("""AAAGAGTGTCTGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAATTAAATTTTATTGAC
TTAGGTCACTAAATACTTTAACCAATATAGGCATAGCGCACAGACAGATAATAATTACAGAGTA
CACAACATCCAT""","AAA") == 4)

def test_pattern_count_4():
	assert(pattern_count("""AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTG
CATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGC
CGACTTT""","TTT") == 4)

def test_pattern_count_5():
	assert(pattern_count("GGACTTACTGACGTACG","ACT") == 2)

def test_pattern_count_6():
	assert(pattern_count("ATCCGATCCCATGCCCATG","CC") == 5)

def test_pattern_count_7():
	assert(pattern_count("""CTGTTTTTGATCCATGATATGTTATCTCTCCGTCATCAGAAGAACAGTGACGGATCGCCCTCTCTCTTGGTCAGGCGACCGTTTGCCATAATGCCCATGCTTTCCAGCCAGCTCTCAAACTCCGGTGACTCGCGCAGGTTGAGTA""","CTC") == 9)