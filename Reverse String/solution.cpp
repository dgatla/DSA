#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:

    void reverseString(vector<char> s) {
        int i = 0, j = s.size() - 1;
        while(i < j){
            // Swaps the characters at the current indices.
            swap(s[i], s[j]);
            i++;
            j--;
        }
    }
};