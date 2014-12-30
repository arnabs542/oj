/*
 * Word Ladder
 *
 * Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
 *
 *
 */


import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class WordLadder {

    public int length;

    public boolean isConnected(String sa, String sb) {
        int length = 0;
        if (sa.length() != sb.length()) {
            return false;
        }

        length = sa.length();
        int i, diff = 0;
        for (i = 0; i < length; i++) {
            if (sa.charAt(i) != sb.charAt(i)) {
                diff++;
            }
        }

        return (diff == 1);
    }

    public int ladderLength(String start, String end, Set<String> dict) {
        // TODO Auto-generated constructor stub
        Map<String, Integer> ladderLength = Collections.synchronizedMap(new HashMap<String, Integer>());
        int length;

        for (String word : dict) {
            ladderLength.put(word, Integer.MAX_VALUE);
        }

        // the ladder length from start to start is 0
        ladderLength.put(start, 1);
        Queue<String> queue = new LinkedList<String>();
        // Breadth-first search to solve this graph shortest path problem
        /*
         * if (dict.contains(start)) { // string start is in the dictionary,ladder length is 0 return 0; }
         */
        queue.offer(start);
        dict.add(end);
        ladderLength.put(end, Integer.MAX_VALUE);
        while (!queue.isEmpty()) {
            String word = queue.poll();
            if (word.equals(end)) {
                length = ladderLength.get(word);
                return length;
            }
            // System.out.println(word);
            for (String adjString : dict) {
                if (this.isConnected(word, adjString) && ladderLength.get(word) < ladderLength.get(adjString)) {
                    ladderLength.put(adjString, ladderLength.get(word) + 1);
                    if (adjString.equals(end)) {
                        length = ladderLength.get(adjString);
                        return length;
                    }
                    queue.offer(adjString);
                    // causes java.util.ConcurrentModificationException when calling
                    // .remove with iterator

                    // dict.removeAll(new LinkedList<String>(Arrays.asList(adjString)));
                    // dict.remove(adjString);
                }
            }
        }
        length = -1;
        return length;
    }

    static public void main(String[] args) {
        Set<String> set = new HashSet<String>(Arrays.asList("hot", "dot", "lot", "log"));
        // System.out.println(set);
        LadderLength ll = new LadderLength("hit", "cog", set);
        System.out.println(ll.ladderLength("hit", "cog", set));
    }

}
