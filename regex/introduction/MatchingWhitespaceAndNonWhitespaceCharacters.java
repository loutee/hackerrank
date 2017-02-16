// Matching Whitespace & Non-Whitespace Character
// Matches pattern XXxXXxXX
// 	Where x denotes whitespace characters
// 		  X denotes non-whitespace characters
import java.util.*;
import java.util.regex.*;

public class MatchingWhitespaceAndNonWhitespaceCharacters {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("\\S\\S\\s\\S\\S\\s\\S\\S");
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
