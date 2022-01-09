/*
@name : Convert Seconds to Hours, Minutes, and Seconds
@author : Nasrullah
@url github : https://github.com/nasdevs
*/

#include <iostream>
using namespace std;
 
int main() {
    int secondsInput;

    cout << "Convert Seconds to Hours, Minutes, and Seconds" << endl;
    cout << "==============================================\n" << endl;
    
    // input
    cout << "Input seconds : "; cin >> secondsInput;

    // to get hours
    int hours = secondsInput / 3600;

    // to get minutes
    int minutes = (secondsInput/60) % 60;

    // to get seconds
    int seconds = (secondsInput%3600) % 60;

    // output
    cout << "Result:" << endl;
    cout << hours << " hours : " << minutes << " minutes : " << seconds << " seconds" << endl;
}
