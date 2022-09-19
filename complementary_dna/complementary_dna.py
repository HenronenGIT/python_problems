# In DNA strings, symbols "A" and "T" are complements of each other, 
# as "C" and "G". Your function receives one side of the DNA 
# (string, except for Haskell); you need to return the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"

def DNA_strand(dna):
	str = dna.translate(dna.maketrans("ATCG", "TAGC"))
	# print (str)
	return (str)

assert(DNA_strand("AAAA") == "TTTT")
assert(DNA_strand("ATTGC") == "TAACG")
assert(DNA_strand("GTAT") == "CATA")
assert(DNA_strand("AAGG") == "TTCC")
assert(DNA_strand("CGCG") == "GCGC")
assert(DNA_strand("ATTGC") == "TAACG")
assert(DNA_strand("GTATCGATCGATCGATCGATTATATTTTCGACGAGATTTAAATATATATATATACGAGAGAATACAGATAGACAGATTA") == "CATAGCTAGCTAGCTAGCTAATATAAAAGCTGCTCTAAATTTATATATATATATGCTCTCTTATGTCTATCTGTCTAAT")
        