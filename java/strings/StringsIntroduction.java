// Java Strings Introduction
import java.io.*;
import java.util.*;

public class StringsIntroduction {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String A = sc.next();
		String B = sc.next();

		// Sum of lengths of A and B
		System.out.println(A.length() + B.length());
		
		// Determine if A is lexicographically larger than B
		if (A.compareTo(B) > B.compareTo(A)) {
			System.out.println("Yes");
		} else {
			System.out.println("No");
		}

		// Capitalize first letter in A and B
		System.out.print(Character.toUpperCase(A.charAt(0)));
		for (int i=1; i<A.length(); i++) {
			System.out.print(A.charAt(i));
		}
		System.out.print(" ");

		System.out.print(Character.toUpperCase(B.charAt(0)));
		for (int i=1; i<B.length(); i++) {
			System.out.print(B.charAt(i));
		}
		System.out.println();	
	}
}
