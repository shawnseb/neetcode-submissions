class Solution {
    public void reverseString(char[] s) {
        int end = s.length -1;
        char inter;
        for(int i = 0; i <= end/2; i++)
        {
            inter = s[i];
            s[i] = s[end-i];
            s[end-i] = inter;
        }
        
    }
}