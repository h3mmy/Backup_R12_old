#include <iostream>
#include <fstream>
using namespace std;




int main() {
    
    ifstream srcfile;
    ofstream outfile;
    
    srcfile.open(sample);
    outfile.open(output_file);

    if (srcfile.is_open()){
        while (srcfile.good()){
            //srcfile >> a;
            //getline(srcfile, b);
            
            if (!srcfile.good()) break;
            if (outfile.is_open()){
            
                // Do stuff
                
                }
            }
            
        else{
        cerr << "Unable to open " << students_old << endl;
        cerr << "Program Terminated...\n";
        exit(1);
        }
        }
    
    srcfile.close();
    
    outfile.close();
    }