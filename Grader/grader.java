import java.io.*;

public class Task
{
	public static void main(String[] args) throws IOException
	{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		String s;
		while ((s = in.readLine()) != null && s.length() != 0)
		{
			String integers[] = s.split(" ");
			int sum = AdditionTest.Add(Integer.valueOf(integers[0]), Integer.valueOf(integers[1]));
			System.out.println(sum);
		}
	}
}
