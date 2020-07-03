package bakjoon;
import java.util.Stack;
public class exam9013 {

	public static void main(String[] args) {
		String in = "backjoon online judge";
		String out = null;
		Stack<Character> stack = new Stack<>();
		String[] str = in.split(" ");
		char[] temp = new char[10];
		int k = 0;
		for(int i = 0; i < 3 ; i++)
		{
			char[] ctr = str[i].toCharArray();
			for(int j = 0; j < str[i].length() ;j++)
				stack.push(ctr[j]);
			while(!stack.empty())
			{
				temp[k] = stack.pop();
				k++;
			}
			out = String.copyValueOf(temp);
			temp = new char[10];
			k = 0;
			System.out.print(out);

		}
		
	}

}
