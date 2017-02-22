// Matching Same Text Again & Again
// S must be of length 20
// 1st character: lowercase letter
// 2nd 			: word character
// 3rd			: whitespace character
// 4th			: non word character
// 5th			: digit
// 6th			: non digit
// 7th			: uppercase letter
// 8th			: letter
// 9th			: vowl
// 10th			: non whitespace character
// 11th			: same as 1st
// 12th			: same as 2nd
// ...			: ...
// Test with: ab #1?AZa$ab #1?AZa$
// Should output: true
import java.util.*;
import java.util.regex.*;

public class SameTextAgainAndAgain {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^([a-z]\\w\\s\\W\\d\\D[A-Z][a-zA-z][aeiouAEIOU]\\S)\\1$");
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
