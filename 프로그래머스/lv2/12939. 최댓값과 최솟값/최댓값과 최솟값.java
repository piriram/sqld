import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        String tmp = "";
        ArrayList<Integer> al = new ArrayList<>();
        for(int i=0;i<s.length();i++){
            char tmp1 = s.charAt(i);
            if(tmp1==' '){
                al.add(Integer.parseInt(tmp));
                tmp = "";
            }else if(i==s.length()-1){
                tmp += Character.toString(tmp1);
                al.add(Integer.parseInt(tmp));
            }else{
                tmp += Character.toString(tmp1);
            }
            
            
            
            
        }
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int i=0;i<al.size();i++){
            if (al.get(i)>max){
                max = al.get(i);
            }
            if(al.get(i)<min){
                min = al.get(i);
            }
            
        }
        answer = Integer.toString(min)+" "+Integer.toString(max);

        return answer;
    }
}