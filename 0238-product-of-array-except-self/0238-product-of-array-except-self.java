class Solution {
    public int[] productExceptSelf(int[] nums) {
        int temp=nums.length;
        int [] res = new int[temp];
        res[0]=1;
        for (int i = 1; i<temp;i++){
            res[i]=nums[i-1]*res[i-1];
        }
        int suffix =1;
        for (int i = temp-1; i>-1 ;i--){
            res[i]=res[i]*suffix;
            suffix*=nums[i];
        }
        return res;
    }
}
