import java.util.Scanner;

public class beecrowd_1026 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextLong()) {
            long a = scanner.nextLong();
            long b = scanner.nextLong();
            System.out.println(a ^ b);
        }
    }
}
