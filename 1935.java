import java.util.Stack;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int loop = Integer.parseInt(br.readLine());
		char[] sik = br.readLine().toCharArray();
		Double[] num = new Double[27];
		Stack<Double> stack = new Stack<>();
		for (int i = 0; i < loop; i++) {
			num[i] = Double.parseDouble(br.readLine());
		}
		int length = sik.length;
		for (int i = 0; i < length; i++) {
			if (sik[i] >= 65 && sik[i] <= 90) 
				stack.add(num[sik[i]-65]);
			else {
				Double num1 = stack.pop();
				Double num2 = stack.pop();
				if (sik[i] == 42)
					stack.add(num2*num1);
				else if (sik[i] == 43)
					stack.add(num2+num1);
				else if (sik[i] == 45)
					stack.add(num2-num1);
				else if (sik[i] == 47)
					stack.add(num2/num1);
			}		
		}
		Double answer = stack.pop();
		String str = String.format("%.2f", answer);
		System.out.print(str + "\n");
	}
}