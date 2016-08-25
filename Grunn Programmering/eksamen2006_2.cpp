
#include <iostream>
#include <cstring>


using namespace std;


//---------------- CONST:
const int STRLEN    =  30;  // Maxlendge på tittel/forlag
const int MAXBLAD   = 200;  // Max blader i datastrukturen
const int ANTDAGER =   6;  // Antall ukedager det kommer ut blader
const char dagnavn[ANTDAGER][5] = {"Man", "Tirs", "Ons", "Tors", "Fre", "Lør"};
                            // Seems like it is possible to make chars 2 dimensional.


//---------------- ENUM:
enum Type       {   Tittel, Forlag  };  // Type of cstring
enum Utgivelse  {   Ukentlig, Annenhver, Maanedlig  };

// When you create a new enum you create a new type, which can be used.


// ----------------- KLASSE:
class Blad {

    private:
        char tittel[STRLEN];  // bladnavn
        char forlag[STRLEN];  // navn på utgiver
        int dagnr;            // utgivelsesdag
        Utgivelse utgivelse;  // En instans av enum Utgivelse som sier noe om frekvensen på utgivelser

    public:                   // Deklarasjon av medlemsfunksjoner, IKKE definisjoner. 
        bool er_lik(Type type, const char t[]);  // 
        bool utgis(int d, int u, char f);

        void skriv(int num);
        void lesinn(const char tit[]);
        void endre();
        void les_fra_fil(char tit[], istream* inn);
};


// -------------- DEKLARASJON AV FUNKSJONER:
void skriv_meny();

// Her deklareres 4 forskjellig funksjoner med samme navn.
// Alle funksjonene har forskjellig returtyper.
// Alle fuknsjonen har forskjellig parametertyper.
// Funksjonene brukes for å lese inn fra brukeren, vha cin.

char les(char t[]);                                     // t[] er en hjelpetext, returnerer en toupper() char.
int  les(const char t[], const int min, const int max); // --//--- , returnerer et innlest tall mellom min og max
void les(const char t[], char s[], const int LEN);      // --// --, leser inn en cstring cin.getline(s, LEN) with LEN=lenght.
Utgivelse les();                         // returnerer enum verdi, Ukentlig, Månedlig,... 

void alle_blader();      // Hvert blad skriver all data om seg selv, stopp for hvert 20 blad og vent på input.
void les_fra_fil();      // Sørger for at alle blader blir lest inn i datastrukturen
void nytt_blad();        // Oppretter et nytt Blad-objekt og leser inn verdiene 
void endre_utgivelse();  // Brukes for å endre utgivelses dag eller frekvens.
void forlags_blader();   // Skriver ut info om blader fra et bestemt forlag
void utgivelser();       // Skriver ut info om blader som gis ut på bestemt dag eller uke


//  -------------- GLOBALE VARIABLER:
Blad blader[MAXBLAD+1];     // en array av Blad-objekter med lengden MAXBLAD=200
int siste_blad = 0;             // Hvor mange blad i bruk til enhvertid - index


// --------------- HOVEDPROGRAM:

int main(){

    char kommando;   // kommando input fra brukeren

    les_fra_fil();    // Init-funksjoner
    skriv_meny();
    kommando = les("Velg kommando");

    cout << "Hello";

    while (kommando != 'Q'){

        switch (kommando){

            case 'A':   alle_blader();      break;
            case 'N':   nytt_blad();        break;
            case 'F':   forlags_blader();   break;
            case 'E':   endre_utgivelse();  break;
            case 'U':   utgivelser();       break;
            default:    skriv_meny();       break;
        }
    }
    cout << "End of program\n";
    return 0;       // Always return 0 in the int main()-loop
}

// ---------- DEFINISJON AV KLASSE-FUNKSJONER:

bool Blad::er_lik(Type type, const char t[]) {
    // strcmp returns 0 if the to cstrings parameters are equal.

    if (type == Tittel){   
        return (!strcmp(tittel, t));    
    } 

    else if (type == Forlag){  
        return (!strcmp(forlag, t));    
    } 

    else {  return 0; }
}

// Oppgave a - f
bool Blad::utgis(int d, int u, char f) {    return 0;   }
void Blad::skriv(int num){

    cout << "Nr: " << num << "  Tittel: " << tittel << "  Forlag: " << forlag << "  Utgivelsesdag: " << dagnr << "  Frekvens: " << utgivelse;

}

void Blad::lesinn(const char tit[]){}
void Blad::endre(){}
void Blad::les_fra_fil(char tit[], istream* inn){}

// ------------- DEFINISJON AV FUNKSJONER:


void skriv_meny(){

    cout << "FØLGENDE KOMMANDOER ER LOVLIG:\n";
    cout << "\tA = Alle blader\n";
    cout << "\tN = Nytt blad\n";
    cout << "\tF = Blad fra et gitt Forlag\n";
    cout << "\tE = Endre utgivelsestidspunkt for ett blad\n";
    cout << "\tU = blad Utgitt et visst tidspunkt\n";
    cout << "\tQ = quit/avslutt\n";
}


char les(char t[]) {

    char ch; 
    cout << t << ":  ";
    cin >> ch;  cin.ignore();
    cout << ch;
    //return (toupper(ch));
    return (toupper(ch));
}            


int  les(const char t[], const int min, const int max) {
    
    int n;
    do {
        cout << "\t" << t << "("<< min << ", " << max << "):\t";
        cin >> n;   cin.ignore();  // Ignores whitespace
    } 
    while (n < min || n >= max);
    return n;
}


void les(const char t[], char s[], const int LEN) {

    do {
        cout << '\t' << t << ":  ";
        cin.getline(s, LEN);            // cin.getline - an unformatted amount of characters

    } while(strlen(s) == 0);            // Input s lenght has to be greater than zero.
}


Utgivelse les() {

    int n = les("Hvor ofte? (1=Ukentlig, 2=Annenhver, 3=Månedlig):  ", 0, 3);
    switch(n){

        case 1:
            return Ukentlig;    break;
        case 2:
            return Annenhver;   break;
        case 3:
            return Maanedlig;    break;
    }
}


int finn(Type type, const char t[]) { 
    // Returns the index of the first Blad-objekt it finds in blader

    for (int i = 0; i < siste_blad; i++){

        if(blader[i].er_lik(type, t)){   
            return i;   
        }
    }
    return 0;
}

// Oppgave a - f

void alle_blader(){

    if (siste_blad && siste_blad <= 0){  cout << "Ingen blad registrert"; }

    else {
        for (int i = 0; i < siste_blad + 1; i++){
            blader[i].skriv(i);
        }
    }
}

void nytt_blad() {}
void forlags_blader() {}
void les_fra_fil () {}
void endre_utgivelse () {}
void utgivelser () {}



/*

    strlen(cstring)
    cin.ignore() 
    cin.getline()
    strcmp(cstr1, cstr2)
    toupper()

*/


