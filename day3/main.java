import java.util.Scanner;
public class main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int ans = 0;
        for (int i = 0; i < 100; ++i) {
            String s = in.next(), x = in.next(), y = in.next();
            boolean found = true;
            for (int j = 0; found && j < s.length(); ++j) {
                for (int k = 0; found && k < x.length(); ++k) {
                    for (int l = 0; found && l < y.length(); ++l) {
                        if (s.charAt(j) == x.charAt(k) && x.charAt(k) == y.charAt(l)) {
                            found = false;
                            if (s.charAt(j) <= 'Z') {
                                ans += s.charAt(j) - 'A' + 1;
                            }
                            else {
                                ans += s.charAt(j) - 'a' + 27;
                            }
                        }
                    }
                }
            }
        }
    System.out.println(ans);
    }
}
