class Solution {

    public List<String> validStrings(int n) {
        if(n == 1){
            List<String> result = new ArrayList<>();
            result.add("0");
            result.add("1");
            return result;
        }
        List<String> result = new ArrayList<>();
        List<String> bases = validStrings(n -1);

        for(String num : bases){
            if((num.charAt(num.length() - 1) == '0')){
                result.add(num + "1");
            }else if((num.charAt(num.length() - 1)) == '1'){
                result.add(num + "0");
                result.add(num + "1");
            }
        }

        return result;
    }
}