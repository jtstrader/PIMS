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

def main():
    population = get_population()
    businesses = get_businesses()
    occupations = get_occupations()
    
    # csv files
    write_population_csv(population)
    write_location_csv(population)
    write_marital_status_csv(population)
    write_health_csv(population)

    write_business_csv(businesses)
    write_business_location_csv(businesses)

    write_occupation_csv(occupations)

    # sql queries
    # write_population_sql(population)
    # write_location_sql(population)
    # write_marital_status_sql(population)
    # write_health_sql(population)

    # write_business_sql(businesses)
    # write_business_location_sql(businesses)

##################################################
# POPULATION CSVs #############################
##################################################

# write the sql for the Population table
def write_population_sql(population):
    with open('./upload/Population.sql', 'w') as f:
        f.write('INSERT INTO [Population] VALUES\n')
        for i, p in enumerate(population):
            fixes = fix_quote_in_str([p.first, p.last])
            
            f.write(f"('{p.ssn}', '{fixes[0]}', '{fixes[1]}')")

            # add trailing comma if not on last row insert
            if i != len(population) - 1:
                f.write(",")
            f.write("\n")
                
# write the csv for the Population table 
def write_population_csv(population):
    with open('./upload/csv/Population.csv', 'w') as f:
        f.write('ssn,first_name,last_name\n')
        for p in population:
            f.write(f'{p.ssn},{p.first},{p.last}\n')

# write the sql for the Location table
def write_location_sql(population):
    with open('./upload/sql/Location.sql', 'w') as f:
        f.write('INSERT INTO [Location] VALUES\n')
        for i, p in enumerate(population):
            if p.address.address_1 != 'NULL':
                fixes = fix_quote_in_str([p.address.address_1, p.address.address_2, p.address.city])
                q = '\''

                f.write(f"('{p.ssn}', '{fixes[0]}', {f'{q}{fixes[1]}{q}' if fixes[1] != 'NULL' else 'NULL'}, '{fixes[2]}', '{p.address.state}', {p.address.zip})")                

            else:
                f.write(f"('{p.ssn}', NULL, NULL, NULL, NULL, NULL)")

            # add trailing comma if not on last row insert
            if i != len(population) - 1:
                f.write(",")
            f.write("\n")

# write the csv for the Location table
def write_location_csv(population):
    with open('./upload/csv/Location.csv', 'w') as f:
        f.write('ssn,address_1,address_2,city,state,zip\n')
        for p in population:
            q = "\'"
            out = (f'{p.ssn},{p.address.address_1},{p.address.address_2},{p.address.city},{p.address.state},{p.address.zip if str(p.address.zip) != "NULL" else "NULL"}\n')
            f.write(out.replace('NULL', ''))

# write the sql for the MaritalStatus table
def write_marital_status_sql(population):
    with open('./upload/sql/MaritalStatus.sql', 'w') as f:
        f.write('INSERT INTO [MaritalStatus] VALUES\n')
        for i, p in enumerate(population):
            q = '\''

            f.write(f"('{p.ssn}', {f'{q}{p.partner_ssn}{q}' if p.partner_ssn != '000-00-0000' else 'NULL'})")
            
            # add trailing comma if not on last row insert
            if i != len(population) - 1:
                f.write(",")
            f.write("\n")

# write the csv for the MaritalStatus table
def write_marital_status_csv(population):
    with open('./upload/csv/MaritalStatus.csv', 'w') as f:
        f.write('ssn,partner_ssn\n')
        for p in population:
            q = '\''
            out = (f'{p.ssn},{p.partner_ssn if p.partner_ssn != "000-00-0000" else f"{q}NULL{q}"}\n')
            f.write(out.replace('\'NULL\'', ''))

# write the sql for the Health table
def write_health_sql(population):
    with open('./upload/sql/Health.sql', 'w') as f:
        f.write('INSERT INTO [Health] VALUES\n')
        for i, p in enumerate(population):
            q = '\''

            f.write(f"('{p.ssn}', {f'{q}{p.sex}{q}' if p.sex != 'NULL' else 'NULL'}, {p.age}, {p.dob.csv_out()}, ")

            if isinstance(p.dod, str):
                f.write("NULL)")
            else:
                f.write(f"{p.dod.csv_out()})")

            # add trailing comma if not on last row insert
            if i != len(population) - 1:
                f.write(",")
            f.write("\n")

# write the csv for the Health table
def write_health_csv(population):
    with open('./upload/csv/Health.csv', 'w') as f:
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

# write the sql for the Business table
def write_business_sql(businesses):
    with open('./upload/sql/Business.sql', 'w') as f:
        f.write('INSERT INTO [Business] VALUES\n')
        for i, b in enumerate(businesses):
            fixes = fix_quote_in_str([b.name])
            
            f.write(f"({b.id}, '{fixes[0]}', {b.worth}, {b.founding_year})")

            # add trailing comma if not on last row insert
            if i != len(businesses) - 1:
                f.write(",")
            f.write("\n")
                
# write the csv for the Business table 
def write_business_csv(businesses):
    with open('./upload/csv/Business.csv', 'w') as f:
        f.write('business_id,name,worth,founding_year\n')
        for b in businesses:
            out = (f'{b.id},{b.name},{b.worth},{b.founding_year}\n')
            f.write(out.replace('\'NULL\'', ''))

# write the sql for the Business table
def write_business_location_sql(businesses):
    with open('./upload/sql/BusinessLocation.sql', 'w') as f:
        f.write('INSERT INTO [BusinessLocation] VALUES\n')
        for i, b in enumerate(businesses):
            fixes = fix_quote_in_str([b.address.address_1, b.address.city])
            
            f.write(f"({b.id}, '{fixes[0]}', '{fixes[1]}', '{b.address.state}', {b.address.zip})")

            # add trailing comma if not on last row insert
            if i != len(businesses) - 1:
                f.write(",")
            f.write("\n")
                
# write the csv for the BusinessLocation table 
def write_business_location_csv(businesses):
    with open('./upload/csv/BusinessLocation.csv', 'w') as f:
        f.write('business_id,address,city,state,zip\n')
        for b in businesses:
            fixes = fix_quote_in_str([b.address.address_1, b.address.city])
            f.write(f'{b.id},{fixes[0]},{fixes[1]},{b.address.state},{b.address.zip}\n')

##################################################
# OCCUPATION JOIN ################################
##################################################

# write the csv for the Occupation table
def write_occupation_csv(occupations):
    with open('./upload/csv/Occupation.csv', 'w') as f:
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
