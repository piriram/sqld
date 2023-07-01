class Solution {
    public int solution(int[] money) {
        int[] dp_first = new int[money.length];    // 첫 번째 집부터 시작하는 경우의 돈의 최댓값을 저장할 배열
        int[] dp_second = new int[money.length];   // 두 번째 집부터 시작하는 경우의 돈의 최댓값을 저장할 배열
        
        for(int i = 0; i < money.length; i++) {
            dp_first[i] = money[i];     // 각 집에서 얻을 수 있는 돈의 최댓값으로 초기화
            dp_second[i] = money[i];
        }
        dp_first[1] = -1;    // 첫 번째 집을 훔친 경우는 두 번째 집을 훔칠 수 없으므로 값 설정
        dp_second[0] = -1;   // 두 번째 집을 훔친 경우는 첫 번째 집을 훔칠 수 없으므로 값 설정
        dp_first[2] += dp_first[0];     // 세 번째 집부터는 첫 번째 집의 돈을 훔치기 때문에 해당 값을 더해줌
        for (int i = 3; i < money.length; i++) {
            dp_first[i] += Math.max(dp_first[i - 2], dp_first[i - 3]);      // 직전 집에서 훔친 돈의 최댓값 중 큰 값을 더해줌
            dp_second[i] += Math.max(dp_second[i - 2], dp_second[i - 3]);
        }
        int first_max = Math.max(dp_first[money.length - 2], dp_first[money.length - 3]);      // 마지막 집 전까지의 돈의 최댓값 중 큰 값을 저장
        int second_max = Math.max(dp_second[money.length - 1], dp_second[money.length - 2]);   // 마지막 집까지의 돈의 최댓값 중 큰 값을 저장
        return Math.max(first_max, second_max);     // 두 경우 중 큰 값을 반환
    }
}
