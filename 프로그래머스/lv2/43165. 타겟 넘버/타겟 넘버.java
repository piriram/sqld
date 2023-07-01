import java.util.*;
// visited에 저장?
// 숫자는 최대 50
// 큐를 어떻게 이용해야할까
// 큐를 안이용하고 나올때마다 sum을 뺄까?

class Solution {

    Queue<Integer> sumQue = new LinkedList<>();
    int answer = 0;
    int len ;
    
    public int solution(int[] numbers, int target) {
        
        len = numbers.length; //numbers 배열에서 index의 끝을 나타내기위함
        bfs(0,0,target,numbers);
        
        return answer;
    }
    public void bfs(int sum2,int index,int target,int[] numbers){

        if(index<len){  
            bfs(sum2+numbers[index],index+1,target,numbers);
            bfs(sum2-numbers[index],index+1,target,numbers);
        }else if(index == len && target == sum2){
            answer++;
        }
    

    }
}