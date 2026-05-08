class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, ArrayList<Integer>> set = new HashMap<>();
        for(int i = nums.length-1; i >= 0; i--)
        {
            if(set.get(nums[i]) == null)
            {
                ArrayList<Integer> list = new ArrayList<>();
                list.add(i);
                set.put(nums[i], list);
            } else {
                ArrayList<Integer> list = set.get(nums[i]);
                list.add(nums[i]);
            }
        }
        for(int i = 0; i <nums.length; i++)
        {
            int newt = target - nums[i];
            if(set.get(newt)!=null)
            {
                ArrayList<Integer> list = set.get(newt);
                for(int k = 0; k < list.size(); k++)
                {
                    if(i != list.get(k))
                    {
                        int [] ans = new int [2];
                        ans[0] = i;
                        ans[1] = list.get(k);
                        return ans;
                    }
                }   
            }
        }
        return null;
    }
}
