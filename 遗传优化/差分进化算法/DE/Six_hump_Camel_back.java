
public class Six_hump_Camel_back {
	
	public static double f(double[] x) {
		double value =0;
		value =4*Math.pow(x[0], 2) - 2.1*Math.pow(x[0], 4)+ Math.pow(x[0],6)/3.0 + x[0]*x[1] - 4*Math.pow(x[1], 2) + 4*Math.pow(x[1], 4);
		return value;
	}

}
