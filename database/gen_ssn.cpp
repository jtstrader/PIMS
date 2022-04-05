#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
#include<time.h>
#include<map>

// convert number to ssn format
std::string convert(int ssn);

// writing this in C++ because Python go slow :(
// generate 1_000_000 random unique SSNs 
int main() {
    // set random seed
    srand(time(NULL));

    // open output file and start writing random numbers
    // use a hash table to handle numbers, will use a lot of RAM but very fast
    std::ofstream outFile("./data/ssn.dat");
    
    std::map<int, bool> hash;

    int ssn = 1;

    for(int i=0; i<1000000; i++) {
        while(hash.find(ssn) != hash.end()) {
            ssn = (ssn + (rand() % 1888 + 1)) % 1000000000;
        }
        hash[ssn] = true;
        outFile << convert(ssn) << '\n';
    }

    return 0;
}


// convert ssn to string format
std::string convert(int ssn) {
    // need 9 - len 0's
    std::string ssn_fmt = "";
    std::string ssn_str = std::to_string(ssn);
    int str_len = ssn_str.length();
    int j = 0;

    for(int i=0; i<9; i++) {
        if(i < 9-str_len)
            ssn_fmt += '0';
        else
            ssn_fmt += ssn_str[j++];
        if(i == 2 || i == 4)
            ssn_fmt += '-';
    }
    return ssn_fmt;
}