// The functions should have one double paramater to be converted
// into celsius/fahrenheit. Since celsius and fahrenheit can be decimal
// values, the input and return type is a double.



class CtoFTester {
  public static void main(String[] args) {
    System.out.println(celsiusToFahrenheit(0));  // 32F
    System.out.println(celsiusToFahrenheit(10));  // 50F
    System.out.println(fahrenheitToCelsius(32));  // 0C
    System.out.println(fahrenheitToCelsius(68));  // 20C
  }


  static double celsiusToFahrenheit(double celsius) {
    return celsius * (9.0/5.0) + 32;
  }

  static double fahrenheitToCelsius(double fahren) {
    return (fahren - 32) * (5.0/9.0);
  }


}
