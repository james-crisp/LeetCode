/**
 * Create list of n numbers starting at 1. If the index in
 * the array is divisble by 3 and 5 then the string at the index
 * is "FizzBuzz". If it's divisble by only 3 then it's "Fizz", and
 * it's "Buzz" if only divisble by 5. If neither than String is index.
 * 
 * @author James Crisp
 */
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> array = new ArrayList<String>();

        for (int i = 1; i < n+1; i++) {
            if (i % 3 == 0) {
                if (i % 5 == 0) {
                    array.add("FizzBuzz");
                }
                else {
                    array.add("Fizz");
                }
            } else if (i % 5 == 0) {
                array.add("Buzz");
            } else {
                array.add(Integer.toString(i));
            }
        }

        return array;
    }
}