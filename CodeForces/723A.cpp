// The New Year: Meeting Friends

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minimumTotalDistance(vector<int> positions) {
    sort(positions.begin(), positions.end());
    int median = positions[1];
    int totalDistance = abs(positions[0] - median) + abs(positions[2] - median);

    return totalDistance;
}


int main() {
    vector<int> positions(3);
    int num;
    for (int i=0; i<3; i++) {
        cin>> positions[i];
    }
    int result = minimumTotalDistance(positions);
    cout<< result<< endl;

    return 0;
}