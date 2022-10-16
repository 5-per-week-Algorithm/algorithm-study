#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

priority_queue <pair<int,int>> pq;
bool check[501];

int solution(vector<vector<int>> jobs) {
    
    sort(jobs.begin(),jobs.end());
    int answer=0;
    int temp = jobs[0][0];
    for(vector<int> j: jobs){
        j[0] -= temp;
    }
    int end = jobs[0][1];   
    int time = jobs[0][1];
    int idx = 0;
    check[0] = true;
    answer += time;
    int cnt = 1;    
    
    while(1){
        
        // 우선순위 큐에 대기열 소요시간 계산
        for(int i=0;i<jobs.size();i++){
            if(jobs[i][0] <= end && !check[i]){
                // 이전 종료 - 요청시간 + 소요시간, 소요시간, 인덱스
                pq.push({-jobs[i][1],i});
                check[i] = true;
            }
            else if(jobs[i][0] > end){
                break;
            }
        }
        // 다음꺼 선정함.
        // 만약에 대기열이 없을 경우.
        if(pq.empty()){
            for(int i=0; i<jobs.size();i++){
                if(!check[i]){
                    end = jobs[i][0] + jobs[i][1];
                    idx = i;
                    time = jobs[i][1];
                    answer += jobs[i][1]; // 소요시간 더하기
                    check[i] =true;
                    break;
                }
            }
        }
        // 대기열이 있을 경우. 
        else{
            answer += (-pq.top().first + end - jobs[pq.top().second][0]);
            end = end + -pq.top().first; // 소요시간 + end
            idx = pq.top().second; // 인덱스
            pq.pop();
        }
        
        bool flag = false;
        for(int i=0;i<jobs.size();i++){
            if(check[i] == false){
                flag = true;
            }
        }
        if(pq.empty() && !flag){
            break;
        }
    }
    return answer/jobs.size();
}