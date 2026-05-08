class Solution {
    public int[] getConcatenation(int[] nums) {
        int n=nums.length;
        int[] ans = new int[n*2];
        System.arraycopy(nums, 0, ans, 0, n);
        // Copy second half
        System.arraycopy(nums, 0, ans, n, n);
        return ans;
    }
}