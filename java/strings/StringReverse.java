// Java String Reverse
import java.io.*;
import java.util.*;

public class StringReverse {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String A = sc.next();

		StringBuilder reverseA = new StringBuilder();
		reverseA.append(A);
		reverseA = reverseA.reverse();

		if (A.equalsIgnoreCase(reverseA.toString())) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}
	}
}
