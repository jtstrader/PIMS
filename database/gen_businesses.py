#!/usr/bin/python3

import pickle
import random
random.seed()

# business information
class Business:
    def __init__(self, id, name, address, worth, founding_year):
        self.id = id
        self.name = name
        self.address = address
        self.worth = worth
        self.founding_year = founding_year

    def __repr__(self):
        return f'{self.id:<5}{self.name:<40}{self.address}{self.worth:<15}{self.founding_year:<15}'

# address of the business
class Address:
    def __init__(self, address_1, city, state, zip):
        self.address_1 = address_1
        self.address_2 = None
        self.city = city
        self.state = state
        self.zip = zip
    
    def __repr__(self):
        return f'{self.address_1:<40}{self.city:<40}{self.state:<6}{self.zip:<10}'


# generate business locations -- 2 business per state
def main():
    streets, cities, states = get_address_values()
    companies = get_businesses()
    businesses = gen_info(streets, cities, states, companies)

    write_businesses(businesses)
    write_businesses_pickle(businesses)

# read from files and get relevant address information
def get_address_values():
    with open('./data/street.dat') as f:
        streets = [street.rstrip() for street in f]
    with open('./data/cities.dat') as f:
        cities = [city.rstrip() for city in f]
    with open('./data/states.dat') as f:
        states = [state.rstrip() for state in f]
    return (streets, cities, states)

# read from files and get businesses
def get_businesses():
    with open('./data/companies.dat') as f:
        return [business.rstrip() for business in f]

# generate the location info for the businesses
def gen_info(streets, cities, states, companies):
    businesses = []
    for i, state in enumerate(states):
        for j in range(2):
            business_idx = random.randint(0, len(companies)-1)
            street_idx = random.randint(0, len(streets)-1)
            city_idx = random.randint(0, len(cities)-1)

            businesses.append(
                Business((i*2)+j+1, companies[business_idx],
                Address(f'{random.randint(1, 1000)} {streets[street_idx]}', cities[city_idx], state, random.randint(10000, 99999)),
                random.randint(100_000_000, 1_000_000_000_000), random.randint(1900, 2000))
            )
            del companies[business_idx]
            
    return businesses

# write the business information to a file
def write_businesses(businesses):
    with open('./data/businesses.dat', 'w') as f:
        f.write(f'{"ID":<5}{"Business Name":<40}{"Address":<40}{"City":<40}{"State":<6}{"Zip":<10}{"Worth":<15}{"Founding Year":<15}\n')
        f.write(f'{"*" * 171}\n')
        for business in businesses:
            f.write(f'{business}\n')

# write the business information to a file in binary format to be read in from other files
def write_businesses_pickle(businesses):
    with open('./upload/pkl/businesses.pkl', 'wb') as f:
        pickle.dump(businesses, f)

if __name__ == '__main__':
    main()