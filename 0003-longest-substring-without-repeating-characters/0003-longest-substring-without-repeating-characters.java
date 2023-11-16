class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap();
        int right = 0, max = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                right = Math.max(right, map.get(c)+1);
            }
            map.put(c, i);
            max = Math.max(max, i - right +1);
        }
        return max;
    }
}