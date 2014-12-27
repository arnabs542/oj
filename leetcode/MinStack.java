public class MinStack {

    // Built-in Stack implementation
    // ArrayList leads to "Memory Limit Exceeds"
    private Stack<Integer> stack    = new Stack<Integer>();
    private Stack<Integer> minStack = new Stack<Integer>();

    public MinStack() {
        // TODO Auto-generated constructor stub
    }

    public void push(int x) {
        stack.add(x);
        if (minStack.isEmpty() || x <= minStack.peek()) {
            minStack.push(x);
        }
    }

    public void pop() {
        if (minStack.peek().equals(stack.peek())) {
            minStack.pop();
        }
        stack.pop();
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }

    public static void main(String[] args) {
        // TODO Auto-generated method stub
    }
}
