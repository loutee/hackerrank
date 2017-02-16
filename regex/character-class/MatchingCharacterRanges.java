// Matching Character Ranges
// Input of length >=5 
// 		First character: 	Lowercase English alphabetic character
// 		Second character:	Positive digit
// 		Third character:	Not a lowercase alphabetic character
// 		Fourth character:	Not an uppercase alphabetic character
// 		Fifth character:	Uppercase alphabetic character
import java.util.*;
import java.util.regex.*;

public class MatchingCharacterRanges {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^[a-z][1-9][^a-z][^A-Z][A-Z]");
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
