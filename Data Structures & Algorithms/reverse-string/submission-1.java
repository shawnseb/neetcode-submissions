class Solution {
    public void reverseString(char[] s) {
        int end = (s.length -1);
        int other = end/2;
        char inter;
        for(int i = 0; i <= other; i++)
        {
            inter = s[i];
            s[i] = s[end-i];
            s[end-i] = inter;
        }
        
    }
}