package longestConsecutive;

import java.util.Hashtable;

public class LongestConsecutive {

    static public int LongestConsecutive(int[] num) {
        // TODO Auto-generated constructor stub
        Hashtable<Integer, Integer> table = new Hashtable<Integer, Integer>();
        int curr = 1, length = 0, left, right;
        for (int i : num) {
            table.put(i, 1);
        }

        for (int e : num) {
            left = e - 1;
            right = e + 1;
            length = 1;

            while (table.containsKey(left)) {
                length++;
                table.remove(left);
                left--;
            }

            while (table.containsKey(right)) {
                length++;
                table.remove(right);
                right++;
            }

            if (length > curr) {
                curr = length;
            }
        }

        return curr;
    }

    public static void main(String[] args) {
        System.out.println(LongestConsecutive(new int[] { 100, 4, 200, 1, 3, 2 }));
    }
}
