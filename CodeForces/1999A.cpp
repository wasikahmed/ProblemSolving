// A+B Again?

#include <iostream>
using namespace std;

int main() {
    int t;
    cin>> t;
    while (t--) {
        int num;
        cin>> num;
        cout<< (num % 10) + ((num / 10) % 10)<< endl;
    }

    return 0;
}