package subnet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("enter subnet:");
    String response = input.nextLine();
    System.out.println(response);
    input.close();
  }
}