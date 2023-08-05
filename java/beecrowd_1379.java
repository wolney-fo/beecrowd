import java.util.Scanner;

public class beecrowd_1379 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b;

        while (true) {
            a = sc.nextInt();
            b = sc.nextInt();

            if (a == 0 && b == 0) {
                break;
            }

            System.out.println(2 * a - b);
        }
    }
}
