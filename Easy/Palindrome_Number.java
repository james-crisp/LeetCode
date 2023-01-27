/**
 * Method isPalindrome checks whether a number is a palindrome. If the number
 * is negative, it is not a palindrome. The number must read the same forwards 
 * and backwards.
 * 
 * @author James Crisp
 */
class Solution {
    public boolean isPalindrome(int x) {
        // If integer is negative, not a palindrome
        if (x < 0) {
            return false;
        }

        // Convert integer to string
        String stringX = Integer.toString(x);
        
        // Iterate through string and see if forwards and backwards are alike
        for (int i = 0; i < stringX.length(); i++) {
            if (stringX.charAt(i) != stringX.charAt(stringX.length()-i-1)) {
                return false;
            }
        }
        // Number is a palindrome, return true
        return true;
    }
}