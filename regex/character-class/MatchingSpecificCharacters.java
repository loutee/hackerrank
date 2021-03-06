// Matching Specific Characters
// Input of length 6
// 		First character: 	1, 2, or 3
// 		Second character:	1, 2, or 0
// 		Third character:	x, s, or 0
// 		Fourth character:	3, 0, A, or a
// 		Fifth character:	x, s, or u
// 		Sixth character:	. or ,
import java.util.*;
import java.util.regex.*;

public class MatchingSpecificCharacters {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^[123][120][xs0][30Aa][xsu][.,]$");
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
