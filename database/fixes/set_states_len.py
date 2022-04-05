#!/usr/bin/python3

import random
random.seed()

# set the length of the states file to 250 elements to account for 500 companies
# this is so the dataset can have 2 companies per state

# read data first
with open('../data/states.dat') as f:
    states = [x.rstrip() for x in f]

while len(states) > 250:
    rm = random.randint(0, len(states)-1)
    del states[rm]

# write out data
with open('../data/states.dat', 'w') as f:
    for state in states:
        f.write(f'{state}\n')