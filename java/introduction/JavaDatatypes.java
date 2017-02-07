// Java Datatypes
import java.util.*;

public class JavaDatatypes {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();

		for (int i=0; i<t; i++) {
			try {
				long x = sc.nextLong();
				System.out.println( x + " can be fitted in:");
				// Byte, 4 bits: [-128, 127]
				if (x>=Byte.MIN_VALUE && x<=Byte.MAX_VALUE) {
				   System.out.println("* byte");
				}

				// Short, 8 bits: [-32768, 32767] 
				if (x>=Short.MIN_VALUE && x<=Short.MAX_VALUE) {
				   System.out.println("* short");
				}

				// Int, 16 bits: [-2147483648, 2147483647]
				if (x>=Integer.MIN_VALUE && x<=Integer.MAX_VALUE) {
				   System.out.println("* int");
				}

				// Long, 32 bits: !Integers too big to be compared with
				if (x>=Long.MIN_VALUE && x<=Long.MAX_VALUE) {
				   System.out.println("* long");
				}
			} catch (Exception e) {
				System.out.println(sc.next() + " can't be fitted anywhere.");
			}
		}
	}
}
