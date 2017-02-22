// Matching Word Boundaries
// Match word starting with vowel
// Matched word can be of any length
// Should consist of letters only
// Must start and end with a word boundary
import java.util.*;
import java.util.regex.*;

public class WordBoundaries {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("\\b[aeiouAEIOU]*[a-zA-Z]*\\b");
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
