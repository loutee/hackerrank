// Matching Word & Non-Word Character
// Matches pattern xxxXxxxxxxxxxxXxxx
// 	Where x denotes any word character character
// 		  X denotes any non-word character
import java.util.*;
import java.util.regex.*;

public class WordAndNonWordCharacter {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("\\w{3}\\W\\w{10}\\W\\w{3}");
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
