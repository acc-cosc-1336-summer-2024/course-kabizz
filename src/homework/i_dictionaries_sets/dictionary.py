def get_p_distance(s1, s2):
    """
    Calculate the p-distance between two DNA sequences s1 and s2.
    """
    differing_positions = 0
    length = len(s1)
    
    for i in range(length):
        if s1[i] != s2[i]:
            differing_positions += 1
    
    p_distance = differing_positions / length
    return p_distance

def get_p_distance_matrix(strings):
    """
    Compute the p-distance matrix for a list of DNA sequences.
    """
    n = len(strings)
    distance_matrix = [[0.0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            p_distance = get_p_distance(strings[i], strings[j])
            distance_matrix[i][j] = p_distance
            distance_matrix[j][i] = p_distance
    
    return distance_matrix

if __name__ == "__main__":
    # Sample input
    dna_strings = [
        ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
        ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],
        ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],
        ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
    ]

    # Compute distance matrix
    distance_matrix = get_p_distance_matrix(dna_strings)

    # Print the distance matrix with the required formatting
    for row in distance_matrix:
        print(' '.join(f'{dist:.5f}' for dist in row))

