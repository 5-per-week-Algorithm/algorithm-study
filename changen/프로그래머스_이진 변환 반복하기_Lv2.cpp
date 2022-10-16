#include <string>
#include <vector>
#include <iostream>

using namespace std;

string binary_to_decimal(int n){
    string binary = "";
    while(1){
        if(n%2==1) binary.push_back('1');
        else binary.push_back('0');
        n = n/2;
        
        if(n==0) break;
    }
    return binary;
}

vector<int> solution(string s) {
    vector<int> answer;
    int t = 0;
    int zero = 0;
    int i, one;
    int check;
    
    while(1){
        if(s=="1") break;
        check = 0;
        one = 0;
        for(char c: s){
            if(int(c-'0')==0){
                zero++;
                check=1;
            }
            else if(int(c-'0')==1) one++;
            }
        if(s=="1") break;
        s = binary_to_decimal(one);
        t++;
    }
    answer.push_back(t);
    answer.push_back(zero);
    return answer;
}