// Matching {x} Repetitions
// S must be length equal to 45
// The first 40 characters should consist of letters or even digits
// The last 5 characters should consist of odd digits or whitespace characters 
// Test with 2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
// Should output true
import java.util.*;
import java.util.regex.*;

public class XRepetitions {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^[a-zA-z02468]{40}[13579\\s]{5}$");
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
