// Matching Zero Or More Repetitions
// S should begin with 2 or more digits
// After that S should have 0 or more lowercase letters
// S should end with 0 or more uppercase letters
import java.util.*;
import java.util.regex.*;

public class ZeroOrMoreRepetitions {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^\\d{2,}[a-zA-Z]*0*$");
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
