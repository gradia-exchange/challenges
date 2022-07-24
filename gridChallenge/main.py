from desmond import gridChallenge as gridChallengeDesmond
from prince import gridChallenge as gridChallengePrince
from david import gridChallenge as gridChallengeDavid
from moses import gridChallenge as gridChallengeMoses

grid1 = ['abc', 'ade', 'efg'],
grid2 = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'],
grid3 = ['zvfg', 'bcde', 'qyut']

functions = [gridChallengeDesmond, gridChallengePrince, gridChallengeDavid, gridChallengeMoses]
grids = [grid1, grid2, grid3]
results = ["YES", "YES", "NO"]

for gridFunction in functions:
    for grid, ordered in zip(grids, results):
        assert gridFunction(grid) == ordered
