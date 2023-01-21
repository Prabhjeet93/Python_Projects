import itertools

# combinations = list(itertools.permutations(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
# print(combinations)


combinations = list(itertools.combinations(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 2))
#print(combinations)

for i in combinations:
    print(i)