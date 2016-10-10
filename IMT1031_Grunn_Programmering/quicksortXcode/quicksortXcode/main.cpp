//
//  main.cpp
//  quicksortXcode
//
//  Created by Jonas Solsvik on 29.09.2016.
//  Copyright © 2016 Jonas Solsvik. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

void quickSort(int A[],int,int);

int partition(int A[], int,int);

const int LEN = 90;

int SWAP = 0;

int main()
{
    int A[LEN] = {6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,
                  6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,
                  6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11,6,10,13,5,8,3,2,25,4,11};
    int p=0;
    int q=90;
    
    cout<<"======Original======="<<endl;
    for(int i=0; i<LEN; i++)
        cout<< A[i] <<" ";
    cout<< endl;
    
    quickSort(A,p,q);
    
    cout<<"======Sorted======="<<endl;
    for(int i=0; i<LEN; i++)
        cout<< A[i] <<" ";
    cout<< endl;
    cout << "Swaps = " << SWAP << endl;
}


void quickSort(int A[], int p,int q)
{
    int r;
    if(p<q)
    {
        r=partition(A, p,q);
        quickSort(A,p,r);
        quickSort(A,r+1,q);
    }
}


int partition(int A[], int p,int q)
{
    int x= A[p];
    int i=p;
    int j;
    
    for(j=p+1; j<q; j++)
    {
        if( A[j] <= x)
        {
            i=i+1;
            swap(A[i],A[j]);

            SWAP ++;
        }
        
    }
    
    swap(A[i],A[p]);
    SWAP++;
    return i;
}
