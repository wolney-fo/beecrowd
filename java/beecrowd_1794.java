import java.util.Scanner;

public class beecrowd_1794 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n, la, lb, sa, sb;

        n = sc.nextInt();
        la = sc.nextInt();
        lb = sc.nextInt();
        sa = sc.nextInt();
        sb = sc.nextInt();

        if ((la <= n && n <= lb) && (sa <= n && n <= sb)) {
            System.out.println("possivel");
        } else {
            System.out.println("impossivel");
        }

        sc.close();
    }
}
