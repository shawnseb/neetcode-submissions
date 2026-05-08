

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // 1. Count frequencies using a HashMap
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // 2. Create a list of your custom 'Element' objects
        List<Element> list = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            list.add(new Element(entry.getKey(), entry.getValue()));
        }

        // 3. Sort the list (Collections.sort uses your compareTo logic)
        // We want descending order (highest frequency first)
        Collections.sort(list);

        // 4. Extract the top K 'actual' values
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            ans[i] = list.get(i).actual;
        }
        return ans;
    }

    // Fixed: Must implement Comparable<Element> for sorting to work
    class Element implements Comparable<Element> {
        int actual;
        int freq;

        public Element(int act, int f) {
            actual = act;
            freq = f;
        }

        @Override
        public int compareTo(Element l) {
            // Sort by frequency in descending order
            return l.freq - this.freq;
        }
    }
}