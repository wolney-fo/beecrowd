import java.util.Scanner;

public class beecrowd_1250 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i= 0; i<n; i++) {
            int counter = 0;

            int t = sc.nextInt();
            int[] tiros = new int[50];
            for (int j=0; j<t; j++) {
                tiros[j] = sc.nextInt();
            }
            String pulos = sc.next();

            for (int j=0; j<t; j++) {
                if ( (tiros[j] <= 2 && pulos.charAt(j) == 'S') || (tiros[j] > 2 && pulos.charAt(j) == 'J') ) {
                    counter++;
                }
            }

            System.out.println(counter);
        }

        sc.close();
    }
}
