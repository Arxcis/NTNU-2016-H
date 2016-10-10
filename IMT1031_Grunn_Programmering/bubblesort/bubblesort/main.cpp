//
//  main.cpp
//  bubblesort
//
//  Created by Jonas Solsvik on 29.09.2016.
//  Copyright © 2016 Jonas Solsvik. All rights reserved.
//


#include <iostream>

const int LEN = 90;

void printArray( int arr[] )
{
    for (int i=0; i<LEN; i++)
        std::cout << arr[i] << ' ';
    std::cout << '\n';
}

void swapInt( int& a, int& b )
{
    a = a + b;
    b = a - b;
    a = a - b;
}


void bubbleSort ( int array[] )
{
    int swaps = 1;
    int i;
    int count = 0;
    while (swaps != 0) {
        swaps = 0;
        
        i = 0;
        for (int j = i+1; j < LEN; j++, i++) {
            
            if (array[i] > array[j]) {
                printArray( array );
                swapInt( array[i], array[j] );
                swaps ++; count++;
            }
        }
    }
    printArray( array );
    std::cout << "Swaps = " << count << '\n';
}

void bubbleSortV2 ( int array[] )
{   
    int count = 0;
    for (int i = 0; i < LEN - 1; i++) {
        for (int j = i+1; j < LEN; j++) {
            if (array[i] > array[j]) {
                printArray( array );
                swapInt( array[i], array[j] );
                count ++;
            }
        }
    }
    printArray( array );
    std::cout << "Swaps = " << count << '\n';
}


int main ()
{
    int mylist  [LEN] = {6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,
                         6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,
                        6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11};

    
    bubbleSort  ( mylist  );
    
    return 0;
}
