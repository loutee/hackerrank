// Matching Ending Items
// S should consist of only lowercase and uppercase letters
// S should end in s
import java.util.*;
import java.util.regex.*;

public class EndingItems {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^[a-zA-z]*s$");
		}
}

class Regex_Test {

	public void checker(String Regex_Pattern) {
		
		Scanner Input = new Scanner(System.in);
		String Test_String = Input.nextLine();
		Pattern p = Pattern.compile(Regex_Pattern);
		Matcher m = p.matcher(Test_String);
		System.out.println(m.find());
	}
}
