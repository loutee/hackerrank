// Java End-of-file
import java.io.*;
import java.util.*;

public class JavaEndOfFile {
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int count = 1;
		while(in.hasNextLine()) {
			System.out.println(count + " " + in.nextLine());
			count++;
		}
	}
}
