//package breaktime; // breaktime 패키지를 사용하겠다는 선언문

import java.util.*; // 자바 내장 라이브러리인 java.util을 가져옴
import java.io.*; // 자바 내장 라이브러리인 java.io를 가져옴

/* 숨바꼭질
 * 
 * 
 */
public class Main { 
    static int N,K; // N, K를 static 변수로 선언
    static int[] check = new int[100001]; // check 배열을 선언하고 크기를 100001로 함

    public static void main(String[] args) { // main 메소드 시작
        Scanner sc = new Scanner(System.in); // Scanner 객체 생성
        N = sc.nextInt(); // N 입력 받음
        K = sc.nextInt(); // K 입력 받음

        if(N==K) { // N과 K가 같으면
            System.out.println(0); // 0 출력
        }else { // N과 K가 같지 않으면
            bfs(N); // bfs 메소드 호출
        }
    }
    static void bfs(int n) { // bfs 메소드 시작
        Queue<Integer> q = new LinkedList<>(); // Integer 형식의 Queue 객체 생성
        q.add(n); // 큐에 n 추가
        check[n]=1; // check[n]을 1로 설정

        while(!q.isEmpty()) { // 큐가 비어 있지 않으면
            int tmp = q.poll(); // 큐에서 값 하나 꺼내서 tmp에 저장

            for(int i=0;i<3;i++) { // i가 0부터 2까지 1씩 증가하면서 반복
                int next; // next를 int 형식으로 선언

                if(i==0) { // i가 0이면
                    next = tmp + 1; // next를 tmp + 1로 설정
                } else if(i==1) { // i가 1이면
                    next = tmp - 1; // next를 tmp - 1로 설정
                } else { // i가 0도 아니고 1도 아니면
                    next = tmp * 2; // next를 tmp * 2로 설정
                }
                if(next == K) { // next가 K와 같으면
                    System.out.println(check[tmp]); // check[tmp] 출력
                    return; // 메소드 종료
                }
                if(next>=0&&next<check.length&&check[next]==0) { // next가 0보다 크거나 같고 check 배열의 길이보다 작으며 check[next]가 0이면
                    q.add(next); // 큐에 next 추가
                    check[next]=check[tmp]+1; // check[next]를 check[tmp] + 1로 설정
                }

            }
        }


    }

}
