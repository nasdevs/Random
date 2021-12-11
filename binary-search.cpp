#include <iostream>
using namespace std;

int binarySearch(int arr[], int size, int searchFind) {
    int low = 0;
    int high = size - 1;
    int mid = 0;

    while (low <= high) {
        mid = (low + high) / 2;

        if (searchFind == arr[mid]) return mid;
        else if (searchFind > arr[mid]) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int main() {
    int list[] = {1, 34, 42, 59, 90, 103, 114, 152, 190, 219, 308};
    int find;
    cout << "Input : "; cin >> find;

    int size = sizeof(list) / sizeof(list[0]);
    int result = binarySearch(list, size, find);

    if (result >= 0) {
        cout << "Ditemukan, angka " << find << " ada di index " << result << endl;
    }
    else cout << "Tidak ditemukan" << endl;
}
