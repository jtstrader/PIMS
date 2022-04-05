# Data Generation
The data generation is handled through a connection of Python scripts and C++ program(s) that work together to pull random data. The data was obtained through various online resources through CSV files, saved in the `csv` directory. Normalized data is saved in the `data` directory, and is obtained from using bash and Python scripts and C++ programs to take large sets of data from CSVs and isolate them into a usable format for the generation programs.

The generation programs will take the normalized data and generate either more normalized data, such as the `gen_dates.py`, while others will be used to produce debug data and object data, such as `gen_people.py`. The programs that generate the debug/object data will save their information in two respective locations:
 1. A user readable information file in the `debug` directory
 2. An object (pickle) file that is used by `gen_queries.py` to easily obtain previously generated information without having to parse through the debug file.  

Data then has its query generated through `gen_queries.py`, which saves all relevant information into the `upload` directory. These are the queries ran in the SQL Server to upload the information. Files in the `upload` directory are generated only on client-side machines. No data from this directory is stored on the repo.

The original sets of the data are included in compressed files to allow for easy transference, a tarball for Linux and 7-zip for Windows.

# Generation Programs
The generation programs function to print data in a .dat format and a .csv format for uploading. This means that for generating the uploading queries, the generation program needs a variety of information to generate multiple different scripts for the various tables.

The insertions are generated into CSV files, as the amount of data required is too large for standard SQL queries. However, an optional flag is available if a SQL query must be generated for inserting values.

These CSV files are expected to be inserted into the database using `BULK INSERT`. Note that `KEEPNULLS` must be set in the insertion to avoid missing foreign key errors (as otherwise, SQL Server will interpret NULL foreign keys as empty strings, and throw an error).

A simple dynamic SQL script is included in `init.sql` to help assist in the insertion. Simply copy and paste the entirety of `init.sql` into your query editor, replace **PATH TO UPLOAD CSV DIRECTORY HERE** with the path on your computer to PIMS/database/upload/csv/ (make sure there is a slash at the end!) and then the script will create the tables and insert the data for you!

**Note**: Make sure that the path you provided in the init.sql is the path to your upload/csv directory, not the database/csv directory that contains some of the unnormalized ata.
