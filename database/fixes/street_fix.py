#!/usr/bin/python3

# fix all street names to be in capitalized state

streets = []
with open('../data/street_names.dat') as f:
    for street in f:
        caps = True
        build = ''
        for c in street:
            if c.isalpha() and not caps:
                # is a letter
                build += c.lower()
            elif c == ' ':
                caps = True
                build += c
            else:
                caps = False
                build += c
        streets.append(build[:-1])

for street in streets:
    print(street)