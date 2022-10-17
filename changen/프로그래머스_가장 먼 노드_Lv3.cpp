#include <vector>
#include <queue>

using namespace std;    

int solution(int n, vector<vector<int>> edge) {
    
    vector<int> graph[n+1];
    vector<int> visited(n+1);
    vector<int> distance(n+1);
    
    int i;
    for(vector<int> e: edge){
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }
    
    queue<int> q;
    q.push(1);
    visited[1] = 1;
    distance[1] = 0;
    
    int x;
    
    while (!q.empty()) {
        x = q.front();
        q.pop();
        for (int g: graph[x]) {
            int y = g;
            if (!visited[y]) {
                distance[y] = distance[x]+1;
                q.push(y);
                visited[y] = 1;
            }
        }
    }

    int answer = 0;
    
    int max = distance[x];
    for(i=1;i<n+1;i++){
        if(distance[i] == max){
            answer++;
        }
    }
    
    return answer;
}