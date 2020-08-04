import java.util.Stack;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
	public static void main(String[] args) throws IOException
	{
		Stack<Character> right = new Stack<>();
		Stack<Character> left = new Stack<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		char[] line = br.readLine().toCharArray();
		int loop = Integer.parseInt(br.readLine());
		for (int i = 0; i < line.length; i++)
			left.add(line[i]);
		while (loop != 0) {
			loop -= 1;
			char[] inst = br.readLine().toCharArray();
			if (inst[0] == 'L') {
				if (left.isEmpty())
					continue;
				else 
					right.add(left.pop());
			}
			else if (inst[0] == 'D') {
				if (right.isEmpty())
					continue;
				else 
					left.add(right.pop());

			}
			else if (inst[0] == 'P') {
				left.add(inst[2]);
			}
			else if (inst[0] == 'B') {
				if (left.isEmpty())
					continue;
				else
					left.pop();
			}
			
				
		}
		while (!left.isEmpty()) {
			right.add(left.pop());
		}
		StringBuilder sb = new StringBuilder();
		int size = right.size();
		for (int i = 0; i < size; i++) {
			char temp = right.pop();
			sb.append(temp);
		}
		System.out.print(sb + "\n");
	}
}
