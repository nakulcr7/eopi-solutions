def is_valid_sudoku(puzzle):
    """
    2D List -> Boolean
    Given: a 2D matrix that represents a partially completed sudoku puzzle
    Returns: True if the given puzzle is valid
    """

    def has_duplicates(array):
        """
        List -> Boolean
        Given: a list
        Returns: True iff the given list does not contain duplicates
        """
        array = [a for a in array if a != 0]
        return not(len(array) == len(set(array)))

    n = len(puzzle)

    # Row and Column constraints
    if any(
            has_duplicates([puzzle[i][j] for j in range(n)]) or
            has_duplicates([puzzle[j][i] for j in range(n)])
            for i in range(n)):
        return False

    # Region constraints
    region_size = sqrt(n)
    return all(not has_duplicates([
        puzzle[a][b]
        for a in range(region_size * I, region_size * (I + 1))
        for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))