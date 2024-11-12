class Solution {
    public int smallestEvenMultiple(int n) {
        if(n % 2 == 0){
            return n;
        }else{
            int num = n * 2;
            for(int i = num; i > n; i-=2){
                if(i % n == 0){
                    num = i;
                }
            }
            return num;
        }
    }
}