/**
 * Find max volume of water a container can hold
 * 
 * @author James Crisp
 */
class Solution {
    public int maxArea(int[] height) {
        
        // Index of the left side container
        int iLeft = 0;
        // Index of the right side of the container
        int iRight = 1;
        // Max volume the container can hold
        int maxVol = (iRight - iLeft) * min(height[iLeft], height[iRight]);

        for (int i = 2; i < height.length() - 1; i++) {
            if (maxVol < (i - iLeft) * min(height(iLeft), height(i))) {
                maxVol = (i - iLeft) * min(height(iLeft), height(i));
                iRight = i;
            }
            if (maxVol < (i - iRight) * min(height(iRight), height(i))) {
                maxVol = (i - iRight) * min(height(iRight), height(i));
                iLeft = iRight;
                iRight = i;
            }
        }

        return maxVol;
    }
}