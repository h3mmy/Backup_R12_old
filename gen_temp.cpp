#include <iostream>
#include <fstream>
#include <string>
using namespace std;




int main() {
    
    ifstream srcfile;
    ofstream outfile;
    
    string b;
    
    srcfile.open("sample");
    outfile.open("output_file");

    if (srcfile.is_open()){
        while (srcfile.good()){
            //srcfile >> a;
            getline(srcfile, b);
            
            
            // Do stuff
            outfile << b;
            cout << b << endl;
                
                

            if (!srcfile.good()) break;
            }
        
        }    
    else{
        cerr << "Unable to open " << srcfile << endl;
        cerr << "Program Terminated...\n";
        exit(1);
        }
        
    
    srcfile.close();
    
    outfile.close();
    }