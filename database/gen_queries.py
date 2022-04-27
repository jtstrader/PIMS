#!/usr/bin/python3
import pickle
from functools import total_ordering

# generate queries based on large data files provided by the generation scripts

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

# date object used to help manage writing date information
class Date:
    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    def csv_out(self):
        return f'{self.year}-{f"0{self.month}" if self.month < 10 else self.month}-{f"0{self.date}" if self.date < 10 else self.date}'

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

class Business:
    def __init__(self, id, name, address, worth, founding_year):
        self.id = id
        self.name = name
        self.address = address
        self.worth = worth
        self.founding_year = founding_year

class Occupation:
    def __init__(self, ssn, business_id, position, wage, salary):
        self.ssn = ssn
        self.business_id = business_id
        self.position = position
        self.wage = wage
        self.salary = salary

def main():
    population, businesses, occupations = get_population(), get_businesses(), get_occupations()
    
    # population info
    write_population_csv(population)
    write_location_csv(population)
    write_marital_status_csv(population)
    write_health_csv(population)

    # business info
    write_business_csv(businesses)
    write_business_location_csv(businesses)

    # occupation info
    write_occupation_csv(occupations)

##################################################
# POPULATION CSVs #############################
##################################################
                
# write the csv for the Population table 
def write_population_csv(population):
    with open('./upload/csv/population.csv', 'w') as f:
        f.write('ssn,first_name,last_name\n')
        for p in population:
            f.write(f'{p.ssn},{p.first},{p.last}\n')

# write the csv for the Location table
def write_location_csv(population):
    with open('./upload/csv/location.csv', 'w') as f:
        f.write('ssn,address_1,address_2,city,state,zip\n')
        for p in population:
            q = "\'"
            out = (f'{p.ssn},{p.address.address_1},{p.address.address_2},{p.address.city},{p.address.state},{p.address.zip if str(p.address.zip) != "NULL" else "NULL"}\n')
            f.write(out.replace('NULL', ''))

# write the csv for the MaritalStatus table
def write_marital_status_csv(population):
    with open('./upload/csv/marital_status.csv', 'w') as f:
        f.write('ssn,partner_ssn\n')
        for p in population:
            q = '\''
            out = (f'{p.ssn},{p.partner_ssn if p.partner_ssn != "000-00-0000" else f"{q}NULL{q}"}\n')
            f.write(out.replace('\'NULL\'', ''))

# write the csv for the Health table
def write_health_csv(population):
    with open('./upload/csv/health.csv', 'w') as f:
        f.write('ssn,sex,date_of_birth,age,date_of_death\n')
        for p in population:
            if isinstance(p.dod, str):
                dod_out = '\'NULL\''
            else:
                dod_out = p.dod.csv_out()
            out = (f'{p.ssn},{p.sex},{p.dob.csv_out()},{dod_out}\n')
            f.write(out.replace('\'NULL\'', ''))

##################################################
# BUSINESSES CSVs #############################
##################################################
                
# write the csv for the Business table 
def write_business_csv(businesses):
    with open('./upload/csv/business.csv', 'w') as f:
        f.write('business_id,name,worth,founding_year\n')
        for b in businesses:
            out = (f'{b.id},{b.name},{b.worth},{b.founding_year}\n')
            f.write(out.replace('\'NULL\'', ''))
                
# write the csv for the BusinessLocation table 
def write_business_location_csv(businesses):
    with open('./upload/csv/business_location.csv', 'w') as f:
        f.write('business_id,address,city,state,zip\n')
        for b in businesses:
            fixes = fix_quote_in_str([b.address.address_1, b.address.city])
            f.write(f'{b.id},{fixes[0]},{fixes[1]},{b.address.state},{b.address.zip}\n')

##################################################
# OCCUPATION JOIN ################################
##################################################

# write the csv for the Occupation table
def write_occupation_csv(occupations):
    with open('./upload/csv/occupation.csv', 'w') as f:
        f.write('ssn,business_id,position,wage,salary\n')
        for o in occupations:
            out = f'{o.ssn},{o.business_id},{o.position},{o.wage},{o.salary}\n'
            f.write(out.replace('NULL', ''))

##################################################
# UTILITIES / DATA GATHERING #####################
##################################################

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

# get the occupations from the pickle file
def get_occupations():
    with open('./upload/pkl/occupations.pkl', 'rb') as f:
        occupations = pickle.load(f)
    return occupations

# fix quotes (like apostrophes) found in strings to prevent string parsing errors in the .sql form
def fix_quote_in_str(strings):
    return [x.replace("'", "''") for x in strings]

if __name__ == '__main__':
    main()
