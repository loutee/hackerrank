// Matching {x, y} Repetitions
// S must begin with 1 or 2 digits
// after, S should have 3 or more letters
// then, S should end with 0 to 3 . symbols 
// Test with 3threeormorealphabets.
// Outputs true
import java.util.*;
import java.util.regex.*;

public class XYRepetitions {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^\\d{1,2}[a-zA-Z]{3,}\\.{0,3}$");
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
