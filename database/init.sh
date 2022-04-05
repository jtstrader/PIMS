#!/bin/bash

# initialize data and create queries in the upload/ directory
if [ ! -d "csv" ] || [ ! -d "data" ]; then
    if [ ! -f "data.tar.gz" ]; then
        echo 'init: err: data set corrupted and/or missing. exiting program.'
        exit
    fi
fi

tar -xzf data.tar.gz

mkdir -p debug/

mkdir -p upload/csv
mkdir -p upload/sql
mkdir -p upload/pkl
mkdir -p upload/data

chmod u+x gen_people.py
chmod u+x gen_businesses.py
chmod u+x gen_occupations.py
chmod u+x gen_dates.py
chmod u+x gen_states.py

# keep track of processes in background -- many of these can run at the same time
proc=()

# run generators
c++ gen_ssn.cpp -O
./a.out &
proc+=("$!")

./gen_dates.py &
proc+=("$!")

./gen_states.py &
proc+=("$!")

for pid in "${proc[@]}"; do
    wait "$pid"
done
rm -f a.out # remove a.out -- ignore error if not exist
echo 'init: ssn.dat created'
echo 'init: dates.dat created'
echo 'init: states.dat created'

proc=()

./gen_businesses.py &
proc+=("$!")

./gen_people.py &
proc+=("$!")

for pid in "${proc[@]}"; do
    wait "$pid"
done

echo 'init: businesses.dat created'
echo 'init: population.dat created'

./gen_occupations.py

echo 'init: occupations.dat created'

./gen_queries.py

echo 'init: queries generated'