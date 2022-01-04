/*
sorting algorithm | bubble sort | version 1.0
@author : Nasrullah
*/

#include <iostream>
#include <unistd.h>
#include <utility> // swap()

using namespace std;

int main() {
    int randomNumber[] = {3, 2, 6, 1, 8, 9, 4, 7, 5, 29, 98, 31, 11, 90, 92, 21};
    int size = sizeof(randomNumber) / sizeof(randomNumber[0]);
    int j = 0;

    cout << "Before:" << endl;
    for (int a = 0; a < size; a++) cout << randomNumber[a] << " ";
    cout << endl;
    for (int i = 0; i <= size; i++) {
        if (i == size-1) {
            i = 0;
            j = 0;
        }
        if (randomNumber[i+1] > randomNumber[i]) {
            j++;
            if (j == size-1) break;
            continue;
        }            
        else {
            swap(randomNumber[i+1], randomNumber[i]);
        }
    }

    cout << "After:" << endl;
    for (int k = 0; k < size; k++) cout << randomNumber[k] << " ";
}
