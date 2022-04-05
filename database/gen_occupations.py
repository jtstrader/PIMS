#!/usr/bin/python3

import pickle
import random
import pprint as pp
from functools import total_ordering
import locale

random.seed()
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# generate the occupational information for the population set

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
        if self.address_2 is None:
            self.address_2 = 'NULL'
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
    def csv_out_depr(self):
        return f'{self.year}-{f"0{self.month}" if self.month < 10 else self.month}-{f"0{self.date}" if self.date < 10 else self.date} 00:00:00'

    def csv_out(self):
        return f'{self.year}-{f"0{self.month}" if self.month < 10 else self.month}-{f"0{self.date}" if self.date < 10 else self.date}'

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
        self.sex = "M" if sex == "B" else "F"
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

class Business:
    def __init__(self, id, name, address, worth, founding_year):
        self.id = id
        self.name = name
        self.address = address
        self.worth = worth
        self.founding_year = founding_year

    def __repr__(self):
        return f'{self.name:<40}{self.address}{self.worth:<15}{self.founding_year:<15}'

class Occupation:
    def __init__(self, ssn, business_id, position, wage, salary):
        self.ssn = ssn
        self.business_id = business_id
        self.position = position
        self.wage = wage
        self.salary = salary
    
    def __repr__(self):
        if self.business_id is None:
            self.business_id = 'NULL'
        if self.position is None:
            self.position = 'NULL'
        if self.wage is None:
            self.wage = 'NULL'
        if self.salary is None:
            self.salary = 'NULL'
        return f'{self.ssn:<15}{self.business_id:<15}{self.position:<40}{self.wage:<12}{self.salary:<12}'

# fill positions based on tier
# tier 1 MUST be filled
# tier 2 has a  5% probability of being filled
# tier 3 has a 95% probability of being filled
tier_1 = [
    ['CEO', 500_000],
    ['CFO', 160_000],
    ['CTO', 219_000],
    ['COO', 195_000],
    ['Research and Development Lead Engineer', 130_000], 
    ['IT System Administrator', 112_000],
    ['Financial Department Supervisor', 90_000],
    ['Marketing Department Supervisor', 70_000],
    ['Human Resources Supervisor', 100_000],
    ['Internal Affairs Lead Supervisor', 100_000],
    ['Legal Department Supervisor', 130_000],
]

tier_2 = [
    ['Administrator', 56_000],
    ['Senior Developer', 120_000],
    ['Senior Analyst', 115_000],
    ['Qualitative Analyst', 85_000],
    ['Financial Analyst', 65_000],
    ['Senior Sales Representative', 76_000],
    ['Telemarketing Supervisor', 70_000],
    ['Human Resources Hiring Manager', 95_000],
    ['Internal Affairs Investigator', 90_000],
    ['Company Lawyer', 115_000]
]

tier_3 = [
    ['Research and Development Engineer', 110_000],
    ['Software Engineer', 107_000],
    ['Software Analyst', 95_000],
    ['IT Analyst', 65_000],
    ['Actuary', 96_000],
    ['Portfolio Manager', 88_000],
    ['Sales Representative', 62_000],
    ['Telemarketer', 55_000],
    ['Human Resources Representative', 70_000],
    ['Internal Affairs Representative', 75_000],
]

# generalized structure to make assigning values in get_company_status more concise
occupation = {
    1: tier_1,
    2: tier_2,
    3: tier_3
}

# list of size 500 with sublist of 11 0's in each cell
# represents tier_1 positions filled in a business
tier_1_finished = [[0 for _ in range(11)] for _ in range(500)]

pay_testing = []

def main():
    population, businesses = get_population(), get_businesses()
    occupations = get_occupations(population, businesses)

    write_occupations(occupations)
    write_occupations_pickle(occupations)

# generate the list of occupations for each population member who is not dead
def get_occupations(population, businesses):
    # sort by a businesses worth to assist in which business gets which priority of employee
    # businesses worth more on the market will have more employees, and by extension, a 
    # much higher % chance to receive employees during random selection
    businesses.sort(key=lambda x: x.worth, reverse=True)

    # Business % Chance of Selection
    # ==============================
    # Rank 1-100: 50% chance
    # Rank 100-200: 25% chance
    # Rank 200-300: 12.5% chance
    # Rank 300-400: 7.5% chance
    # Rank 400-500: 5.0% chance
    # ==============================

    occupations = []
    # population member must NOT be dead and must be at or over the age of 18
    for p in population:
        if p.age < 18 or p.dod is None:
            occupations.append(Occupation(p.ssn, None, None, None, None))
            continue
        
        chance = random.random()

        if chance > 0.5: # between 1.000 - 0.500 = 50%
            business_idx = int(random.random() * 100)
        elif chance > 0.25: # between 0.50 - 0.250 = 25%
            business_idx = int(random.random() * 100) + 100
        elif chance > 0.125: # between 0.250 - 0.125 = 12.5%
            business_idx = int(random.random() * 100) + 200
        elif chance > 0.05: # between 0.125 - 0.050 = 7.5%
            business_idx = int(random.random() * 100) + 300
        else: # between 0.050 - 0.000 = 5%
            business_idx = int(random.random() * 100) + 400
        
        position, wage, salary = get_company_status(businesses, business_idx)

        occupations.append(Occupation(p.ssn, businesses[business_idx].id, position, wage, salary))
    return occupations

# generate the position, wage/salary of an individual at a given company
def get_company_status(businesses, business_id):
    worth = businesses[business_id].worth

    # default wage to None
    wage = None

    # tier 1 MUST be filled
    # tier 2 has a  5% probability of being filled
    # tier 3 has a 95% probability of being filled

    # not all tier 1 positions are filled out
    if any(x == 0 for x in tier_1_finished[business_id]):
        tier = 1
        position_idx = tier_1_finished[business_id].index(0)
        tier_1_finished[business_id][position_idx] = 1

    else:
        # all tier 1 positions are filled out, move towards tier 2 and tier 3
        chance = random.random()
        
        if chance <= 0.05:
            tier = 2
        else:
            tier = 3

        position_idx = int(random.random() * len(occupation[tier]))

    # all tier 2 positions are salaries
    position = occupation[tier][position_idx][0]
    base_salary = occupation[tier][position_idx][1]
    salary = base_salary + company_worth_pay_adjust(worth, base_salary)

    # if tier 3, 50% chance employee is waged
    if tier == 3:
        if random.random() <= 0.05:
            wage = salary // 52 // 40
            salary = None

    return position, wage, salary

# adjust the net pay of an individual working at a company 
# based on their provided salary and the worth of the company
def company_worth_pay_adjust(worth, salary):
    if worth >= 400_000_000_000:
        return int((worth / 1_000_000_000_000) * salary)
    return -int((worth / 5_000_000_000_000) * salary)

# get the population from the pickle file
def get_population():
    with open('./upload/pkl/population.pkl', 'rb') as f:
        population = pickle.load(f)
    return population

# get the businesses from the pickle file
def get_businesses():
    with open('./upload/pkl/businesses.pkl', 'rb') as f:
        businesses = pickle.load(f)
    return businesses
    
# write occupations out to occupations.dat in the data directory
def write_occupations(occupations):
    with open ('./upload/data/occupations.dat', 'w') as f:
        f.write(f'{"SSN":<15}{"Business ID":<15}{"Position":<40}{"Wage":<12}{"Salary":<12}\n')
        f.write(f'{"*" * 94}\n')
        for o in occupations:
            f.write(f'{o}\n')

# write occupations out to an object file for reading by the query generator
def write_occupations_pickle(occupations):
    with open('./upload/pkl/occupations.pkl', 'wb') as f:
        pickle.dump(occupations, f)

if __name__ == '__main__':
    main()