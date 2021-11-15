#include <iostream>
using namespace std;

int main () {
    int a;
    int i = 0;
    int j = 0;
    cout << "Input : "; cin >> a;

    //=============================//
    
    cout << "Segitiga dengan for loop" << endl;
    for (i = 1; i <= a; i++) {
        for (j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }
    for (i = 1; i <= a; i++) {
        for (j = i; j <= a; j++) {
            cout << "*";
        }
        cout << endl;
    }

    //=============================/

    cout << "Segitiga dengan while loop" << endl;
    i = 1;
    while (i <= a) {
        j = 1;
        while (j <= i) {
            cout << "*";
            j++;
        }
        i++;
        cout << endl;
    }
    i = 1;
    while (i <= a)  {
        j = i;
        while (j <= a) {
            cout << "*";
            j++;
        }
        i++;
        cout << endl;
    }

    //=============================//

    cout << "Segitiga dengan do-while loop" << endl;
    i = 1;
    do {
        j = 1;
        do {
            cout << "*";
            j++;
        }
        while(j <= i);
        i++;
        cout << endl;
    }
    while (i <= a);
    i = 1;
    do {
        j = i;
        do {
            cout << "*";
            j++;
        }
        while(j <= a);
        i++;
        cout << endl;
    }
    while (i <= a);

}
