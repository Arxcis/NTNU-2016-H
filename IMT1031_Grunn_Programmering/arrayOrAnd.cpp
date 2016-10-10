

#include <iostream>

bool arrayAnd( const char checker, const char array[], const char operand[]); 
bool arrayAnd( const int checker,   const int array[], const char operand  );
 


bool arrayAnd( const char checker, const char array[], const char operand[] ) 
{
    int arrSize = sizeof (array) / sizeof (array[0]);
    int trueCount = 0;

    switch (operand[0]) 
    {
        case '!':
            for (int i=0;i<arrSize) { if (checker != array[i])    
                                            trueCount ++;   }
            break;

        case '=':
            for (int i=0;i<arrSize) { if (checker == array[i])
                                            trueCount ++;       }
            break; 
    } 

    if (trueCount == arrSize)  return true;
    if (trueCount != arrSize)  return false;
}


bool arrayAnd( const int checker, const int array[], const char operand ) 
{

    int arrSize = sizeof (array) / sizeof (array[0]);
    int trueCount = 0;

    switch (operand[0]) 
    {
        case '!':
            for (int i=0;i<arrSize) { if (checker != array[i])    
                                            trueCount ++;   }
            break;

        case '=':
            for (int i=0;i<arrSize) { if (checker == array[i])
                                            trueCount ++;       }
            break; 
    } 

    if (trueCount == arrSize)  return true;
    if (trueCount != arrSize)  return false;
}

int main() 
{
    char input; 

    do {

        std::cout << "Try again";
        std::cin >> input;
        input = toupper(input);

    } while (arrayAnd(input, "!=", { 'M', 'Q', 'A', 'B', 'C' }));

    return 0; 
}