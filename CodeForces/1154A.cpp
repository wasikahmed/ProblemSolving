// Restoring Three Numbers

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> restoreThreeNums(int x1, int x2, int x3, int x4) {
    vector<int> nums;
    vector<int> sums = {x1, x2, x3, x4};

    // a+b+c
    int sumAll = *max_element(sums.begin(), sums.end());

    sums.erase(remove(sums.begin(), sums.end(), sumAll), sums.end());

    int a = sumAll - sums[0];
    int b = sumAll - sums[1];
    int c = sumAll - sums[2];

    nums.push_back(a);
    nums.push_back(b);
    nums.push_back(c);

    return nums;
}

int main() {
    int x1, x2, x3, x4;
    cin>> x1>> x2>> x3>> x4;

    vector<int> result = restoreThreeNums(x1, x2, x3, x4);

    if (!result.empty()) {
        cout<< result[0]<< " "<< result[1]<< " "<<result[2]<< endl;
    }

    return 0;
}