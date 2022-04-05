#!/usr/bin/python3

# fix the original last names list to put all names into capitalized state

names = []
with open('../data/last_names.dat') as f:
    names = [name.rstrip().captalize() for name in f]
    
with open('../last_names.dat', 'w') as f:
    for name in names:
        f.write(f'{name}\n')