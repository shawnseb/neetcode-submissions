class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        for (int num : nums) {
            // If our count hits zero, we pick a new potential candidate
            if (count == 0) {
                candidate = num;
            }
            
            // If the current number matches our candidate, increment
            // Otherwise, decrement (the "cancellation")
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
}