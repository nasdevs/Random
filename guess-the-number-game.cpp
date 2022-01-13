/*
@name : Guess the Number Game
@author : Nasrullah
@version : 0.1.0
@url github : https://github.com/nasdevs
*/

#include <iostream>
#include <unistd.h>
using namespace std;

int tebakAngka(int &low, int &high, int mid = 0) {
    char jawaban;
    bool loop = true;
    while (loop == true) {
        mid = (low + high) / 2;
        cout << "Apakah angkanya lebih besar / sama dengan " << mid << " [y/n] : "; cin >> jawaban;
        if (low-1== mid) {
            return mid;
        }
        else if (jawaban == 'y' || jawaban == 'Y') {
            low = mid + 1;
        }
        else if (jawaban == 'n' || jawaban == 'N') {
            high = mid - 1;
        }
        else mid+=0;
    }
    return -1;
}

int main() {
    int search, low, high;
    int result = -1;
    cout << "Masukkan di antara mana angka anda berada      " << endl;
    cout << "contoh : angka 34 berada di antara -9 dan 902  " << endl;
    cout << "=============================================\n" << endl;
    cout << "Input terendah : "; cin >> low;
    cout << "Input tertinggi : "; cin >> high;
    cout << "Pikirkan 1 angka diantara " << low << " - " << high << endl;
    sleep(3);
    cout << "Sudah dapat? jika ya silahkan jawab pertanyaan berikut" << endl;

    result =  tebakAngka(low, high);
    if (result >= 0) cout << "Angka anda adalah = " << result << endl;
    else cout << "Error!" << endl;
}
