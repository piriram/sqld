//가는 경우의 수 : 오른쪽 한칸, 아래 한칸
//현재 내 타일 (1, 0)일 때, 바로 전에서 올 수 있는 경로는 (0,0) 하나뿐. dp[1][0] = 1
//(1, 2)일 때, 이전 (1,1)과 (0,2)에서 올수 있는 경로를 더한다. dp[1][2] = dp[1][1] + dp[0][2];
//다만 웅덩이인 경우는 -1 넣고 제외
class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        int [][]dp = new int[n][m];
        
        for (int[] i : puddles)
            dp[i[1] - 1][i[0] - 1] = -1;
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (dp[i][j] == 0) {
                    if (i != 0 && dp[i - 1][j] != -1)
                        dp[i][j] += dp[i - 1][j];
                    if (j != 0 && dp[i][j - 1] != -1)
                        dp[i][j] += dp[i][j - 1];
                    dp[i][j] %= 1000000007;
                }
            }
        }
        return dp[n - 1][m - 1];
    }
}