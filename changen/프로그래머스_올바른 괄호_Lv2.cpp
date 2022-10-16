#include<string>
#include <iostream>
#include <vector>

using namespace std;

void checkBraket(string s, bool &answer){
    vector<char> v;
    
    for(char i: s){
//          여는 괄호면 v에 push
        if(i == '('){
            v.push_back(i);
        }
        else{
//             v의 size가 0이여서 v.back() 을 참조할 수 없는 경우 체크 후 false 처리
            if(v.size() == 0){
                answer = false;
                return;
            }
            
//             닫는 괄호가 나왔을 때 여는 괄호가 아니면 false 처리
            if(v.back() != '('){
                answer = false;
                return;
            }
            else{
                v.pop_back();
            }
        }
    }
    
//     모든 괄호를 처리이후에도 v의 크기가 0이 아니라면 false 처리
    if(v.size() != 0){
        answer = false;
    }
    
    return;
}

bool solution(string s)
{
    bool answer = true;

    checkBraket(s, answer);

    return answer;
}