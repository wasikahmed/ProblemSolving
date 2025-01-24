// To My Critics

#include <iostream>
using namespace std;

int main() {
    int t; cin>> t;
    int digits[3];
    while (t--)
    {
        cin>> digits[0]>> digits[1]>> digits[2];
        if (digits[0]+digits[1]>=10 || digits[0]+digits[2]>=10 || digits[1]+digits[2]>=10) cout<< "YES"<< endl;
        else cout<< "NO"<< endl;
    }
    
    return 0;
}