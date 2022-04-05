#!/usr/bin/python3

import random
from collections import OrderedDict
from datetime import date

# generate wide variety of birth/death dates and the ages of a population
# placed in a separate program to increase speed of gen_people.py

# date object used to help manage writing date information
class Date:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    def __repr__(self):        
        return f'{self.month}/{self.date}/{self.year}'

class LifeInfo:
    def __init__(self, dob, age, dod):
        self.dob = dob
        self.age = age
        self.dod = dod if dod is not None else "NULL"
    
    def __repr__(self):
        return f'{self.dob},{self.age},{self.dod}'

# death rates
D_POP_SIZE = 100_000
death_rates = {
    ((603+500)/2)/D_POP_SIZE: 0,
    ((25+21)/2)/D_POP_SIZE: [1, 4],
    ((15+11)/2)/D_POP_SIZE: [5, 14],
    ((99+38)/2)/D_POP_SIZE: [15, 24],
    ((177+78)/2)/D_POP_SIZE: [25, 34],
    ((257+141)/2)/D_POP_SIZE: [35, 44],
    ((490+297)/2)/D_POP_SIZE: [45, 54],
    ((1111+669)/2)/D_POP_SIZE: [55, 64],
    ((2178+1402)/2)/D_POP_SIZE: [65, 74],
    ((5074+3710)/2)/D_POP_SIZE: [75, 84],
    ((12229+10666)/2)/D_POP_SIZE: [85, 95],
    ((7000+6000)/2)/D_POP_SIZE: [95, 105],
    ((1000+500)/2)/D_POP_SIZE: [105, 115]
}
death_rates = OrderedDict(sorted(death_rates.items(), key=lambda x: x[0]))

base_date = date.today()
b_month, b_day, b_year = base_date.month, base_date.day, base_date.year


# get a date of birth for an individual
def get_random_date():
    month = int(random.random() * 12) + 1
    year = int(random.random() * (b_year-1900)) + 1900

    # 31 days
    if month in [1, 3, 5, 7, 8, 10, 12]:
        date = int(random.random() * 31) + 1
    # February
    elif month == 2:
        date = int(random.random() * 28) + 1
    # 30 days
    else:
        date = int(random.random() * 30) + 1
    
    return Date(date, month, year)

# generate the date of birth, the age, and possibly the date of death of an individual
def gen_dates():
    # get a random probability and start printing likely death ages
    # of individuals in a population set
    prob = random.uniform(0, 1)
    dob = get_random_date()
    age_range = []
    for key, value in death_rates.items():
        if prob > key:
            age_range = value

    if age_range == 0 or age_range == []:
        e_age = 0
    else:
        # e_age = random.randint(age_range[0], age_range[1])
        e_age = int(random.random() * (age_range[1]-age_range[0]+1)) * age_range[0]

    if b_year - dob.year <= e_age:
        while b_year - int(dob.year) <= e_age:
            e_age -= 1
        
    # adjust age if required (base date -- March 28, 2022 )
    if dob.month < b_month or (dob.month == b_month and dob.date <= b_day):
        e_age += 1

    # calculate date of death (if applicable)
    if ((dob.year + e_age < b_year) and (dob.month < b_month or (dob.month == b_month and dob.date < b_day))) \
        or dob.year + e_age < b_year-1:
        # person is dead, generate random date of death
        years_of_death = [dob.year + e_age, dob.year + e_age + 1]
        
        # generate random date (ignore the year for now)
        dod = get_random_date()
        if dod.month > dob.month or (dod.month == dob.month and dod.date > dob.date):
            # we are PAST a birthday, meaning year of death is index 1
            dod.year = years_of_death[0]
        else:
            # we are BEFORE a birthday, meaning year of death is index 2
            dod.year = years_of_death[1]
    # death could not be found
    else:
        dod = None    
    return (dob, e_age, dod)

def main():
    with open('./upload/data/dates.dat', 'w') as f:
        for _ in range(1_000_000):
            dob, age, dod = gen_dates()
            f.write(f'{LifeInfo(dob, age, dod)}\n')

def test():
    with open('./upload/data/dates.dat') as f:
        data = [x.rstrip().split(',') for x in f]
    
    for d in data:
        b_month, b_date, b_year = tuple(d[0].split('/'))
        if d[2] != "NULL":
            d_month, d_date, d_year = tuple(d[2].split('/'))
        
        print(
            LifeInfo(
                Date(b_date, b_month, b_year),
                int(d[1]),
                Date(d_month, d_date, d_year) if d[2] != "NULL" else None
            )
        )

# quick test to read dates
if __name__ == "__main__":
    main()