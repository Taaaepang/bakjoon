package stack;
import java.util.Scanner;

public class stack {
	int[] stack = new int[10000];
	int size = 0;
	
	stack(){}
	public void push(int num) {
		size += 1;
		stack[size] = num;
	}
	public int pop() {
		if(size == 0)
			return -1;
		else {
			int temp = stack[size-1];
			stack[size-1] = 0;
			size -= 1;
			return temp;
		}
	}
	public int size() {
		return size;
	}
	public int empty() {
		if(size == 0)
			return 1;
		else
			return 0;
	}
	public int top() {
		if(size == 0)
			return -1;
		else {
			return stack[size];
		}
	}
	
	public static void main(String[] args)
	{
		stack stack = new stack();
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		System.out.print("\n");
		while(true) {
			String inst = sc.nextLine();
			String[] temp = inst.split(" ");
			System.out.println(temp[0]);
			if(temp[0].equals("push"))
			{
				int num = Integer.parseInt(temp[1]);
				stack.push(num);
			}
			if(temp[0].equals("pop"))
				System.out.println(stack.pop());
			if(temp[0].equals("top")) {
				System.out.println(stack.top());
			}
			if(temp[0].equals("size"))
				System.out.println(stack.size());
			if(temp[0].equals("empty"))
				System.out.println(stack.empty());
			// System.out.println(size);
			if (!sc.hasNextLine())
			{
				break;
			}
		}
	}
}
