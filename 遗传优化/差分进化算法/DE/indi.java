/*
 * The class of individual which contains position @x and fitness value @fitness.
 */


public class indi {	
	
	double [] x;
	double fitness;
	
	public indi()
	{		
		fitness = Double.NaN;
		x = new double[DE.D];
		for(int i=0; i<DE.D; i++)
			x[i] = Double.NaN;
	}

}
