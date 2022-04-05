#!/usr/bin/python3
from asyncore import write
from os import lstat
from collections import OrderedDict
from functools import total_ordering
import random
import pickle

# generate list of random people to be put into the database


# address of the individual
class Address:
    def __init__(self, address_1, address_2, city, state, zip):
        self.address_1 = address_1
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zip = zip
    
    def csv_out(self):
        return f'{self.address_1},{self.address_2},{self.city},{self.state},{self.zip},'

    def __repr__(self):
        return f'{self.address_1:<40}{self.address_2:<40}{self.city:<40}{self.state:<6}{self.zip:<10}'

# date object used to help manage writing date information
@total_ordering
class Date:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year
    
    # read in query format and parse that way
    @classmethod
    def query_init(self, qry_str):
        self.date = qry_str[6:]
        self.month = qry_str[4:6]
        self.year = qry_str[0:4]
    
    def __eq__(self, other):
        return self.date == other.date and self.month == other.month and self.year == other.year
    
    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        elif self.month > other.month:
            return True
        elif self.month < other.month:
            return False
        elif self.date > other.date:
            return True
        else:
            return False

    # Query Format: YYYYMMDD
    def csv_out(self):
        return f'{self.year}{self.month}{self.date}'

    def __repr__(self):
        out = (
            f'{f"0{self.month}" if self.month < 10 else str(self.month)}/'
            f'{f"0{self.date}" if self.date < 10 else str(self.date)}/'
            f'{str(self.year)}'
        )
        return f'{out:<18}'

# object used in the population list below
class Person:
    def __init__(self, ssn, first, last, sex, dob, age, dod, address, partner_ssn):
        self.ssn = ssn
        self.first = first
        self.last = last
        self.sex = "M" if sex == "B" or sex == "M" else "F"
        self.dob = dob
        self.age = age
        self.dod = dod
        self.address = address
        self.partner_ssn = partner_ssn

    def csv_out(self):
        if self.dod is not None:
            dod_out = "NULL"
        else:
            dod_out = self.dod.csv_out()
        return f'{self.ssn},{self.first},{self.last},{self.sex},{self.dob.csv_out()},{self.age},{dod_out},{self.address.csv_out()},{self.partner_ssn},'

    def __repr__(self):
        if self.dod is None:
            self.dod = f'{"NULL":<18}'
        return f'{self.ssn:<15}{self.first:<20}{self.last:<20}{self.sex:<5}{self.dob}{self.age:<11}{self.dod}{self.address}{self.partner_ssn:<15}' 

random.seed() # init random number generator

# create a population set of 1_000_000 individuals using provided file information and RNG
def main():
    first_names, last_names, ssn = get_first_last_names_and_ssn()
    streets, cities, states = get_address_values()
    dobs, ages, dods = get_dates()
    population = create_population(ssn, first_names, last_names, dobs, ages, dods, streets, cities, states)

    # set marriage status for each individual (if applicable)
    set_married(population)
    write_population(population)
    write_population_pickle(population)

# get first and last name lists from the files
def get_first_last_names_and_ssn():
    with open('./data/first_names.dat') as f:
        first_names = [name.split(',') for name in f]
    with open('./data/last_names.dat') as f:
            last_names = [name for name in f]
    with open('./data/ssn.dat') as f:
            ssn = [n for n in f]
    return (first_names, last_names, ssn)

# read from files and get relevant address information
def get_address_values():
    with open('./data/street.dat') as f:
        streets = [street.rstrip() for street in f]
    with open('./data/cities.dat') as f:
        cities = [city.rstrip() for city in f]
    with open('./data/states.dat') as f:
        states = [state.rstrip() for state in f]
    return (streets, cities, states)

# read from file and get all date info
def get_dates():
    with open('./data/dates.dat') as f:
        data = [x.rstrip().split(',') for x in f]
    
    dobs = []
    ages = []
    dods = []

    # parse through saved data and break up MM/DD/YYYY into date data
    for d in data:
        b_month, b_date, b_year = tuple(d[0].split('/'))
        if d[2] != "NULL":
            d_month, d_date, d_year = tuple(d[2].split('/'))
    
        dobs.append(Date(int(b_date), int(b_month), int(b_year)))
        ages.append(int(d[1]))
        dods.append(Date(int(d_date), int(d_month), int(d_year)) if d[2] != "NULL" else None)
    
    return (dobs, ages, dods)

# create the population list -- 1_000_000 people
def create_population(ssn, first_names, last_names, dobs, ages, dods, streets, cities, states):
    population = []
    for i in range(1_000_000):
        first_name_idx = random.randint(0, len(first_names)-1)
        last_name_idx = random.randint(0, len(last_names)-1)

        # check for homelessness
        if random.uniform(0, 1) > 0.0017:
            streets_1_idx = random.randint(0, len(streets)-1)
            streets_2_idx = random.randint(0, len(streets)-1)
            city_idx = random.randint(0, len(cities)-1)
            state_idx = random.randint(0, len(states)-1)
            
            chance = random.randint(0, 10) # if a 3 or lower, get the second address

            population.append(
                Person(ssn[i].rstrip(), first_names[first_name_idx][1].rstrip(), last_names[last_name_idx].rstrip(), first_names[first_name_idx][0], dobs[i], ages[i], dods[i],
                Address(f'{random.randint(1, 1000)} {streets[streets_1_idx]}', f'{random.randint(1, 1000)} {streets[streets_2_idx]}' if chance <= 3 else "NULL", cities[city_idx], states[state_idx], random.randint(10000, 99999)), '000-00-0000'),
            )
        # person is homeless
        else:
            population.append(
                Person(ssn[i].rstrip(), first_names[first_name_idx][1].rstrip(), last_names[last_name_idx].rstrip(), first_names[first_name_idx][0], dobs[i], ages[i], dods[i],
                Address('NULL', 'NULL', 'NULL', 'NULL', 'NULL'), '000-00-0000'),
            )
        
        #print(f'%{i/10_000:.2f}\r', end='')

    return population

# assign marriage status
def set_married(population):
    population.sort(key=lambda x: x.dob)
    for i, person in enumerate(population):
        # skip already married people, people under 18, or people who fail the probability check
        if person.partner_ssn != '000-00-0000' or person.age < 18 or random.uniform(0, 1) > 0.005:
            continue

        # assign the first viable partner, if possible, otherwise ignore
        idx = i + 1
        while abs(population[idx].dob.year - person.dob.year) <= 5:
            # no strange stuff going on here :)
            if population[idx].age >= 18:
                # assign marriage
                person.partner_ssn = population[idx].ssn
                population[idx].partner_ssn = person.ssn

                # 90% chance the married couple lives in the same home
                if random.uniform(0, 1) < 0.9:
                    # 50% chance who gets whose address
                    if random.uniform(0, 5) < 0.5:
                        person.address = population[idx].address
                    else:
                        population[idx].address = person.address
                break
            idx += 1

# write the population information to a file, formatted like a table (left-aligned)
def write_population(population):
    with open('./data/population.dat', 'w') as f:
        f.write(f'{"SSN":<15}{"First Name":<20}{"Last Name":<20}{"Sex":<5}{"DOB":<18}{"Age":<11}{"DOD":<18}{"Address 1":<40}{"Address 2":<40}{"City":<40}{"State":<6}{"Zip":<10}{"Partner SSN":<15}\n')
        f.write(f'{"*" * 258}\n')
        for p in population:
            f.write(f'{p}\n')

# write the population information to a file in binary format to be read in from other files
def write_population_pickle(population):
    with open('./upload/pkl/population.pkl', 'wb') as f:
        pickle.dump(population, f)

if __name__ == '__main__':
    main()