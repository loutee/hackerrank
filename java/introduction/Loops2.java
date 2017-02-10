// Java Loops 2
import java.util.*;

public class Loops2 {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		for(int i=0; i<t; i++) {
			int a = in.nextInt();
			int b = in.nextInt();
			int n = in.nextInt();

			int s = 0;
			for(int j=0; j<n; j++) {
				s = a;
				for(int k=j; k>=0; k--) {
					s += (Math.pow(2, k)*b);
				}
				System.out.printf(s + " ");
			}
			System.out.println();
		}
		in.close();
	}
}
