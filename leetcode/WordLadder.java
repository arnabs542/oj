/*
 * Word Ladder
 *
 * Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
 *
 * Only one letter can be changed at a time
 * Each intermediate word must exist in the dictionary
 * For example,
 *
 * Given:
 * start = "hit"
 * end = "cog"
 * dict = ["hot","dot","dog","lot","log"]
 * As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * return its length 5.
 *
 * Note:
 * Return 0 if there is no such transformation sequence.
 * All words have the same length.
 * All words contain only lowercase alphabetic characters.
 *
 *
 * Algorithm:
 * This is a shortest path problem in Graph theory.If the Edit Distance between two words is the distance 
 * between two vertices representing them.
 * For shorest path problem, we have breadth-fist search problem.
 *      Naively,we can build the graph with time complexity of O(|V|*|V|),and do a BFS in O(|V|+|E|).This 
 * implementation will fail the big data test.To optimize the code,we can get around the graph building process:
 * We store vertices in a hash table,thus retrieving them in constant time.Initially,we push the start word into 
 * the queueWhile Breadth-first searching,do change one character each time with a word,and check if it's in the 
 * dictionary.If it's in,then we push it into a queue,updating its search depth.Then we can find the shortest path
 * in O(|V| * L * 26).L is the words' length.
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

    // Check if two words are 1 distance from each other,no used actually
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
        Map<String, Integer> ladderLength = Collections.synchronizedMap(new HashMap<String, Integer>());
        int length;
        for (String word : dict) {
            ladderLength.put(word, Integer.MAX_VALUE);
        }

        // the ladder length from start to start is 0.
        // Initialization
        ladderLength.put(start, 1);
        Queue<String> queue = new LinkedList<String>();
        queue.offer(start);
        dict.add(end);
        ladderLength.put(end, Integer.MAX_VALUE);
        
        // maintenance
        while (!queue.isEmpty()) {
            String word = queue.poll();
            // termination
            if (word.equals(end)) {
                length = ladderLength.get(word);
                return length;
            }
            
            int l = word.length();
            for (int i = 0; i < l; i++) {
                char[] arr = word.toCharArray();
                for (char c = 'a'; c <= 'z'; c++) {
                    arr[i] = c;
                    String newWord = new String(arr);
                    if (dict.contains(newWord) && !newWord.equals(word)) {
                        dict.remove(newWord);
                        queue.offer(newWord);
                        ladderLength.put(newWord, ladderLength.get(word) + 1);
                        System.out.println(ladderLength);
                    }
                }
            }
            /*
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
            */
        }
        return 0;
    }

    static public void main(String[] args) {
        Set<String> set = new HashSet<String>(Arrays.asList("hot", "dot", "lot", "log"));
        // System.out.println(set);
        WordLadder ll = new WordLadder();
        System.out.println(ll.ladderLength("hit", "cog", set));
        
        set = new HashSet<String>(Arrays.asList("a","b","c"));
        System.out.println(ll.ladderLength("a","c"));
    }
}
