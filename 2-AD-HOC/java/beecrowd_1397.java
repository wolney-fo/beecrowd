import java.util.Scanner;

public class beecrowd_1397 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, a, b, count_a, count_b;

        while (true) {
            n = sc.nextInt();

            if (n == 0) {
                break;
            }

            count_a = count_b = 0;

            for (int i=0; i<n; i++) {
                a = sc.nextInt();
                b = sc.nextInt();

                if (a > b) {
                    count_a++;
                } else if (b > a) {
                    count_b++;
                }
            }

            System.out.printf("%d %d\n", count_a, count_b);
        }
    }
}
