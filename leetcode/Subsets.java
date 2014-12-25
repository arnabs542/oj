import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Subsets {

    static public List<List<Integer>> combine(int n, int k) {
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

    static public List<List<Integer>> Subsets(int[] S) {
        // TODO Auto-generated constructor stub
        List<List<Integer>> subsets = new ArrayList<List<Integer>>();
        int n = S.length, k = 0;
        for (k = 1; k <= n; k++) {
            ArrayList<List<Integer>> indexes = new ArrayList<List<Integer>>(combine(n, k));
            // System.out.println(k + " " + indexes);
            for (List<Integer> index : indexes) {
                // System.out.println(index);
                ArrayList<Integer> sets = new ArrayList<Integer>();
                for (int i : index) {
                    sets.add(S[i - 1]);
                }
                Collections.sort(sets);
                subsets.add(sets);
                // subsets.addAll(sets);
            }
        }
        return subsets;
    }

    public static void main(String[] args) {
        // initialize int array
        System.out.println((new Subsets()).Subsets(new int[] { 1, 4, 3 }));
    }
}
