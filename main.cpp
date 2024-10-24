#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>

class CombinationGenerator {
public:
    CombinationGenerator(const std::vector<std::string>& input , const std::vector<std::string>& input2 ) 
    : set(input) , INFOS(input2) {
        generateDefaultCombinations();
        generateAllCombinations();
    }

    void writeAllCombinations(){
        int flag = 0;
        std::string filename = set[0]+set[1]+".txt";
        std::fstream output(filename , std::ios::out);
        if (!output)
            std::cerr << "Error: Writting to the file " << filename << "\n";
        for (auto combo : combinations){
            if (combo != "" )
                output << combo << "\n";
                flag++;
        }
        std::cout << flag << " passwords were written to " << filename << "\n";
        std::cout << "*** DONE ***\n";
   }

private:
    std::vector<std::string> set;
    std::vector<std::string> combinations;
    std::vector<std::string> INFOS;

    std::string capitalize(const std::string& str){
        return ((char)toupper(str[0])+ str.substr(1,size(str)-1) );
    }

    void generateDefaultCombinations() {
        const std::string& name = set[0];
        const std::string& surname = set[1];
        const std::string& date = set[2];
        const std::string& month = set[3];
        const std::string& year = set[4];
        const std::string& phone = set[5];

        for (const std::string symbol : {"!", "_" ,"@", "#", "$", "%", "^", "&", "*" , "@@" }) {
			combinations.push_back(name + symbol + date + month );     
            combinations.push_back(capitalize(name) + symbol + date + month );    
			combinations.push_back(name + symbol + surname + year);   
            combinations.push_back(capitalize(name) + symbol + surname + year);   
            combinations.push_back(capitalize(name) + symbol + capitalize(surname) + year );   
            combinations.push_back(name + symbol + "123"); 
            combinations.push_back(capitalize(name) + symbol + "123");
            combinations.push_back(name + symbol + year);
            combinations.push_back(capitalize(name) + symbol + year);
            combinations.push_back(name + symbol + surname);
            combinations.push_back(capitalize(name) + symbol + capitalize(surname));
            combinations.push_back(symbol + symbol + name + year);
            combinations.push_back(name + surname + symbol + year);
            if ( std::stoi(date) < 10 && std::stoi(month) < 10 && std::stoi(year) < 2010 )
                combinations.push_back(name + surname + symbol + date + month + year[3]);
            
        }
    }

    void generateAllCombinations() {
        unsigned int power = 1 << INFOS.size(); // 2^size

        for (unsigned int i = 0; i < power; i++) {
            std::string word;
            for (unsigned int j = 0; j < INFOS.size(); j++) {
                if (i & (1 << j)) {
                    word += INFOS[j];
                }
            }
            combinations.push_back(word);
        }
    }
};

void gatherInfo(std::vector<std::string>& set , std::vector<std::string>& INFOS) {
    std::string name, surname, date, month, year, phoneNumber , info , temp;

    std::cout << "Enter victim name (separated by space): ";
    std::cin >> name >> surname;
    set.push_back(name);
    set.push_back(surname);

    std::cout << "Enter date of birth (day month year): ";
    std::cin >> date >> month >> year;
    set.push_back(date);
    set.push_back(month);
    set.push_back(year);

    std::cout << "Enter victim phone number: ";
    std::cin >> phoneNumber;
    set.push_back(phoneNumber);
	
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::cout << "Enter extra info (separated by space) : " ;
	std::getline(std::cin , info) ;
	std::stringstream obj(info);

	while ( obj >> temp)
		INFOS.push_back(temp);
	temp = "";
}

int main() {
    std::vector<std::string> set;
    std::vector <std::string> INFOS;
    gatherInfo(set , INFOS);
    
    CombinationGenerator generator(set,INFOS);
    generator.writeAllCombinations();

    return 0;
}

