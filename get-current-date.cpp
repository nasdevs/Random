#include <bits/stdc++.h>
using namespace std;

int main() {
    time_t t = time(0);
    tm* now = localtime(&t);
    cout << "Year  : " << (now->tm_year + 1900) << "\n"
         << "Mount : " << (now->tm_mon + 1) << "\n"
         << "Day   : " << now->tm_mday << "\n";
}
