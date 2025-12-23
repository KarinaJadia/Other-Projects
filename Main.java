import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);

    System.out.println("enter subnet:");
    String response = input.nextLine();
    String[] raws = response.split("[./]");

    System.out.println(raws.toString());

    input.close();
  }
}