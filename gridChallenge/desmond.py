def gridChallenge(grid: list) -> str:
    """
    Returns YES if grid when ordered rows are arranged alphabetically and columns also arranged alphabetically. 
    Returns NO otherwise
    Alorithm
    --------
    n(C) = length of each word in the grid
    r = element of the grid (row)
    1. sort each row in the grid (make it alphabetically ordered).
    2. ordered = "YES"
    2. do while i = 0 and n < n(C)
            foreach r, get the ith element and compare with the next element i+1th element 
                if (i+1)th element is greater than the ith element
                    ordered = "NO"
                    break
        return ordered
    :param grid:
    :returns:
    """
    sorted_rows_grid = ["".join(sorted(row)) for row in grid]
    ordered = "YES"
    row_count = len(sorted_rows_grid[0])   # although this was given in the input
    for i in range(row_count):
        for index in range(len(sorted_rows_grid)-1):
            row1 = sorted_rows_grid[index]
            row2 = sorted_rows_grid[index+1]
            if row1[i] > row2[i]:
                ordered = "NO"
                break

    return ordered


if __name__ == "__main__":
    # Do your personal testing here and call your function
    grid1 = ['abc', 'ade', 'efg']
    grid2 = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    grid3 = ['zvfg', 'bcde', 'qyut']
    print("Grid 1:", gridChallenge(grid1))
    print("Grid 2:", gridChallenge(grid2))
    print("Grid 3:", gridChallenge(grid3))