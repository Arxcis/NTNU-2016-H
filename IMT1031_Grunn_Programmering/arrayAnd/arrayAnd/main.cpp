#include <iostream>



bool arrayAnd( const char checker, const char operand[], const char array[] )
{
    const int arrSize = std::size(array);
    int trueCount = 0;
    
    switch (operand[0])
    {
        case '!':

            for (int i = 0; i < arrSize; i++) 
            { 
                if (checker != array[i])
                    trueCount ++;   
            }
            break;
            
        case '=':
            for (int i = 0; i < arrSize; i++) 
            {  
                if (checker == array[i])
                    trueCount ++;       
            }
            break;

        default:
            return false;
    }

    return trueCount == arrCount;
}


bool arrayAnd( const int checker, const char operand[], 
               const int array[])
{
    const int arrSize = std::size(array);
    
    switch (operand[0])
    {
        case '!':

            for (int i = 0; i < arrSize; i++) 
            { 
                if (checker != array[i])
                    trueCount ++;     
            }
            break;
            
        case '=':

            for (int i = 0; i < arrSize; i++) 
            { 
                if (checker == array[i])
                    trueCount ++;     
            }
            break;

        default:
            return false;
    }

    return trueCount == arrCount;
}

int main()
{
    char    input;
    int    input2;

    char charKeys[] = { "AEIOUY" };
    int   intKeys[] = { 1, 3, 5, 7, 9 };
    
    do {
        
        std::cout << "Try again {char} - en vokal\n";
        std::cin >> input;
        input = toupper(input);
        
    } while (arrayAnd( input, "!=", charKeys ));
    
    std::cout << "\n\n";

    do {
        
        std::cout << "Try again {int} - et oddetall\n";
        std::cin >> input2;
        
    } while (arrayAnd( input2, "!=", intKeys));
        while(
        input2 != 1,
        input2 != 3,
        input2 != 5,
        input2 != 7,
        input2 != 9, )    
    
    return 0;
}
