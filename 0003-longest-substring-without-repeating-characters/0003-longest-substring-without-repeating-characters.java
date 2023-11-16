class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap();
        int right = 0, max = 0;
        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                right = right > map.get(s.charAt(i)) + 1 ? right : map.get(s.charAt(i)) + 1;
            }
            map.put(s.charAt(i), i);
            max = max > i - right + 1 ? max : i - right + 1;
        }
        return max;
    }
}