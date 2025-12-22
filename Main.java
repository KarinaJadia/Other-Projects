import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("Hello World");
    String response = input.nextLine();
    System.out.println(response);
    input.close();
  }
}