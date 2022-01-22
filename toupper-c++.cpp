#include <ctype.h>
#include <iostream>
using namespace std;
 
int main () {
  int i=0;
  string str="Teksteks";
  char c;
  while (str[i]) {
    cout << (char) toupper(str[i]); //sama dengan yg baris 11, cuma yg ini harus di casting dulu ke char
                                    // supaya outputnya dalam bentuk char, klo nda pake itu << toupper(str[i]) hasilnya bakalan bilangan ascii yg yg keluar.
    putchar (toupper(str[i]));
    i++;
  }
  return 0;
}
