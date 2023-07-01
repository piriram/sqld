import java.util.*;

class Solution {
    static boolean[] visited;

    public int solution(int n, int[][] computers) {
        int answer = 0;

        visited = new boolean[n];
        for(int i=0;i<n;i++){
            if(!visited[i]){
                bfs(n,computers,i);
                answer++;
            }
                
        }

        return answer;
    }
    public void bfs(int n,int[][] computers,int give){
        int ans = 0;
        Queue<Integer> que = new LinkedList<>();
        que.offer(give);
        visited[give] = true;
        while(!que.isEmpty()){
            int x = que.poll();
            for(int i=0;i<n;i++){
                if(!visited[i] && computers[x][i]==1){
                    que.offer(i);
                    visited[i]=true;
                }
            }
        }
    }
    
}