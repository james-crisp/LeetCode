/**
 * Tested whether a given string is a palindrome. 
 * 
 * @author James Crisp
 */
class Solution {
    public boolean isPalindrome(String s) {
        
        for (int i = 0; i < s.length(); i++) {
            if(s.charAt(i) != s.charAt(s.length()-i-1)) {
                return false;
            }
        }
        return true;
    }
}