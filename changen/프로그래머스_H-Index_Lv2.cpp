#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(),citations.end(),greater<int>());
    int i, n;
    int temp = 0;
    for(i=0;i<citations.size();i++){
        if((i+1)<=citations[i]){
            if(i+1>answer){
                answer = i+1;
            }
        }
    }
    return answer;
}