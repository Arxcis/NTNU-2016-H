#include <iostream>
#include <cstring>
using namespace std;


// 2. oppgave b)


class AA {

	private:
		char nvn[10];   // cstring of 10 characters.
		int nr;

	public:
		AA() 					{	strcpy(nvn, ""); nr = 0;	    }  // strcpy copies cstring from 1 variable to another.
		AA(char t[], int n)		{	strcpy(nvn, t);  nr = 0; cout << t << ' '; }  // t[]  - variable size array
		void skriv() 			{   cout << nvn << "\t#: " << nr;	}  // 
		char funk1()  			{	return (char(nvn[4]+4)); 		}  // char(a + 4) =  e 
		bool funk2(AA a) 		{   return (nvn[1] == a.nvn[1]);    }  // 
		AA   funk3(int n)		{	return (AA(nvn, nr*n));         }  

};


int main(){

	AA  k1, k2("Petter", 1), k3("Henning", 7);      cout << '\n';
	cout << k3.funk1();								cout << '\n';
	cout << k3.funk2(k2);							cout << '\n';
	k1 = k2.funk3(3);								cout << '\n';
	cout << "K1: "; k1.skriv();						cout << '\n'; 
}




// 1. experiement:
// What is the difference between ++i and i++ in a for-loop

/*
int main(){

	int i;
	int j;

	for (i = 0, j=0; i <= 10; j++, i += j){

		cout << i << '\n';

	}

	j = 8;
	cout << "j prosent 3= " << j % 3 << '\n';
	// << '\n';
	cout << "j /  3 = " << j / 3 << '\n';
	cout << j/3.0 << '\n';

}
*/