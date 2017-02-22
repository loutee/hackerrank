// Matching One Or More Repetitions
// S should begin with 1 or more digits
// After that S should have 1 or more uppercase letters
// S should end with 1 or more lowercase letters
import java.util.*;
import java.util.regex.*;

public class OneOrMoreRepetitions {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^\\d+[A-Z]+[a-z]+$");
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
