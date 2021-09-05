import java.math.*;
public class test 
{
    public static void main(String[] args) 
    {
		BigInteger a = BigInteger.valueOf(77044651);
		BigInteger c = BigInteger.valueOf(1205096635);
		a = a.pow(c);
		BigInteger b = BigInteger.valueOf(1565601761);
		a = a.mod(b);
        System.out.println(a);
    }
}
