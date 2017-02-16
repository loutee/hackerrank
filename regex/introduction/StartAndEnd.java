// Matching Start & End 
// Matches pattern Xxxxx.
// 	Where x denotes a word character
// 		  X denotes a digit 
import java.util.*;
import java.util.regex.*;

public class StartAndEnd {

		public static void main(String[] args) {
			
			Regex_Test tester = new Regex_Test();
			tester.checker("^\\d\\w{4}.$");
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
