class Solution {
    public String clearDigits(String s) {
        StringBuilder result = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            if (Character.isDigit(s.charAt(i)) == false){
                result.append(s.charAt(i));
            }else{
                result.deleteCharAt(result.length() - 1);
            }
        }
        s = result.toString();
        return s;
    }
}