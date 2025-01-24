// Amusing Joke

#include <iostream>
#include <unordered_map>
using namespace std;


bool solve(string guest, string host, string pile) {
    if ((guest.length() + host.length()) != pile.length()) {
        return false;
    }

    unordered_map<char, int> guestFreq, hostFreq, pileFreq;
    for (char c: guest) guestFreq[c]++;
    for (char c: host) hostFreq[c]++;
    for (char c: pile) pileFreq[c]++;

    unordered_map<char, int>:: iterator it;
    for (it=pileFreq.begin(); it!=pileFreq.end(); it++) {
        it->second -= guestFreq[it->first];
        it->second -= hostFreq[it->first];

        if (it->second > 0) return false;
        if (guestFreq[it->first] < 0 || hostFreq[it->first] < 0) return false;
    }
    return true;
}

int main() {
    string guest, host, pile;
    cin>> guest>> host>> pile;

    bool result = solve(guest, host, pile);
    if (result) cout<< "YES"<< endl;
    else cout<< "NO"<< endl;

    return 0;
}