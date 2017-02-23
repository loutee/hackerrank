// Alternative Matching
// S must start with Mr., Mrs., Ms., Dr., or Er.
// Rest of S must contain one or more English alphabetic letters
import java.util.*;
import java.util.regex.*;

public class CapturingAndNonCapturingGroups {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^(Mr|Mrs|Ms|Dr|Er)\\.[a-zA-Z]+$");
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
