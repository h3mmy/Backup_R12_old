#include <iostream>
#include <fstream>
#include <string>
using namespace std;


bool verify (unsigned long int d, unsigned p_d){
    
    for (int i=1; i<=d; i++){
        if (double(i)*100/double(d) == double(p_d)){
            cout << i << endl;
            return 1;
            }
        else{
            return 0;
            }
        }
    }


int main() {
    
    ifstream srcfile;
    ofstream outfile;
    
    int T;
    
    srcfile.open("sample");
    outfile.open("output_file");

    if (srcfile.is_open()){
        
        srcfile >> T;
        
        while (srcfile.good()){
            unsigned long int N;
            unsigned int P_D;
            unsigned int P_G;
            unsigned long int D;
        
            srcfile >> N >> P_D >> P_G;
            
            if (outfile.is_open()){
            
                D = N;
                while (!(verify(D, P_D))){
                    D--;
                    }
                
                //for (unsigned long G
                
                outfile << N << endl;
                cout << D << endl;
                
                
                }
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