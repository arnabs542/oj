import java.util.ArrayList;
import java.util.List;

public class Solution {

    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> combinations = new ArrayList<List<Integer>>();
        // n == k is acceptable
        if (n < k || k <= 0 || n <= 0) {
            return null;
        }
        int icur = 0;
        List<Integer> combination = new ArrayList<Integer>();
        for (int i = 0; i < k; i++) {
            combination.add(-1);
        }

        while (icur >= 0) {
            if (icur == k) {
                // filled all slot,seeking next combination solution
                icur--;
            }
            if (combination.get(icur) == -1) {
                // fill next slot
                if (icur > 0) {
                    combination.set(icur, combination.get(icur - 1) + 1);
                } else {
                    // Fill in the 1st slot first time.
                    combination.set(icur, 1);
                }
                // icur++;
            } else {
                // increase the index on current slot by 1 to find next combination
                combination.set(icur, combination.get(icur) + 1);
            }

            // validation
            if (combination.get(icur) > n) {
                combination.set(icur, -1);
                icur--;
                continue;
            } else {
                icur++;
            }

            if (icur == k) {
                // filled all slot,generating a combination
                // We need to copy a List,not adding this list.
                combinations.add(new ArrayList<Integer>(combination));
            }
        }
        return combinations;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        List<List<Integer>> sols = sol.combine(5, 5);
        System.out.println("Solutions are");
        System.out.println(sols);
    }
}
