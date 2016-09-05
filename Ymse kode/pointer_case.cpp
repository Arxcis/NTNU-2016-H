
#include <iostream>


int main(){

    char array[] = {    '1','2','3','4','5','6','7','8'   };

    std::cout << &array << '\n';

    char* mypointer = &array[0];

    std::cout << * mypointer << '\n';
    std::cout << mypointer << '\n';

                // sizeof() is the keyword i have been looking for all along.
                // sizeof() equals 'len(value)' in python and 'value.length' in
                // javacript.
                // NOT QUITE though, sizeof is the size of the value in bytes!
                //    So to get the real length of an array for instance, we 
                //    have to devide the size in bytes by bytes per length unit
                // This gives the following formula:
                // Length = total number of bytes / bytes per array unit
                // Eksample:
                // Length =  (int_32 array[8])  32 bytes  /  (int_32)  4 bytes 
                // Length =  (char   array[8])   8 bytes  /  ( char )  1 byte

    std::cout << "Sizeof array : " << sizeof(array) << '\n';
    std::cout << "Sizeof unit : " << sizeof(array[0]) << '\n';

    for (int i=0; i< sizeof(array) / sizeof(array[0]); i++){

        std::cout << * (mypointer + i) << '\n';

    }

    return 0;
}