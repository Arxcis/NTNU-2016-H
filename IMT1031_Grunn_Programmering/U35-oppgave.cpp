

#include <iostream>
using namespace std;



// --- Calculate area of triangle -- 
// ------------------------------------

int main () {

    double g, h, area;

    cout << "\nSkriv inn grunnlinje:  \n";
    cin >> g;
    cout << "\n Skriv inn hoyde: "     << '\n';
    cin >> h;

    area = (g * h) / 2; 

    cout << "\nThe area of the triangle is:" << area << '\n';

    cout << "\nPress enter to continue ...\n";


    cin.ignore(10, '\n');
    cin.get();

    return 0;
}

// --------------------------------------



