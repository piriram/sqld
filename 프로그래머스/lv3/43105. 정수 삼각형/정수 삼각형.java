import java.util.*;
class Solution {
    int[][] sum;
    public int solution(int[][] triangle) {
        int answer = 0;
        int len = triangle.length;
        sum = new int[len][len];
        for(int i=0;i<len;i++){
            sum[i] = new int[len];
        }
        sum[0][0] = triangle[0][0];
        for(int i=1;i<len;i++){
            for(int j=0;j<triangle[i].length;j++){

                if (j>0){
                   sum[i][j]= Math.max(sum[i-1][j]+triangle[i][j],sum[i-1][j-1]+triangle[i][j]);
                }
                else{
                    sum[i][j]=sum[i-1][j]+triangle[i][j];
                }
            }
        }
        for(int i=0;i<len;i++){
            answer = Math.max(sum[len-1][i],answer);
        }
        return answer;
    }
}