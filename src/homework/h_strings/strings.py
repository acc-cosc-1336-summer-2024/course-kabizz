def get_hamming_distance(dna1, dna2):
    return sum(c1 != c2 for c1, c2 in zip(dna1, dna2))

def get_dna_complement(base):
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return complements.get(base, base)  # return the complement 

def reverse_dna_sequence(sequence):
    return sequence[::-1]  # return the reversed sequence

def complement_sequence(dna_sequence):
    complemented_sequence = ''.join(get_dna_complement(base) for base in dna_sequence)
    return complemented_sequence