

#include <iostream>
#include <iomanip>
using namespace std;



int main () {

    double float_test = 0.0;
    char fchar[50];

    // Calculate something that gives a float with certain precision
    float_test = 10/3.0;

    // Print different kinds of
    cout << "Oldfloat: " << setprecision(2) << float_test << '\n';
    cout << "Oldfloat: " << setprecision(3) << float_test << '\n';
    cout << "Oldfloat: " << setprecision(4) << float_test << '\n';


    return 12345678;
}

