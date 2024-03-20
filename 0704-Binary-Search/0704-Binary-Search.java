class Solution {
    public static int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1 ;

        while (left <= right) {
            int middle = left +(right - left) / 2;
            System.out.println(middle);
            if (nums[middle] == target) {
                return middle;
            }
            if (target > nums[middle]) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] x = {9};
        System.out.println(search(x, 9));
    }
}