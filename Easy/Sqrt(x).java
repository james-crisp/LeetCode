/**
 * Return the square root of x rounded down to the nearest integer.
 * 
 * @author James Crisp
 */
class Solution {
    public int mySqrt(int x) {
        for (int i = 0; i <= x + 1; i++) {
            if (i * i > x) {
                return i - 1;
            }
        }
        return -1;
    }
}