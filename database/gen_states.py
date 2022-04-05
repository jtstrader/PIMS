#!/usr/bin/python3
from string import ascii_uppercase

# create every possible permutation for a state in uppercase letters (no two letters will be the same in a state abbr.)
with open('./data/states.dat', 'w') as f:
    count = 0
    for c1 in ascii_uppercase:
        for c2 in ascii_uppercase:
            if c1 != c2:
                if count < 250:
                    f.write(f'{c1}{c2}\n')
                    count += 1