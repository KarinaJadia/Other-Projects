package subnet;

public class Subnet {
  String raw; // the raw input subnet: 68.168.0.34/29
  String address; // binary-ized subnet address
  String netmask; // 32-29 = 3 host bits

  public Subnet(String raw) {
    this.raw = raw;
  }

  public String bionize() {
    String[] raws = raw.split("[./]");
    return raw;
  }
}