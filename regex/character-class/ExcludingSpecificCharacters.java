// Excluding Specific Characters
// Input of length 6
// 		First character: 	not a digit [0-9]
// 		Second character:	not lowercase vowel [aeiou]
// 		Third character:	not [bcDF]
// 		Fourth character:	not whitespace character
// 		Fifth character:	not uppercase vowel [AEIOU]
// 		Sixth character:	not . or ,
import java.util.*;
import java.util.regex.*;

public class ExcludingSpecificCharacters {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^\\D[^aeiou][^bcDF]\\S[^AEIOU][^.,]$");
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
